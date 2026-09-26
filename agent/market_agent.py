from typing import TypedDict

from langgraph.graph import StateGraph, END

from backend.database import get_connection
from ml.price_model import predict_price
from services.geo_market_service import (
    get_market_distance,
    discover_markets_in_radius,
    resolve_location,
    find_best_small_market
)


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
# MARKET DISTANCE MAP
# Demo distances from farmer location
# ============================================================

DISTANCE_MAP = {
    "Bowenpally": 15,
    "Gudimalkapur": 12,
    "RYTHU BAZAR FALAKNUMA": 20,
    "RYTHU BAZAR ERRAGADDA": 10,
    "Kukatpally,RBZ": 18,
    "Saroornagar,RBZ": 16,
    "Vanasthalipuram,RBZ": 22,
    "Siddipet(Rythu Bazar)": 100,
    "Excise Colony,RBZ": 70,
    "Miryalguda(Rythu Bazar)": 150
}


# ============================================================
# LANGGRAPH STATE
# ============================================================

class MarketState(TypedDict, total=False):

    crop: str
    location: str
    resolved_location: str
    radius_km: float
    quantity: float
    quality: str
    harvest_date: str
    price_date: str

    market_data: list

    predicted_price: float
    has_prediction_model: bool

    best_market: str
    best_market_location: str
    best_market_distance: float
    best_price: float

    is_small_quantity: bool
    suggested_small_market: dict
    small_batch_advisory: str

    sell_now_score: int
    wait_score: int

    decision: str
    reason: str
    recommendation: str


# ============================================================
# NODE 1
# GET LOCATION-AWARE MARKET DATA
# ============================================================

