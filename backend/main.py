import base64
import urllib.parse
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from agent.market_agent import market_agent
from agent.llm_advisor import get_farmer_advice

from backend.database import (
    create_tables,
    insert_sample_data,
    get_connection
)

from ml.price_model import (
    predict_price,
    predict_price_details
)

from services.market_intel import (
    get_market_rating,
    get_weather_conditions,
    get_crop_spoilage_risk,
    evaluate_crop_quality_from_harvest_date,
    calculate_holding_spoilage_and_loss
)

from services.live_mandi_service import (
    fetch_live_mandi_prices,
    sync_daily_prices_to_db,
    format_target_date
)

from services.geo_market_service import (
    discover_markets_in_radius,
    get_market_distance,
    geocode_location,
    get_road_distance_and_time,
    resolve_location
)

from services.voice_service import (
    extract_parameters_with_llm_fallback,
    transcribe_audio_bytes,
    generate_farmer_voice_script,
    generate_speech_audio_base64
)


# ============================================================
# FASTAPI CONFIGURATION
# ============================================================

app = FastAPI(
    title="Farmer-to-Market Intelligence API",
    description="AI-powered backend for farmer market intelligence",
    version="1.0.0"
)


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

create_tables()
insert_sample_data()


# ============================================================
# REQUEST MODEL
# ============================================================

class FarmerRequest(BaseModel):
    crop: str
    location: str
    quantity: float
    quality: str
    harvest_date: str
    price_date: Optional[str] = None
    radius_km: Optional[float] = 50.0
    detected_language: Optional[str] = "en"


# ============================================================
# CROP MAPPING (24 Authentic Telangana Crops)
# ============================================================

CROP_MAPPING = {
    # 1. Cereals & Millets
    "Rice": ["Rice", "Paddy(Common)", "Paddy(Basmati)", "Broken Rice"],
    "Maize": ["Maize", "Sweet Corn", "Baby Corn"],
    "Jowar": ["Jowar(Sorghum)", "Jowar"],
    "Bajra": ["Bajra(Pearl Millet/Cumbu)", "Bajra"],
    "Ragi": ["Ragi(Finger Millet)", "Ragi"],

    # 2. Pulses
    "Red Gram": ["Red gram/Arhar/Tur(whole)", "Pegeon Pea(Arhar Fali)", "Red Gram", "Tur", "Arhar"],
    "Bengal Gram": ["Bengal Gram(Gram)(Whole)", "Kabuli Chana(Chickpeas-White)", "Gram Raw(Chholia)", "Bengal Gram", "Chana"],
    "Green Gram": ["Green Gram(Moong)(Whole)", "Green Gram", "Moong"],
    "Black Gram": ["Black Gram(Urd Beans)(Whole)", "Black Gram Dal(Urd Dal)", "Black Gram", "Urad"],

    # 3. Oilseeds
    "Groundnut": ["Groundnut", "Groundnut pods(raw)"],
    "Soybean": ["Soyabean", "Soybean"],
    "Sunflower": ["Sunflower/Sunflower Seed", "Sunflower"],
    "Sesamum": ["Sesamum", "Gingelly", "Til", "Mustard"],
    "Castor": ["Castor Seed", "Castor"],

    # 4. Spices & Commercial
    "Chilli": ["Chilli", "Green Chilli", "Chili Red"],
    "Cotton": ["Cotton"],
    "Turmeric": ["Turmeric", "Haldi"],
    "Ginger": ["Ginger(Green)", "Ginger"],
    "Garlic": ["Garlic"],

    # 5. Vegetables
    "Tomato": ["Tomato"],
    "Onion": ["Onion", "Onion Green"],
    "Brinjal": ["Brinjal"],
    "Bhendi": ["Bhindi(Ladies Finger)", "Ladies Finger", "Bhendi", "Bhindi"],
    "Bitter Gourd": ["Bitter gourd", "Bitter Gourd"]
}


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Farmer Market Intelligence API is running"
    }


# ============================================================
# LIVE MANDI PRICES (AGMARKNET / DATA.GOV.IN)
# ============================================================

@app.get("/live-mandi-prices")
def live_mandi_prices(
    crop: str,
    location: str = "Hyderabad",
    date: str = None
):
    return fetch_live_mandi_prices(crop=crop, location=location, target_date=date)


@app.post("/sync-live-data")
def sync_live_data(
    crop: str,
    location: str = "Hyderabad",
    date: str = None
):
    count = sync_daily_prices_to_db(crop=crop, location=location, target_date=date)
    return {
        "status": "success",
        "message": f"Successfully synchronized {count} daily market records for {crop}",
        "records_synced": count,
        "date": format_target_date(date)
    }


# ============================================================
# MARKET PRICE
# ============================================================

@app.get("/market-price")
def market_price(
    crop: str,
    location: str,
    date: str = None
):

    crop_names = CROP_MAPPING.get(
        crop,
        [crop]
    )

    connection = get_connection()
    cursor = connection.cursor()

    placeholders = ",".join(
        ["?"] * len(crop_names)
    )

    farmer_location = location.lower().strip()

    # --------------------------------------------------------
    # LOCATION FILTER
    # --------------------------------------------------------

    if "hyderabad" in farmer_location:

        location_condition = """
            AND (
                LOWER(location) LIKE '%hyderabad%'
                OR LOWER(location) LIKE '%ranga reddy%'
                OR LOWER(location) LIKE '%rangareddy%'
                OR LOWER(location) LIKE '%medchal%'
            )
        """

        location_params = []

    elif "telangana" in farmer_location:

        location_condition = """
            AND LOWER(location) LIKE '%telangana%'
        """

        location_params = []

    else:

        location_condition = """
            AND LOWER(location) LIKE ?
        """

        location_params = [
            f"%{farmer_location}%"
        ]

    # --------------------------------------------------------
    # DATE FILTER & AUTO SYNC
    # --------------------------------------------------------

    if date:
        target_d = format_target_date(date)
        cursor.execute(
            f"SELECT COUNT(*) as cnt FROM market_prices WHERE crop IN ({placeholders}) AND date = ?",
            crop_names + [target_d]
        )
        if cursor.fetchone()["cnt"] == 0:
            sync_daily_prices_to_db(crop, location, target_date=target_d)

        query = f"""
            SELECT
                market,
                location,
                price_per_kg,
                date
            FROM market_prices
            WHERE crop IN ({placeholders})
            AND date = ?
            {location_condition}
            ORDER BY price_per_kg DESC
            LIMIT 1
        """
        query_params = crop_names + [target_d] + location_params
    else:
        query = f"""
            SELECT
                market,
                location,
                price_per_kg,
                date
            FROM (
                SELECT
                    market,
                    location,
                    price_per_kg,
                    date,
                    ROW_NUMBER() OVER (
                        PARTITION BY market
                        ORDER BY
                            date DESC,
                            price_per_kg DESC
                    ) AS row_num
                FROM market_prices
                WHERE crop IN ({placeholders})
                {location_condition}
            )
            WHERE row_num = 1
            ORDER BY price_per_kg DESC
            LIMIT 1
        """
        query_params = crop_names + location_params

    cursor.execute(
        query,
        query_params
    )

    row = cursor.fetchone()

    connection.close()

    # --------------------------------------------------------
    # NO DATA
    # --------------------------------------------------------

    if row is None:

        return {

            "crop": crop,

            "location": location,

            "market": "No market found",

            "market_location": "N/A",

            "price_per_kg": 0,

            "date": "",

            "message":
                "No market data available for "
                "this crop and location"
        }

    # --------------------------------------------------------
    # RESPONSE
    # --------------------------------------------------------

    return {

        "crop": crop,

        "location": location,

        "market": row["market"],

        "market_location":
            row["location"],

        "price_per_kg":
            row["price_per_kg"],

        "date":
            row["date"]
    }


# ============================================================
# NEARBY MARKETS (30-50 KM RADIUS DISCOVERY)
# ============================================================

@app.get("/nearby-markets")
def nearby_markets(
    crop: str,
    location: str = "Hyderabad",
    radius_km: float = 50.0,
    date: str = None
):
    discovered = discover_markets_in_radius(
        crop=crop,
        farmer_location=location,
        radius_km=radius_km,
        target_date=date
    )
    return {
        "crop": crop,
        "location": location,
        "radius_km": radius_km,
        "count": len(discovered),
        "markets": discovered
    }