def get_market_data(state: MarketState):

    crop = state["crop"]
    location = state["location"]
    radius_km = float(state.get("radius_km") or 50.0)

    crop_names = CROP_MAPPING.get(
        crop,
        [crop]
    )

    # Canonicalize and resolve location to handle typos (e.g. 'janagoan' -> 'Jangaon')
    loc_info = resolve_location(location)
    canonical_name = loc_info["canonical_name"]
    farmer_location = canonical_name.lower().strip()

    connection = get_connection()
    cursor = connection.cursor()

    placeholders = ",".join(
        ["?"] * len(crop_names)
    )

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

    elif "telangana" in farmer_location:

        location_condition = """
            AND LOWER(location) LIKE '%telangana%'
        """

    else:

        location_condition = """
            AND (
                LOWER(location) LIKE ?
                OR LOWER(location) LIKE '%telangana%'
            )
        """

    # --------------------------------------------------------
    # GET LATEST RECORD FOR EACH MARKET
    # --------------------------------------------------------

    if (
        "hyderabad" in farmer_location
        or "telangana" in farmer_location
    ):
        location_params = []
    else:
        location_params = [f"%{farmer_location}%"]

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
    """

    cursor.execute(
        query,
        crop_names + location_params
    )

    rows = cursor.fetchall()

    connection.close()

    # --------------------------------------------------------
    # CONVERT DATABASE ROWS
    # --------------------------------------------------------

    market_data = []

    for row in rows:

        market_data.append({

            "market": row["market"],

            "location": row["location"],

            "price_per_kg": float(
                row["price_per_kg"]
            ),

            "date": row["date"]
        })

    # Always include radius discovered physical markets so local mandis are always present
    discovered = discover_markets_in_radius(crop, canonical_name, radius_km=radius_km)
    existing_mkts = {m["market"].lower().strip() for m in market_data}
    for d in discovered:
        if d["market"].lower().strip() not in existing_mkts:
            market_data.append({
                "market": d["market"],
                "location": d["location"],
                "price_per_kg": float(d["price_per_kg"]),
                "date": d["date"],
                "distance_km": float(d["distance_km"])
            })
            existing_mkts.add(d["market"].lower().strip())

    return {
        "market_data": market_data,
        "resolved_location": canonical_name
    }


# ============================================================
# NODE 2
# FIND BEST MARKET + DISTANCE
# ============================================================

def find_best_market(state: MarketState):

    market_data = state["market_data"]
    farmer_loc = state.get("resolved_location") or state.get("location", "Hyderabad")
    radius_km = float(state.get("radius_km") or 50.0)
    crop = state.get("crop", "Tomato")
    quantity = float(state.get("quantity") or 100.0)
    is_small_quantity = quantity <= 500.0

    # Discover / evaluate closest dedicated Small Market / Rythu Bazar
    suggested_small = find_best_small_market(
        crop=crop,
        farmer_location=farmer_loc,
        radius_km=radius_km,
        quantity=quantity,
        target_date=state.get("price_date")
    )

    # --------------------------------------------------------
    # NO MARKET FOUND
    # --------------------------------------------------------

    if not market_data:

        return {

            "best_market": "No market found",

            "best_market_location": "N/A",

            "best_market_distance": 0,

            "best_price": 0,

            "is_small_quantity": is_small_quantity,

            "suggested_small_market": suggested_small,

            "small_batch_advisory": ""
        }

    # --------------------------------------------------------
    # COMPUTE EXACT ROAD DISTANCE & UNIT ECONOMICS
    # --------------------------------------------------------

    for m in market_data:
        if "distance_km" not in m:
            m["distance_km"] = get_market_distance(farmer_loc, m["market"], m.get("location"))

        dist = float(m.get("distance_km", 0.0))
        price = float(m.get("price_per_kg", 0.0))
        is_rbz = (
            m.get("is_small_market", False) or
            "rythu" in m.get("market", "").lower() or
            "rbz" in m.get("market", "").lower() or
            "sub-market" in str(m.get("type", "")).lower()
        )

        if is_small_quantity:
            # Small load (<= 500 kg):
            # Short distance (<= 10 km) is reachable by two-wheeler / auto without commercial truck hire
            if dist <= 10.0:
                transit = round(max(30.0, 20.0 + dist * 3.0), 2)
            else:
                transit = round(100.0 + (dist - 10.0) * 8.0, 2)
            comm = 0.0 if is_rbz else round(price * quantity * 0.04, 2)
            handling = 0.0 if is_rbz else round(quantity * 0.50, 2)
        else:
            # Bulk commercial load (> 500 kg): requires pickup truck or tractor
            transit = round(2 * dist * 4.50 * (1.0 + quantity / 2000.0), 2)
            comm = round(price * quantity * 0.04, 2)
            handling = round(quantity * 0.50, 2)

        gross = round(price * quantity, 2)
        net_ret = round(gross - transit - comm - handling, 2)
        m["net_in_hand_est"] = net_ret
        m["transit_est"] = transit
        m["is_small_market"] = is_rbz

    # Prioritize markets strictly within farmer's chosen radius
    in_radius = [m for m in market_data if m.get("distance_km", 999.0) <= radius_km + 3.0]
    candidate_pool = in_radius if in_radius else market_data

    # Selection strategy:
    if is_small_quantity:
        # For small quantities, maximize net in-hand return so high travel costs don't wipe out profit.
        # Break ties on closest distance.
        best_market = max(
            candidate_pool,
            key=lambda x: (
                x.get("net_in_hand_est", 0.0),
                -x.get("distance_km", 50.0)
            )
        )
    else:
        # For bulk commercial lots (> 500 kg), wholesale APMC mandis are equipped for large auctions.
        # Prefer wholesale APMC mandis over retail Rythu Bazars if available in candidate pool.
        wholesale_candidates = [m for m in candidate_pool if not m.get("is_small_market", False)]
        bulk_pool = wholesale_candidates if wholesale_candidates else candidate_pool
        best_market = max(
            bulk_pool,
            key=lambda x: (
                x["price_per_kg"],
                -x.get("distance_km", 50.0)
            )
        )

    market_name = best_market["market"]
    distance = best_market.get("distance_km", 0.0)

    # Build small batch advisory
    advisory = ""
    if is_small_quantity:
        if suggested_small and suggested_small.get("market") != market_name:
            sm_name = suggested_small.get("market")
            sm_dist = suggested_small.get("distance_km", 0.0)
            sm_net = suggested_small.get("small_batch_net_profit", 0.0)
            advisory = (
                f"Small Batch Notice ({quantity:g} kg): You can also sell directly at your local {sm_name} "
                f"just {sm_dist:.1f} km away (0% commission, bike/auto accessible) with ~₹{sm_net:,.0f} net in hand, "
                f"avoiding long travel."
            )
        else:
            advisory = (
                f"Small Batch Notice ({quantity:g} kg): {market_name} is close (~{distance:.1f} km) "
                f"and minimizes your transport overhead, maximizing your take-home cash."
            )

    return {

        "best_market": market_name,

        "best_market_location":
            best_market["location"],

        "best_market_distance":
            float(distance),

        "best_price":
            best_market["price_per_kg"],

        "is_small_quantity":
            is_small_quantity,

        "suggested_small_market":
            suggested_small,

        "small_batch_advisory":
            advisory
    }



# ============================================================
# NODE 3
# PREDICT FUTURE PRICE
# ============================================================

def predict_future_price(state: MarketState):

    crop = state["crop"]

    prediction = predict_price(
        crop,
        days_ahead=3
    )

    has_prediction_model = (prediction is not None)

    # --------------------------------------------------------
    # FALLBACK TO SPOT PRICE WHEN TIME-SERIES DATA IS LIMITED
    # --------------------------------------------------------

    if prediction is None:

        prediction = state["best_price"]

    return {

        "predicted_price":
            round(float(prediction), 2),

        "has_prediction_model":
            has_prediction_model
    }


# ============================================================
# NODE 4
# CALCULATE SELL / WAIT SCORES
# ============================================================

def calculate_scores(state: MarketState):

    current_price = state["best_price"]

    predicted_price = state["predicted_price"]

    # --------------------------------------------------------
    # NO PRICE DATA
    # --------------------------------------------------------

    if current_price <= 0:

        return {

            "sell_now_score": 50,

            "wait_score": 50
        }

    # --------------------------------------------------------
    # PRICE CHANGE
    # --------------------------------------------------------

    price_change_percent = (

        (predicted_price - current_price)

        / current_price

    ) * 100

    # --------------------------------------------------------
    # BASE WAIT SCORE
    # --------------------------------------------------------

    wait_score = 50

    if price_change_percent >= 5:

        wait_score = 80

    elif price_change_percent >= 2:

        wait_score = 70

    elif price_change_percent > 0:

        wait_score = 60

    elif price_change_percent <= -5:

        wait_score = 20

    elif price_change_percent <= -2:

        wait_score = 30

    elif price_change_percent < 0:

        wait_score = 40

    # --------------------------------------------------------
    # QUALITY ADJUSTMENT
    # --------------------------------------------------------

    quality = state["quality"]

    if quality == "Grade A":

        wait_score += 5

    elif quality == "Grade C":

        wait_score -= 5

    # --------------------------------------------------------
    # CROP PERISHABILITY & WEATHER RISK ADJUSTMENT
    # --------------------------------------------------------

    from services.market_intel import (
        get_crop_spoilage_risk,
        get_weather_conditions,
        evaluate_crop_quality_from_harvest_date,
        calculate_holding_spoilage_and_loss
    )

    h_eval = evaluate_crop_quality_from_harvest_date(
        state["crop"],
        state.get("harvest_date"),
        state.get("price_date")
    )
    crop_risk = get_crop_spoilage_risk(
        state["crop"],
        state.get("quality", "Grade A"),
        state.get("harvest_date"),
        state.get("price_date")
    )
    weather = get_weather_conditions(state["location"])
    holding_spoilage = calculate_holding_spoilage_and_loss(
        crop=state["crop"],
        quality=state.get("quality", "Grade A"),
        days_since_harvest=h_eval["days_elapsed"],
        wait_days=3
    )

    # Harvest age adjustment: older harvests lose moisture and degrade rapidly
    if h_eval.get("quality") == "Grade C":
        wait_score -= 25
    elif h_eval.get("quality") == "Grade B" and crop_risk["perishability"] in ["Very High", "High"]:
        wait_score -= 15

    # High perishability crops suffer rot and weight loss if held
    if crop_risk["perishability"] == "Very High":
        wait_score -= 20
    elif crop_risk["perishability"] == "High":
        wait_score -= 10
    elif "Grain" in crop_risk["perishability"]:
        wait_score += 5

    # Weather impact: rain/humidity accelerates perishable rotting
    if weather["rain_prob_val"] >= 20 and crop_risk["perishability"] in ["Very High", "High"]:
        wait_score -= 10

    # HARD SHELF-LIFE CLAMP: If crop is past safe shelf-life or decaying severely,
    # waiting is physically impossible regardless of mandi prices!
    shelf_limit = h_eval.get("shelf_life_limit", 4)
    if h_eval.get("is_past_shelf_life") or (crop_risk["perishability"] in ["Very High", "High"] and (h_eval["days_elapsed"] >= shelf_limit or state.get("quality") == "Grade C")):
        wait_score = min(wait_score, 3)
    elif holding_spoilage["is_severe_spoilage"]:
        wait_score = min(wait_score, 10)

    # Spoilage financial factor: If volume loss + markdown outweighs price rise
    if price_change_percent > 0 and holding_spoilage["volume_loss_pct"] > 0:
        holding_factor = (
            (1.0 - holding_spoilage["volume_loss_pct"] / 100.0) *
            (1.0 - holding_spoilage["quality_markdown_pct"] / 100.0) *
            (1.0 + price_change_percent / 100.0)
        )
        if holding_factor < 0.98:
            wait_score = min(wait_score, 25)

    # --------------------------------------------------------
    # KEEP SCORE BETWEEN 0 AND 100
    # --------------------------------------------------------

    wait_score = max(
        0,
        min(100, wait_score)
    )

    sell_score = 100 - wait_score

    return {

        "sell_now_score":
            int(sell_score),

        "wait_score":
            int(wait_score)
    }


# ============================================================
# NODE 5
# MAKE DECISION
# ============================================================

def make_decision(state):
    current_price = state["best_price"]
    predicted_price = state["predicted_price"]

    if current_price <= 0:
        return {
            "decision": "NO DATA",
            "reason": "Current market price is unavailable."
        }

    price_change_percent = (
        (predicted_price - current_price)
        / current_price
    ) * 100

    from services.market_intel import (
        get_crop_spoilage_risk,
        evaluate_crop_quality_from_harvest_date,
        calculate_holding_spoilage_and_loss
    )

    h_eval = evaluate_crop_quality_from_harvest_date(
        state["crop"],
        state.get("harvest_date"),
        state.get("price_date")
    )
    crop_risk = get_crop_spoilage_risk(
        state["crop"],
        state.get("quality", "Grade A"),
        state.get("harvest_date"),
        state.get("price_date")
    )
    holding_spoilage = calculate_holding_spoilage_and_loss(
        crop=state["crop"],
        quality=state.get("quality", "Grade A"),
        days_since_harvest=h_eval["days_elapsed"],
        wait_days=3
    )

    # 1. HARD OVERRIDE: Past safe shelf-life or Grade C for perishable crops
    shelf_limit = h_eval.get("shelf_life_limit", 4)
    if h_eval.get("is_past_shelf_life") or (crop_risk["perishability"] in ["Very High", "High"] and (h_eval["days_elapsed"] >= shelf_limit or state.get("quality") == "Grade C")):
        return {
            "decision": "SELL NOW",
            "reason": (
                f"🚨 CRITICAL SPOILAGE OVERRIDE: Harvested {h_eval['days_elapsed']} days ago "
                f"(safe shelf life: {shelf_limit} days). "
                f"Holding for 3 more days causes ~{holding_spoilage['volume_loss_pct']:.0f}% rot and heavy discard. "
                f"Even with an expected mandi rate rise, loss of salable produce results in a severe financial deficit. "
                f"Sell immediately!"
            )
        }

    # 2. CHECK SPOILAGE-ADJUSTED HOLDING FACTOR
    # Even if nominal price rises, check if rot volume loss + markdown results in net financial loss
    if price_change_percent > 0 and holding_spoilage["volume_loss_pct"] > 0:
        holding_factor = (
            (1.0 - holding_spoilage["volume_loss_pct"] / 100.0) *
            (1.0 - holding_spoilage["quality_markdown_pct"] / 100.0) *
            (1.0 + price_change_percent / 100.0)
        )
        if holding_factor < 0.98:
            return {
                "decision": "SELL NOW",
                "reason": (
                    f"Physical spoilage ({holding_spoilage['volume_loss_pct']:.0f}% loss) and quality markdown "
                    f"outweigh the expected {price_change_percent:.1f}% price rise. "
                    f"Holding causes net financial loss. Sell now to protect capital."
                )
            }

    # 3. SCORE-ALIGNED DECISION: Directly synchronized with calculate_scores
    wait_score = state.get("wait_score", 50)
    sell_now_score = state.get("sell_now_score", 50)

    if wait_score > sell_now_score:
        decision = "WAIT"
        reason = (
            f"Price is predicted to increase by approximately "
            f"{price_change_percent:.1f}% (+₹{predicted_price - current_price:.2f}/kg). "
            f"{state['crop']} has favorable storage durability. Waiting is expected to provide higher net returns."
        )

    elif sell_now_score > wait_score:
        decision = "SELL NOW"
        if price_change_percent < 0:
            reason = (
                f"Price is predicted to decrease by approximately "
                f"{abs(price_change_percent):.1f}% (-₹{abs(predicted_price - current_price):.2f}/kg). "
                f"Selling now protects against price decline."
            )
        else:
            reason = (
                f"Holding risks, perishability factors, and immediate cash realization make selling now the recommended choice."
            )

    else:
        decision = "NEUTRAL"
        reason = (
            f"Expected price change is minimal. "
            f"Consider selling based on immediate cash requirements, storage availability, and local mandi conditions."
        )

    return {
        "decision": decision,
        "reason": reason
    }


# ============================================================
# NODE 6
# GENERATE RECOMMENDATION
# ============================================================

def generate_recommendation(state: MarketState):

    crop = state["crop"]

    quantity = state["quantity"]

    best_market = state["best_market"]

    best_location = state["best_market_location"]

    best_distance = state["best_market_distance"]

    best_price = state["best_price"]

    predicted_price = state["predicted_price"]

    decision = state["decision"]

    price_difference = (
        predicted_price - best_price
    )
    price_change_percent = (
        (price_difference / best_price * 100)
        if best_price > 0 else 0
    )

    # ========================================================
    # SELL NOW
    # ========================================================

    if decision == "SELL NOW":

        if price_difference < 0:
            trend_text = f"The model expects the price to decrease by ₹{abs(price_difference):.2f}/kg ({abs(price_change_percent):.1f}%). "
        elif price_difference > 0:
            trend_text = f"Although a slight price change of ₹{price_difference:.2f}/kg is possible, holding risks and immediate cash realization make selling now the safer choice. "
        else:
            trend_text = "The model expects prices to remain steady. "

        recommendation = (

            f"For {quantity:g} kg of {crop}, "

            f"the recommended market is "
            f"{best_market}, "

            f"located in {best_location}, "

            f"approximately {best_distance:.1f} km away, "

            f"with a current price of "
            f"₹{best_price:.2f}/kg. "

            f"The predicted price after 3 days is "
            f"₹{predicted_price:.2f}/kg. "

            f"{trend_text}"

            f"Therefore, selling now may help "
            f"maximize current returns."
        )

    # ========================================================
    # WAIT
    # ========================================================

    elif decision == "WAIT":

        if price_difference > 0:
            trend_text = f"The model expects the price to increase by ₹{price_difference:.2f}/kg ({price_change_percent:+.1f}%). "
        else:
            trend_text = "The model expects favorable market conditions over the next 3 days. "

        recommendation = (

            f"For {quantity:g} kg of {crop}, "

            f"the recommended market is "
            f"{best_market}, "

            f"located in {best_location}, "

            f"approximately {best_distance:.1f} km away, "

            f"with a current price of "
            f"₹{best_price:.2f}/kg. "

            f"The predicted price after 3 days is "
            f"₹{predicted_price:.2f}/kg. "

            f"{trend_text}"

            f"Therefore, waiting may provide "
            f"a better selling price."
        )

    # ========================================================
    # NEUTRAL
    # ========================================================

    else:

        recommendation = (

            f"For {quantity:g} kg of {crop}, "

            f"the recommended market is "
            f"{best_market}, "

            f"located in {best_location}, "

            f"approximately {best_distance:.1f} km away, "

            f"with a current price of "
            f"₹{best_price:.2f}/kg. "

            f"The predicted price after 3 days is "
            f"₹{predicted_price:.2f}/kg. "

            f"The expected price change is small. "

            f"Consider selling based on storage "
            f"costs, urgency and local market "
            f"conditions."
        )

    if state.get("is_small_quantity") and state.get("small_batch_advisory"):
        recommendation += f"\n\n🛵 {state['small_batch_advisory']}"

    return {

        "recommendation":
            recommendation
    }


# ============================================================
# BUILD LANGGRAPH
# ============================================================

graph = StateGraph(MarketState)


# ============================================================
# ADD NODES
# ============================================================

graph.add_node(
    "get_market_data",
    get_market_data
)

graph.add_node(
    "find_best_market",
    find_best_market
)

graph.add_node(
    "predict_future_price",
    predict_future_price
)

graph.add_node(
    "calculate_scores",
    calculate_scores
)

graph.add_node(
    "make_decision",
    make_decision
)

graph.add_node(
    "generate_recommendation",
    generate_recommendation
)


# ============================================================
# LANGGRAPH FLOW
# ============================================================

graph.set_entry_point(
    "get_market_data"
)

graph.add_edge(
    "get_market_data",
    "find_best_market"
)

graph.add_edge(
    "find_best_market",
    "predict_future_price"
)

graph.add_edge(
    "predict_future_price",
    "calculate_scores"
)

graph.add_edge(
    "calculate_scores",
    "make_decision"
)

graph.add_edge(
    "make_decision",
    "generate_recommendation"
)

graph.add_edge(
    "generate_recommendation",
    END
)


# ============================================================
# COMPILE AGENT
# ============================================================

market_agent = graph.compile()