# ============================================================
# MARKET COMPARISON
# ============================================================

@app.get("/market-comparison")
def market_comparison(
    crop: str,
    location: str = "Hyderabad",
    date: str = None,
    radius_km: float = 50.0
):
    # Dynamic 30-50 km radius discovery
    if radius_km and radius_km > 0:
        discovered = discover_markets_in_radius(
            crop=crop,
            farmer_location=location,
            radius_km=radius_km,
            target_date=date
        )
        if discovered:
            return {
                "crop": crop,
                "location": location,
                "radius_km": radius_km,
                "count": len(discovered),
                "markets": discovered
            }

    crop_names = CROP_MAPPING.get(
        crop,
        [crop]
    )

    connection = get_connection()
    cursor = connection.cursor()

    placeholders = ",".join(
        ["?"] * len(crop_names)
    )

    farmer_location = location.lower().strip()

    # --------------------------------------------------------
    # LOCATION FILTER
    # --------------------------------------------------------

    if "hyderabad" in farmer_location:

        location_condition = """
            AND (
                LOWER(location) LIKE '%hyderabad%'
                OR LOWER(location) LIKE '%ranga reddy%'
                OR LOWER(location) LIKE '%rangareddy%'
                OR LOWER(location) LIKE '%medchal%'
            )
        """

        location_params = []

    elif "telangana" in farmer_location:

        location_condition = """
            AND LOWER(location) LIKE '%telangana%'
        """

        location_params = []

    else:

        location_condition = """
            AND LOWER(location) LIKE ?
        """

        location_params = [
            f"%{farmer_location}%"
        ]

    # --------------------------------------------------------
    # DATE FILTER & AUTO SYNC
    # --------------------------------------------------------

    if date:
        target_d = format_target_date(date)
        cursor.execute(
            f"SELECT COUNT(*) as cnt FROM market_prices WHERE crop IN ({placeholders}) AND date = ?",
            crop_names + [target_d]
        )
        if cursor.fetchone()["cnt"] == 0:
            sync_daily_prices_to_db(crop, location, target_date=target_d)

        query = f"""
            SELECT
                market,
                location,
                price_per_kg,
                date
            FROM market_prices
            WHERE crop IN ({placeholders})
            AND date = ?
            {location_condition}
            ORDER BY price_per_kg DESC
            LIMIT 10
        """
        query_params = crop_names + [target_d] + location_params
    else:
        query = f"""
            SELECT
                market,
                location,
                price_per_kg,
                date
            FROM (
                SELECT
                    market,
                    location,
                    price_per_kg,
                    date,
                    ROW_NUMBER() OVER (
                        PARTITION BY market
                        ORDER BY
                            date DESC,
                            price_per_kg DESC
                    ) AS row_num
                FROM market_prices
                WHERE crop IN ({placeholders})
                {location_condition}
            )
            WHERE row_num = 1
            ORDER BY price_per_kg DESC
            LIMIT 10
        """
        query_params = crop_names + location_params

    cursor.execute(
        query,
        query_params
    )

    rows = cursor.fetchall()

    connection.close()

    loc_info = resolve_location(location)
    f_lat, f_lon = loc_info["lat"], loc_info["lon"]
    canonical_origin = f"{loc_info['canonical_name']}, Telangana, India"

    markets = []

    for row in rows:

        mkt_rating = get_market_rating(row["market"])
        dist = get_market_distance(loc_info["canonical_name"], row["market"], row["location"])
        m_lat, m_lon = geocode_location(row["location"] if row["location"] else row["market"])
        route_info = get_road_distance_and_time(f_lat, f_lon, m_lat, m_lon)
        travel_time_str = route_info["travel_time_str"]
        est_cost = round(2 * dist * 4.50, 2)
        encoded_dest = urllib.parse.quote(f"{row['market']}, {row['location']}")
        gmaps_url = f"https://www.google.com/maps/dir/?api=1&origin={urllib.parse.quote(canonical_origin)}&destination={encoded_dest}"

        markets.append({

            "market":
                row["market"],

            "location":
                row["location"],

            "price_per_kg":
                row["price_per_kg"],

            "date":
                row["date"],

            "distance_km":
                dist,

            "travel_time":
                travel_time_str,

            "est_transport_cost":
                est_cost,

            "gmaps_url":
                gmaps_url,

            "google_rating":
                mkt_rating["badge"],

            "rating_val":
                mkt_rating["rating"],

            "timing":
                mkt_rating["timing"]
        })

    return {

        "crop": crop,

        "location": location,

        "markets": markets
    }


# ============================================================
# PRICE PREDICTION
# ============================================================

# ============================================================
# PRICE PREDICTION API
# ============================================================

@app.get("/price-prediction")
def price_prediction(
    crop: str,
    days: int = 3
):

    details = predict_price_details(
        crop,
        days_ahead=days
    )

    if details is None:
        return {
            "crop": crop,
            "error": "Not enough historical data"
        }

    return {
        "crop": crop,
        "days_ahead": days,

        "current_price": details[
            "current_price"
        ],

        "predicted_price": details[
            "predicted_price"
        ],

        "lower_bound": details[
            "lower_bound"
        ],

        "upper_bound": details[
            "upper_bound"
        ],

        "confidence": details[
            "confidence"
        ],

        "mae": details[
            "mae"
        ],

        "r2": details[
            "r2"
        ]
    }

# ============================================================
# PRICE HISTORY
# ============================================================

@app.get("/price-history")
def price_history(
    crop: str,
    location: str = "Hyderabad"
):

    crop_names = CROP_MAPPING.get(
        crop,
        [crop]
    )

    connection = get_connection()
    cursor = connection.cursor()

    placeholders = ",".join(
        ["?"] * len(crop_names)
    )

    farmer_location = location.lower().strip()

    # --------------------------------------------------------
    # LOCATION FILTER
    # --------------------------------------------------------

    if "hyderabad" in farmer_location:

        location_condition = """
            AND (
                LOWER(location) LIKE '%hyderabad%'
                OR LOWER(location) LIKE '%ranga reddy%'
                OR LOWER(location) LIKE '%rangareddy%'
                OR LOWER(location) LIKE '%medchal%'
            )
        """

        location_params = []

    elif "telangana" in farmer_location:

        location_condition = """
            AND LOWER(location) LIKE '%telangana%'
        """

        location_params = []

    else:

        location_condition = """
            AND LOWER(location) LIKE ?
        """

        location_params = [
            f"%{farmer_location}%"
        ]

    # --------------------------------------------------------
    # HISTORY QUERY
    # --------------------------------------------------------

    query = f"""
        SELECT
            date,
            AVG(price_per_kg) AS average_price,
            MIN(price_per_kg) AS minimum_price,
            MAX(price_per_kg) AS maximum_price

        FROM market_prices

        WHERE crop IN ({placeholders})

        {location_condition}

        GROUP BY date

        ORDER BY date ASC
    """

    cursor.execute(
        query,
        crop_names + location_params
    )

    rows = cursor.fetchall()

    if len(rows) < 2:
        fallback_query = f"""
            SELECT
                date,
                AVG(price_per_kg) AS average_price,
                MIN(price_per_kg) AS minimum_price,
                MAX(price_per_kg) AS maximum_price
            FROM market_prices
            WHERE crop IN ({placeholders})
            GROUP BY date
            ORDER BY date ASC
        """
        cursor.execute(fallback_query, crop_names)
        fallback_rows = cursor.fetchall()
        if len(fallback_rows) > len(rows):
            rows = fallback_rows

    connection.close()

    history = []

    for row in rows:

        history.append({

            "date":
                row["date"],

            "average_price":
                round(
                    float(row["average_price"]),
                    2
                ),

            "minimum_price":
                round(
                    float(row["minimum_price"]),
                    2
                ),

            "maximum_price":
                round(
                    float(row["maximum_price"]),
                    2
                )
        })

    return {

        "crop": crop,

        "location": location,

        "history": history
    }


# ============================================================
# AI RECOMMENDATION
# ============================================================

@app.post("/ai-recommendation")
def ai_recommendation(
    request: FarmerRequest
):

    # --------------------------------------------------------
    # RUN LANGGRAPH AGENT
    # --------------------------------------------------------

    result = market_agent.invoke({

        "crop":
            request.crop,

        "location":
            request.location,

        "radius_km":
            request.radius_km,

        "quantity":
            request.quantity,

        "quality":
            request.quality,

        "harvest_date":
            request.harvest_date,

        "price_date":
            request.price_date,

        "market_data":
            [],

        "predicted_price":
            0,

        "best_market":
            "",

        "best_market_location":
            "",

        "best_market_distance":
            0,

        "best_price":
            0,

        "sell_now_score":
            0,

        "wait_score":
            0,

        "decision":
            "",

        "recommendation":
            ""
    })

    # --------------------------------------------------------
    # GET MARKET DISTANCE & RESOLVED LOCATION
    # --------------------------------------------------------

    loc_info = resolve_location(request.location)
    canonical_location = loc_info["canonical_name"]

    best_market_distance = result.get(
        "best_market_distance",
        0
    )

    # --------------------------------------------------------
    # FARMER ADVISOR
    # --------------------------------------------------------

    llm_advice = get_farmer_advice(

        crop=request.crop,

        location=canonical_location,

        quantity=request.quantity,

        quality=request.quality,

        best_market=
            result["best_market"],

        best_market_location=
            result["best_market_location"],

        best_market_distance=
            best_market_distance,

        current_price=
            result["best_price"],

        predicted_price=
            result["predicted_price"],

        decision=
            result["decision"],

        is_small_quantity=
            result.get("is_small_quantity", request.quantity <= 500.0),

        suggested_small_market=
            result.get("suggested_small_market"),

        language=
            request.detected_language or "en"
    )

    # --------------------------------------------------------
    # MARKET INTEL: RATINGS, WEATHER & SPOILAGE RISK
    # --------------------------------------------------------

    best_market_rating = get_market_rating(result["best_market"])
    weather_data = get_weather_conditions(canonical_location, target_date=request.price_date)
    harvest_eval = evaluate_crop_quality_from_harvest_date(request.crop, request.harvest_date, ref_date=request.price_date)
    spoilage_data = get_crop_spoilage_risk(request.crop, request.quality, request.harvest_date, ref_date=request.price_date)
    holding_spoilage = calculate_holding_spoilage_and_loss(
        crop=request.crop,
        quality=request.quality,
        days_since_harvest=harvest_eval["days_elapsed"],
        wait_days=3
    )

    f_lat, f_lon = loc_info["lat"], loc_info["lon"]
    m_lat, m_lon = geocode_location(result["best_market_location"] if result.get("best_market_location") else result["best_market"])
    route_info = get_road_distance_and_time(f_lat, f_lon, m_lat, m_lon)

    # --------------------------------------------------------
    # FINANCIAL BREAKDOWN: SELLING TODAY VS HOLDING 3 DAYS
    # --------------------------------------------------------

    gross_revenue = round(result["best_price"] * request.quantity, 2)
    transport_charges = round(best_market_distance * 2.5, 2)
    handling_charges = round(request.quantity * 0.50, 2)
    total_deductions = round(transport_charges + handling_charges, 2)
    net_in_hand_revenue = round(gross_revenue - total_deductions, 2)

    # Future Holding Economics: Deduct Spoilage Discard & Quality Markdown
    salable_pct = holding_spoilage["salable_pct"] / 100.0
    quality_markdown = holding_spoilage["quality_markdown_pct"] / 100.0
    future_salable_quantity = round(request.quantity * salable_pct, 2)
    spoilage_loss_kg = round(request.quantity - future_salable_quantity, 2)
    future_effective_price = round(result["predicted_price"] * (1.0 - quality_markdown), 2)

    predicted_gross_revenue = round(future_effective_price * future_salable_quantity, 2)
    future_handling = round(future_salable_quantity * 0.50, 2)
    predicted_deductions = round(transport_charges + future_handling, 2)
    predicted_net_in_hand = round(predicted_gross_revenue - predicted_deductions, 2)
    net_difference = round(predicted_net_in_hand - net_in_hand_revenue, 2)

    # --------------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------------

    return {

        "crop":
            request.crop,

        "location":
            request.location,

        "resolved_location":
            canonical_location,

        "is_fuzzy_location":
            loc_info.get("is_fuzzy", False),

        "quantity":
            request.quantity,

        "quality":
            request.quality,

        "harvest_date":
            request.harvest_date,

        "price_date":
            request.price_date,

        "best_market":
            result["best_market"],

        "best_market_location":
            result["best_market_location"],

        "best_market_distance":
            best_market_distance,

        "route_info":
            route_info,

        "best_price":
            result["best_price"],

        "predicted_price":
            result["predicted_price"],

        "has_prediction_model":
            result.get("has_prediction_model", True),

        "sell_now_score":
            result["sell_now_score"],

        "wait_score":
            result["wait_score"],

        "decision":
            result.get("decision", "SELL NOW"),

        "reason":
            result.get("reason", ""),

        "recommendation":
            result.get("recommendation", ""),

        "llm_advice":
            llm_advice,

        "google_rating":
            best_market_rating["badge"],

        "google_rating_val":
            best_market_rating["rating"],

        "market_timing":
            best_market_rating["timing"],

        "weather":
            weather_data,

        "spoilage_risk":
            spoilage_data,

        "harvest_evaluation":
            harvest_eval,

        "holding_spoilage":
            holding_spoilage,

        "is_small_quantity":
            result.get("is_small_quantity", request.quantity <= 500.0),

        "suggested_small_market":
            result.get("suggested_small_market"),

        "small_batch_advisory":
            result.get("small_batch_advisory", ""),

        "financial_breakdown": {
            "gross_revenue": gross_revenue,
            "transport_charges": transport_charges,
            "handling_charges": handling_charges,
            "total_deductions": total_deductions,
            "net_in_hand_revenue": net_in_hand_revenue,
            "predicted_gross_revenue": predicted_gross_revenue,
            "predicted_net_in_hand": predicted_net_in_hand,
            "net_difference": net_difference,
            "future_salable_quantity": future_salable_quantity,
            "spoilage_loss_kg": spoilage_loss_kg,
            "future_effective_price": future_effective_price,
            "spoilage_loss_pct": holding_spoilage["volume_loss_pct"],
            "holding_verdict": holding_spoilage["holding_verdict"],
            "holding_warning": holding_spoilage["holding_warning"]
        }
    }


# ============================================================
# NET PROFIT CALCULATOR
# ============================================================

@app.get("/net-profit")
def net_profit(
    crop: str,
    location: str = "Hyderabad",
    quantity: float = 100.0,
    radius_km: float = 50.0,
    date: str = None
):

    # --------------------------------------------------------
    # GET MARKET COMPARISON
    # --------------------------------------------------------

    comparison = market_comparison(
        crop=crop,
        location=location,
        date=date,
        radius_km=radius_km
    )

    markets = comparison.get(
        "markets",
        []
    )

    # --------------------------------------------------------
    # NO DATA
    # --------------------------------------------------------

    if not markets:

        return {

            "crop": crop,

            "location": location,

            "quantity": quantity,

            "markets": [],

            "best_market": None,

            "best_net_profit": 0
        }

    results = []

    # ========================================================
    # COST ASSUMPTIONS
    # ========================================================

    transport_rate_per_km = 2.5

    handling_cost_per_kg = 0.50

    # ========================================================
    # CALCULATE PROFIT WITH SCALE-AWARE ECONOMICS
    # ========================================================

    for market in markets:

        market_name = market["market"]

        price = float(
            market["price_per_kg"]
        )

        distance = market.get("distance_km")
        if distance is None:
            distance = get_market_distance(location, market_name)

        is_rbz = (
            market.get("is_small_market", False) or
            "rythu" in market_name.lower() or
            "rbz" in market_name.lower() or
            "sub-market" in str(market.get("type", "")).lower()
        )

        gross_revenue = price * quantity

        # Unit economics: Small batch (<= 500 kg) vs Bulk commercial (> 500 kg)
        if quantity <= 500.0:
            if distance <= 10.0:
                transport_cost = max(30.0, 20.0 + distance * 3.0)
            else:
                transport_cost = 100.0 + (distance - 10.0) * 8.0
            commission_cost = 0.0 if is_rbz else round(gross_revenue * 0.04, 2)
            handling_cost = 0.0 if is_rbz else round(quantity * 0.50, 2)
        else:
            transport_cost = round(2.0 * distance * 4.50 * (1.0 + quantity / 2000.0), 2)
            commission_cost = round(gross_revenue * 0.04, 2)
            handling_cost = round(quantity * 0.50, 2)

        total_cost = transport_cost + handling_cost + commission_cost
        net_profit_value = gross_revenue - total_cost

        results.append({

            "market":
                market_name,

            "location":
                market["location"],

            "price_per_kg":
                round(
                    price,
                    2
                ),

            "distance_km":
                distance,

            "gross_revenue":
                round(
                    gross_revenue,
                    2
                ),

            "transport_cost":
                round(
                    transport_cost,
                    2
                ),

            "handling_cost":
                round(
                    handling_cost,
                    2
                ),

            "commission_cost":
                round(
                    commission_cost,
                    2
                ),

            "total_cost":
                round(
                    total_cost,
                    2
                ),

            "net_profit":
                round(
                    net_profit_value,
                    2
                ),

            "is_small_market":
                is_rbz,

            "market_category":
                "Rythu Bazar / Local Market" if is_rbz else "Wholesale APMC Mandi",

            "google_rating":
                get_market_rating(market_name)["badge"]
        })

    # ========================================================
    # SORT BY NET PROFIT
    # ========================================================

    results.sort(
        key=lambda x: x["net_profit"],
        reverse=True
    )

    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return {

        "crop":
            crop,

        "location":
            location,

        "quantity":
            quantity,

        "markets":
            results,

        "best_market":
            results[0]["market"],

        "best_net_profit":
            results[0]["net_profit"]
    }


# ============================================================
# VOICE INTELLIGENCE ENDPOINTS (TELUGU / HINDI / ENGLISH)
# ============================================================

class VoiceParseRequest(BaseModel):
    text: Optional[str] = None
    audio_base64: Optional[str] = None
    language: Optional[str] = "te"


class VoiceTTSRequest(BaseModel):
    script_text: Optional[str] = None
    recommendation_data: Optional[dict] = None
    language: Optional[str] = "te"


@app.post("/voice-parse")
def voice_parse(req: VoiceParseRequest):
    """
    Parses spoken voice command into crop, quantity, and location.
    Accepts raw text or base64 audio.
    """
    raw_text = req.text or ""

    # If audio is provided, transcribe with Whisper
    if req.audio_base64:
        try:
            audio_bytes = base64.b64decode(req.audio_base64)
            raw_text = transcribe_audio_bytes(audio_bytes, filename="voice.wav")
        except Exception as e:
            return {
                "status": "error",
                "message": f"Whisper transcription failed: {str(e)}",
                "crop": None,
                "quantity": None,
                "location": None
            }

    if not raw_text.strip():
        return {
            "status": "error",
            "message": "No voice text or audio provided",
            "crop": None,
            "quantity": None,
            "location": None
        }

    parsed = extract_parameters_with_llm_fallback(raw_text, default_lang=req.language or "te")
    return {
        "status": "success",
        "raw_text": raw_text,
        "crop": parsed.get("crop"),
        "quantity": parsed.get("quantity"),
        "location": parsed.get("location"),
        "language": parsed.get("language", req.language)
    }


@app.post("/voice-tts")
def voice_tts(req: VoiceTTSRequest):
    """
    Generates spoken audio in farmer's mother tongue (Telugu, Hindi, or English).
    Returns base64 MP3 audio data URI.
    """
    lang = req.language or "te"
    script_text = req.script_text

    if not script_text and req.recommendation_data:
        script_text = generate_farmer_voice_script(req.recommendation_data, lang=lang)

    if not script_text:
        return {
            "status": "error",
            "message": "Neither script_text nor recommendation_data provided"
        }

    try:
        audio_b64 = generate_speech_audio_base64(script_text, lang=lang)
        return {
            "status": "success",
            "language": lang,
            "script_text": script_text,
            "audio_base64": audio_b64
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"TTS synthesis failed: {str(e)}"
        }