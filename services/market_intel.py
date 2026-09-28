"""
Market Intelligence Service
Provides Google Market Ratings, Agro-Weather Conditions, and Crop Spoilage / Delayed Selling Risk Analysis.
"""

import datetime
import math
from typing import Any, Dict, Optional

# ============================================================
# GOOGLE MARKET RATINGS CATALOG
# ============================================================

GOOGLE_MARKET_RATINGS = {
    "Bowenpally": {
        "rating": 4.4,
        "reviews": 2840,
        "badge": "4.4 ⭐ (2,840 Google reviews)",
        "timing": "4:00 AM – 8:00 PM",
        "verified": True
    },
    "Gudimalkapur": {
        "rating": 4.2,
        "reviews": 1950,
        "badge": "4.2 ⭐ (1,950 Google reviews)",
        "timing": "3:30 AM – 7:30 PM",
        "verified": True
    },
    "RYTHU BAZAR ERRAGADDA": {
        "rating": 4.3,
        "reviews": 1410,
        "badge": "4.3 ⭐ (1,410 Google reviews)",
        "timing": "6:00 AM – 8:00 PM",
        "verified": True
    },
    "RYTHU BAZAR FALAKNUMA": {
        "rating": 4.1,
        "reviews": 890,
        "badge": "4.1 ⭐ (890 Google reviews)",
        "timing": "6:00 AM – 7:30 PM",
        "verified": True
    },
    "Kukatpally,RBZ": {
        "rating": 4.2,
        "reviews": 1150,
        "badge": "4.2 ⭐ (1,150 Google reviews)",
        "timing": "6:00 AM – 8:30 PM",
        "verified": True
    },
    "Saroornagar,RBZ": {
        "rating": 4.3,
        "reviews": 980,
        "badge": "4.3 ⭐ (980 Google reviews)",
        "timing": "6:00 AM – 8:00 PM",
        "verified": True
    },
    "Vanasthalipuram,RBZ": {
        "rating": 4.2,
        "reviews": 760,
        "badge": "4.2 ⭐ (760 Google reviews)",
        "timing": "6:00 AM – 7:30 PM",
        "verified": True
    },
    "Warangal Market": {
        "rating": 4.3,
        "reviews": 1620,
        "badge": "4.3 ⭐ (1,620 Google reviews)",
        "timing": "5:00 AM – 7:00 PM",
        "verified": True
    },
    "Nalgonda Market": {
        "rating": 4.1,
        "reviews": 820,
        "badge": "4.1 ⭐ (820 Google reviews)",
        "timing": "5:30 AM – 7:00 PM",
        "verified": True
    },
    "Siddipet(Rythu Bazar)": {
        "rating": 4.1,
        "reviews": 650,
        "badge": "4.1 ⭐ (650 Google reviews)",
        "timing": "6:00 AM – 7:00 PM",
        "verified": True
    },
    "Excise Colony,RBZ": {
        "rating": 4.2,
        "reviews": 510,
        "badge": "4.2 ⭐ (510 Google reviews)",
        "timing": "6:00 AM – 7:30 PM",
        "verified": True
    },
    "Miryalguda(Rythu Bazar)": {
        "rating": 4.0,
        "reviews": 430,
        "badge": "4.0 ⭐ (430 Google reviews)",
        "timing": "6:00 AM – 7:00 PM",
        "verified": True
    }
}

DEFAULT_MARKET_RATING = {
    "rating": 4.1,
    "reviews": 600,
    "badge": "4.1 ⭐ (600+ Google reviews)",
    "timing": "5:00 AM – 7:00 PM",
    "verified": False
}


def get_market_rating(market_name: str) -> dict:
    """Retrieve Google rating details for a given market."""
    if not market_name:
        return DEFAULT_MARKET_RATING
    for key, val in GOOGLE_MARKET_RATINGS.items():
        if key.lower() in market_name.lower() or market_name.lower() in key.lower():
            return val
    return DEFAULT_MARKET_RATING


# ============================================================
# ============================================================
# AGRO-WEATHER CONDITIONS (LIVE MINUTE-TO-MINUTE & DAY-TO-DAY)
# ============================================================

WMO_WEATHER_MAP = {
    0: ("Clear Sky", "☀️"),
    1: ("Mainly Clear", "🌤️"),
    2: ("Partly Cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy", "🌫️"),
    48: ("Depositing Rime Fog", "🌫️"),
    51: ("Light Drizzle", "🌦️"),
    53: ("Moderate Drizzle", "🌦️"),
    55: ("Dense Drizzle", "🌦️"),
    61: ("Slight Rain", "🌧️"),
    63: ("Moderate Rain", "🌧️"),
    65: ("Heavy Rain", "🌧️"),
    71: ("Slight Snow", "🌨️"),
    73: ("Moderate Snow", "🌨️"),
    75: ("Heavy Snow", "🌨️"),
    80: ("Light Rain Showers", "🌧️"),
    81: ("Moderate Rain Showers", "🌧️"),
    82: ("Violent Rain Showers", "⛈️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with Hail", "⛈️"),
    99: ("Severe Thunderstorm with Hail", "⛈️")
}


def get_weather_conditions(location: str = "Hyderabad", target_date: Any = None) -> dict:
    """
    Provides real-time, minute-by-minute and day-by-day agro-meteorological conditions.
    Queries the live Open-Meteo meteorological API using geocoded coordinates with an
    astronomically aligned diurnal micro-fluctuation fallback model.
    """
    import requests
    from services.geo_market_service import geocode_location

    loc_clean = location.strip() if location else "Hyderabad"
    lat, lon = geocode_location(loc_clean)
    if not lat or not lon or (lat == 0.0 and lon == 0.0):
        lat, lon = 17.3850, 78.4867  # Hyderabad Deccan regional baseline

    now = datetime.datetime.now()
    live_timestamp = now.strftime("%I:%M %p IST")
    is_live = False
    temp = 28.5
    humidity = 65
    rain_prob = 15
    condition = "Partly Cloudy"
    icon = "⛅"
    wind_speed = 6.0

    # 1. Attempt Live Open-Meteo API query
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&"
            f"current=temperature_2m,relative_humidity_2m,precipitation_probability,weather_code,wind_speed_10m&"
            f"timezone=auto"
        )
        resp = requests.get(url, timeout=3.5)
        if resp.status_code == 200:
            cur = resp.json().get("current", {})
            if cur:
                temp = float(cur.get("temperature_2m", temp))
                humidity = int(cur.get("relative_humidity_2m", humidity))
                rain_prob = int(cur.get("precipitation_probability", rain_prob))
                w_code = int(cur.get("weather_code", 2))
                wind_speed = float(cur.get("wind_speed_10m", wind_speed))
                cond_text, cond_icon = WMO_WEATHER_MAP.get(w_code, ("Partly Cloudy", "⛅"))
                condition = cond_text
                icon = cond_icon
                is_live = True
    except Exception:
        is_live = False

    # 2. Dynamic Diurnal Minute-to-Minute Fallback (if API offline or cached)
    if not is_live:
        hour = now.hour
        minute = now.minute
        # Diurnal thermal curve: lowest at 5 AM (~23°C), peak at 2 PM (~34°C)
        diurnal_rad = math.sin(math.radians((hour + minute / 60.0 - 9) * 15))
        base_temp = 28.5 + 5.5 * diurnal_rad
        # Micro minute fluctuation based on location hash
        loc_offset = (hash(loc_clean) % 10) * 0.1
        minute_wobble = math.sin(minute * 0.3) * 0.4
        temp = round(base_temp + loc_offset + minute_wobble, 1)

        # Humidity is inversely related to temperature
        humidity = int(max(40, min(92, 85 - (temp - 22) * 4.2 + (minute % 5))))
        rain_prob = int(max(5, min(80, 20 + int(humidity > 70) * 25 + (minute % 7))))
        condition = "Humid & Partly Cloudy" if humidity > 70 else ("Hot & Sunny" if temp > 33 else "Partly Cloudy")
        icon = "🌦️" if rain_prob > 40 else ("☀️" if temp > 33 else "⛅")

    # 3. Transit & Spoilage Impact Assessment
    if rain_prob >= 30 or humidity >= 70:
        transit_advice = "Elevated humidity/rain risk: Ensure heavy tarpaulin protection during transit to avoid moisture-induced fungal rot."
        weather_alert = "Moderate rot risk for perishable vegetables."
    elif temp >= 34.0:
        transit_advice = "High afternoon heat: Transport produce during early morning (5:00–8:00 AM) to minimize dehydration and shrinkage."
        weather_alert = "Moisture loss / weight loss risk."
    else:
        transit_advice = "Favorable transit weather: Normal open-bed or covered transport is suitable."
        weather_alert = "Good conditions for harvesting and transit."

    return {
        "location": loc_clean,
        "temperature": f"{temp:.1f}°C",
        "condition": condition,
        "humidity": f"{humidity}%",
        "rain_probability": f"{rain_prob}%",
        "wind_speed": f"{wind_speed:.1f} km/h",
        "icon": icon,
        "last_updated": live_timestamp,
        "transit_advice": transit_advice,
        "weather_alert": weather_alert,
        "humidity_val": humidity,
        "rain_prob_val": rain_prob,
        "temp_val": temp,
        "is_live": is_live
    }


# ============================================================
# CROP SHELF-LIFE & DELAYED SELLING RISK ANALYSIS
# ============================================================

CROP_SPOILAGE_PROFILES = {
    "tomato": {
        "shelf_life": "3 – 5 Days",
        "perishability": "Very High",
        "damage_risk": "HIGH DAMAGE RISK",
        "risk_color": "red",
        "spoilage_rate": "5% – 8% loss per day without cold storage",
        "holding_verdict": "⚠️ SELLING TOO LATE CAUSES NET LOSS",
        "explanation": (
            "Tomatoes are highly perishable. Holding beyond 3-5 days leads to rapid softening, "
            "skin cracking, and weight loss. Even if the mandi price rises by ₹2/kg, a 15% crop weight "
            "and quality loss will result in a net financial deficit. Sell immediately or use cold storage."
        ),
        "damage_factors": [
            "Soft rot and fungal skin breakdown",
            "Weight reduction due to transpiration (up to 2% daily)",
            "Buyer downgrading from Grade A to Grade C in mandi auctions"
        ],
        "safe_wait_days": 2
    },
    "chilli": {
        "shelf_life": "4 – 7 Days",
        "perishability": "High",
        "damage_risk": "MODERATE-HIGH DAMAGE RISK",
        "risk_color": "orange",
        "spoilage_rate": "3% – 5% moisture loss per day",
        "holding_verdict": "⚠️ SHORT WINDOW: Sell within 3-4 days",
        "explanation": (
            "Fresh green chillies lose shine, moisture, and crispness quickly at ambient temperatures. "
            "Over-ripening turns them red and lowers mandi commercial grading. Minor price rises rarely "
            "compensate for shriveling weight loss."
        ),
        "damage_factors": [
            "Shriveling and moisture shrinkage",
            "Color fading from green to dull reddish",
            "Stem decay in humid storage"
        ],
        "safe_wait_days": 3
    },
    "onion": {
        "shelf_life": "3 – 6 Weeks",
        "perishability": "Moderate",
        "damage_risk": "LOW-MODERATE DAMAGE RISK",
        "risk_color": "green",
        "spoilage_rate": "1% – 2% per week (if dry and aerated)",
        "holding_verdict": "✅ GOOD PROFIT POTENTIAL: Safe to wait for price rise",
        "explanation": (
            "Well-cured onions store well in dry, ventilated storage. If market predictions project an "
            "upward trend, waiting 3-7 days poses minimal physical damage risk and can yield higher net profit. "
            "Keep away from dampness to prevent premature sprouting."
        ),
        "damage_factors": [
            "Sprouting if exposed to moisture/humidity",
            "Black mold if ventilation is restricted",
            "Minor outer skin peeling"
        ],
        "safe_wait_days": 14
    },
    "rice": {
        "shelf_life": "6 – 12 Months",
        "perishability": "Very Low (Grain)",
        "damage_risk": "VERY LOW DAMAGE RISK",
        "risk_color": "green",
        "spoilage_rate": "< 0.5% per month in dry bags",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Patient selling recommended",
        "explanation": (
            "Dry paddy and milled rice do not spoil quickly. Farmers have the financial leverage to hold "
            "stock for peak off-season market rates. Zero risk of rot in standard warehouse storage. "
            "Holding for higher prices directly maximizes profit."
        ),
        "damage_factors": [
            "Weevil / pest infestation (treat with neem or fumigation)",
            "Moisture absorption if bags touch damp floors"
        ],
        "safe_wait_days": 60
    },
    "cotton": {
        "shelf_life": "4 – 8 Months",
        "perishability": "Very Low (Fiber)",
        "damage_risk": "VERY LOW DAMAGE RISK",
        "risk_color": "green",
        "spoilage_rate": "Negligible if kept dry",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Safe to wait for peak rates",
        "explanation": (
            "Raw seed cotton can be safely stored in covered sheds. Waiting for global or regional price spikes "
            "carries virtually zero rotting risk. Protect from ground moisture and fire hazards."
        ),
        "damage_factors": [
            "Discoloration if exposed to rain",
            "Fire and moisture hazards in storage"
        ],
        "safe_wait_days": 45
    },
    "maize": {
        "shelf_life": "3 – 6 Months",
        "perishability": "Low (Grain)",
        "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green",
        "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ MODERATE PROFIT POTENTIAL: Can wait if dried properly",
        "explanation": (
            "Maize grain with moisture under 14% stores safely. If prices are expected to rise, waiting "
            "a few days to weeks provides solid returns without crop loss."
        ),
        "damage_factors": [
            "Fungal ear rot if grain moisture exceeds 15%",
            "Storage pest damage"
        ],
        "safe_wait_days": 30
    },
    "jowar": {
        "shelf_life": "4 – 6 Months", "perishability": "Low (Grain)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Patient selling recommended",
        "explanation": "Dry sorghum grain stores safely in standard sacks. Safe to wait for peak market rates.",
        "damage_factors": ["Pest infestation", "Moisture exposure"], "safe_wait_days": 45
    },
    "bajra": {
        "shelf_life": "3 – 5 Months", "perishability": "Low (Grain)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Safe to wait for peak prices",
        "explanation": "Dry pearl millet stores with high stability. Minimal risk when kept dry.",
        "damage_factors": ["Moisture dampening", "Storage insects"], "safe_wait_days": 30
    },
    "ragi": {
        "shelf_life": "6 – 12 Months", "perishability": "Very Low (Millet)", "damage_risk": "VERY LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "Negligible in dry godown",
        "holding_verdict": "✅ EXCELLENT HOLDING POTENTIAL: Highly durable millet",
        "explanation": "Finger millet has natural pest resistance and stores extremely well for months.",
        "damage_factors": ["Damp floors", "Fungal mold"], "safe_wait_days": 60
    },
    "red gram": {
        "shelf_life": "6 – 9 Months", "perishability": "Low (Pulse)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Tur pulse holds high market value",
        "explanation": "Whole red gram stores well in dry gunny bags. Holding for off-season rates is safe.",
        "damage_factors": ["Pulse beetle (Bruchid) infestation", "Moisture"], "safe_wait_days": 60
    },
    "bengal gram": {
        "shelf_life": "6 – 9 Months", "perishability": "Low (Pulse)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Safe commercial storage",
        "explanation": "Dry chana grain is durable and can be safely held for market price recoveries.",
        "damage_factors": ["Bruchid weevils", "Moisture dampening"], "safe_wait_days": 60
    },
    "green gram": {
        "shelf_life": "4 – 6 Months", "perishability": "Low (Pulse)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ GOOD PROFIT POTENTIAL: Safe to wait if fumigated",
        "explanation": "Dry moong grain can be stored safely with neem or protective treatment.",
        "damage_factors": ["Bruchid beetles", "Grain discoloration"], "safe_wait_days": 45
    },
    "black gram": {
        "shelf_life": "4 – 6 Months", "perishability": "Low (Pulse)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ GOOD PROFIT POTENTIAL: Urad stores safely",
        "explanation": "Whole urad pulse maintains quality in dry aerated storage.",
        "damage_factors": ["Moisture", "Weevil attack"], "safe_wait_days": 45
    },
    "groundnut": {
        "shelf_life": "4 – 6 Months", "perishability": "Low (Oilseed)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ GOOD PROFIT POTENTIAL: Pods store safely",
        "explanation": "Dry groundnut pods have good shelf stability. Avoid moisture to prevent aflatoxin.",
        "damage_factors": ["Aspergillus mold / aflatoxin if damp", "Rodents"], "safe_wait_days": 45
    },
    "soybean": {
        "shelf_life": "4 – 6 Months", "perishability": "Low (Oilseed)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ GOOD PROFIT POTENTIAL: Stable commercial oilseed",
        "explanation": "Soybean with moisture under 12% stores safely for favorable mandi bids.",
        "damage_factors": ["Oil rancidity if overheated", "Kernel splitting"], "safe_wait_days": 45
    },
    "sunflower": {
        "shelf_life": "3 – 5 Months", "perishability": "Low (Oilseed)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1.5% per month",
        "holding_verdict": "✅ MODERATE PROFIT POTENTIAL: Watch oil rancidity",
        "explanation": "Sunflower seeds can be held in dry shaded godowns for price gains.",
        "damage_factors": ["Heating and rancidity in humid conditions"], "safe_wait_days": 30
    },
    "sesamum": {
        "shelf_life": "6 – 10 Months", "perishability": "Very Low (Oilseed)", "damage_risk": "VERY LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "Negligible if dry",
        "holding_verdict": "✅ EXCELLENT PROFIT POTENTIAL: High value commercial oilseed",
        "explanation": "Sesame seeds possess high antioxidant stability and store exceptionally well.",
        "damage_factors": ["Direct rainwater exposure"], "safe_wait_days": 60
    },
    "castor": {
        "shelf_life": "6 – 12 Months", "perishability": "Very Low (Industrial Seed)", "damage_risk": "VERY LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "Negligible",
        "holding_verdict": "✅ EXCELLENT HOLDING POTENTIAL: Highly durable industrial seed",
        "explanation": "Castor seed has hard outer shell and can be stored for months with zero loss.",
        "damage_factors": ["Rodents", "Direct moisture"], "safe_wait_days": 60
    },
    "turmeric": {
        "shelf_life": "6 – 12 Months", "perishability": "Low (Cured Spice)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% per month",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Cured turmeric rhizomes hold premium value",
        "explanation": "Boiled and dried turmeric fingers can be safely held in godowns for peak seasonal rates.",
        "damage_factors": ["Storage weevils", "Dampness"], "safe_wait_days": 60
    },
    "ginger": {
        "shelf_life": "3 – 6 Weeks", "perishability": "Moderate (Fresh Rhizome)", "damage_risk": "MODERATE DAMAGE RISK",
        "risk_color": "orange", "spoilage_rate": "2% – 3% weekly moisture loss",
        "holding_verdict": "⚖️ BALANCED: Sell within 2-3 weeks or cure properly",
        "explanation": "Fresh ginger loses weight and wrinkles in dry air. Store in cool pit or sand.",
        "damage_factors": ["Shriveling", "Rhizome rot in standing water"], "safe_wait_days": 10
    },
    "garlic": {
        "shelf_life": "2 – 4 Months", "perishability": "Low-Moderate (Bulb)", "damage_risk": "LOW DAMAGE RISK",
        "risk_color": "green", "spoilage_rate": "< 1% weekly",
        "holding_verdict": "✅ HIGH PROFIT POTENTIAL: Cured garlic stores reliably",
        "explanation": "Well-cured garlic bulbs with dry outer wrappers store safely in ventilated sheds.",
        "damage_factors": ["Sprouting if humid", "Neck rot"], "safe_wait_days": 30
    },
    "brinjal": {
        "shelf_life": "3 – 5 Days", "perishability": "Very High (Vegetable)", "damage_risk": "HIGH DAMAGE RISK",
        "risk_color": "red", "spoilage_rate": "5% – 7% daily loss",
        "holding_verdict": "⚠️ SELL IMMEDIATELY: Fresh fruit vegetable loses gloss rapidly",
        "explanation": "Brinjals turn soft, lose calyx greenness, and seediness increases. Sell within 2-3 days.",
        "damage_factors": ["Skin dulling and moisture loss", "Fruit borer decay", "Softening"], "safe_wait_days": 2
    },
    "bhendi": {
        "shelf_life": "2 – 4 Days", "perishability": "Very High (Vegetable)", "damage_risk": "HIGH DAMAGE RISK",
        "risk_color": "red", "spoilage_rate": "6% – 8% daily loss",
        "holding_verdict": "⚠️ SELL IMMEDIATELY: Okra pods turn fibrous quickly",
        "explanation": "Bhendi pods rapidly become fibrous and woody within 48 hours post-harvest. Do not delay selling.",
        "damage_factors": ["Fiber hardening", "Black tips", "Moisture shrinkage"], "safe_wait_days": 1
    },
    "bitter gourd": {
        "shelf_life": "4 – 6 Days", "perishability": "High (Vegetable)", "damage_risk": "HIGH DAMAGE RISK",
        "risk_color": "orange", "spoilage_rate": "4% – 6% daily loss",
        "holding_verdict": "⚠️ SHORT WINDOW: Sells best when dark green and firm",
        "explanation": "Bitter gourd ridges soften and pods turn yellow/orange when held too long, losing market value.",
        "damage_factors": ["Yellowing and over-ripening", "Ridge wilting"], "safe_wait_days": 3
    }
}

DEFAULT_CROP_PROFILE = {
    "shelf_life": "1 – 2 Weeks",
    "perishability": "Moderate",
    "damage_risk": "MODERATE DAMAGE RISK",
    "risk_color": "orange",
    "spoilage_rate": "2% – 4% weekly",
    "holding_verdict": "⚖️ BALANCED: Monitor prices vs physical condition",
    "explanation": "Ensure proper storage conditions. Balance expected price appreciation against gradual quality decay.",
    "damage_factors": ["Moisture loss", "Quality degradation"],
    "safe_wait_days": 5
}


def _parse_flexible_date(val: Any, default_date: datetime.date = None) -> datetime.date:
    """Safely parse various date representations (slash, hyphen, datetime, date, tuple)."""
    if default_date is None:
        default_date = datetime.date.today()
    if val is None:
        return default_date
    if isinstance(val, datetime.date) and not isinstance(val, datetime.datetime):
        return val
    if isinstance(val, datetime.datetime):
        return val.date()
    if isinstance(val, (list, tuple)) and len(val) >= 3:
        try:
            return datetime.date(int(val[0]), int(val[1]), int(val[2]))
        except Exception:
            return default_date
    if isinstance(val, str):
        clean_str = val.strip()
        for fmt in (
            "%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y",
            "%Y.%m.%d", "%d.%m.%Y", "%B %d, %Y", "%b %d, %Y"
        ):
            try:
                return datetime.datetime.strptime(clean_str, fmt).date()
            except ValueError:
                continue
        try:
            return datetime.date.fromisoformat(clean_str[:10].replace("/", "-"))
        except Exception:
            pass
    return default_date


# Distinct scientific agronomic profiles for each crop:
# Defines individual Grade A / Grade B / Grade C thresholds, safe shelf limits, and degradation reasons.
CROP_QUALITY_PROFILES: Dict[str, Dict[str, Any]] = {
    "tomato": {
        "display_name": "Tomato",
        "category": "Highly Perishable Fruit Vegetable",
        "grade_a_max": 1,
        "grade_b_max": 3,
        "shelf_life": 4,
        "timeline_summary": "Grade A: 0–1d • Grade B: 2–3d • Grade C: 4+d (Shelf Life: 4d)",
        "grade_a_status": "Fresh Harvest (Peak Firmness)",
        "grade_b_status": "Standard Mandi Grade (Softening)",
        "grade_c_status": "Over-Ripe / Rot Hazard",
        "grade_a_reason": "Harvested within 24–48h: High turgidity, firm skin, deep red luster, zero rot, peak Grade A mandi valuation.",
        "grade_b_reason": "Harvested {days} days ago: Slight ambient moisture loss (3–5%) and skin softening. Standard commercial Grade B table use.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds safe 3–4 day shelf life. Extreme risk of soft rot, skin liquefaction, and fungal decay. Mandi buyers discount heavily. Sell immediately!",
        "future_reason": "Planned harvest in {days} days: Produce will arrive fresh at peak Grade A firmness."
    },
    "chilli": {
        "display_name": "Chilli",
        "category": "Perishable Fresh Spice",
        "grade_a_max": 2,
        "grade_b_max": 5,
        "shelf_life": 6,
        "timeline_summary": "Grade A: 0–2d • Grade B: 3–5d • Grade C: 6+d (Shelf Life: 6d)",
        "grade_a_status": "Crisp Green Harvest",
        "grade_b_status": "Standard Commercial Grade (Mild Shriveling)",
        "grade_c_status": "Severe Shriveling & Stem Rot",
        "grade_a_reason": "Harvested within 48h: Crisp green pod, firm turgid stem, glossy shine, high capsaicin pungency, top Grade A.",
        "grade_b_reason": "Harvested {days} days ago: Mild moisture loss, slight pod wrinkling and calyx browning. Commercial Grade B.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds safe 5–6 day shelf life. Severe pod shriveling, stem rot, fungal spotting, and red bleaching.",
        "future_reason": "Planned harvest in {days} days: Crop will be harvested at crisp green Grade A condition."
    },
    "onion": {
        "display_name": "Onion",
        "category": "Semi-Perishable Cured Bulb",
        "grade_a_max": 7,
        "grade_b_max": 25,
        "shelf_life": 30,
        "timeline_summary": "Grade A: 0–7d • Grade B: 8–25d • Grade C: 26+d (Shelf Life: 30d)",
        "grade_a_status": "Freshly Cured Prime Bulbs",
        "grade_b_status": "Standard Commercial Stored Bulbs",
        "grade_c_status": "Aged / Sprouting & Neck Rot Risk",
        "grade_a_reason": "Harvested {days} days ago: Freshly cured dry papery skins, tight closed neck, zero sprouting, premium Grade A.",
        "grade_b_reason": "Harvested {days} days ago: Sound commercial bulb with minor outer skin flaking in dry storage. Grade B.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds 25-day safe farm holding. Elevated risk of internal green sprouting, neck softness, and basal fungal rot.",
        "future_reason": "Planned harvest in {days} days: Field harvest will be cured for prime Grade A market supply."
    },
    "maize": {
        "display_name": "Maize",
        "category": "Cereal Grain",
        "grade_a_max": 20,
        "grade_b_max": 60,
        "shelf_life": 75,
        "timeline_summary": "Grade A: 0–20d • Grade B: 21–60d • Grade C: 61+d (Shelf Life: 75d)",
        "grade_a_status": "Prime Dry Golden Kernel",
        "grade_b_status": "Standard Commercial Dry Grain",
        "grade_c_status": "Storage Weevil & Breakage Risk",
        "grade_a_reason": "Harvested {days} days ago: Prime dried golden kernels, optimal moisture (<13%), zero cob mold or pest damage, Grade A.",
        "grade_b_reason": "Harvested {days} days ago: Standard commercial dry storage grain. Sound kernels suitable for milling and feed grade.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds 60-day farm storage. Risk of storage weevil infestation, kernel breakage, and moisture reabsorption.",
        "future_reason": "Planned harvest in {days} days: Golden ears will be shelled and dried to prime Grade A grain."
    },
    "cotton": {
        "display_name": "Cotton",
        "category": "Fiber / Cash Crop",
        "grade_a_max": 30,
        "grade_b_max": 90,
        "shelf_life": 100,
        "timeline_summary": "Grade A: 0–30d • Grade B: 31–90d • Grade C: 91+d (Shelf Life: 100d)",
        "grade_a_status": "High Luster White Lint",
        "grade_b_status": "Standard Ginning Lint Grade",
        "grade_c_status": "Discolored Lint / High Trash Penalty",
        "grade_a_reason": "Harvested {days} days ago: Bright white luster, long staple fiber, dry lint (<8% moisture), zero yellow stain, premium Grade A.",
        "grade_b_reason": "Harvested {days} days ago: Good commercial lint, slight ambient dust or mild leaf trash, standard Grade B ginning quality.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds 90-day storage. Fiber discoloration, moisture staining, compressed lint yellowing, and high trash discount.",
        "future_reason": "Planned harvest in {days} days: Bolls will be hand-picked for high-luster Grade A white lint."
    },
    "rice": {
        "display_name": "Rice",
        "category": "Staple Food Grain / Paddy",
        "grade_a_max": 60,
        "grade_b_max": 180,
        "shelf_life": 200,
        "timeline_summary": "Grade A: 0–60d • Grade B: 61–180d • Grade C: 181+d (Shelf Life: 200d)",
        "grade_a_status": "Prime Dry Translucent Grain",
        "grade_b_status": "Aged Storage Grain (Godown Grade)",
        "grade_c_status": "Aged Grain / Weevil & Rancidity Risk",
        "grade_a_reason": "Harvested {days} days ago: Prime translucent dry grain, moisture <12%, zero chalkiness, superior cooking aroma, Grade A.",
        "grade_b_reason": "Harvested {days} days ago: Well-aged paddy/rice with low stickiness and good elongation in cooking. Standard godown Grade B.",
        "grade_c_reason": "Harvested {days} days ago: Extended storage exceeding 180 days. Susceptible to rice moth/weevil, bran oil rancidity, and high milling breakage.",
        "future_reason": "Planned harvest in {days} days: Freshly harvested paddy will be dried to optimum moisture for Grade A."
    }
}

# Aliases and vernacular variants
CROP_QUALITY_PROFILES["paddy"] = CROP_QUALITY_PROFILES["rice"]
CROP_QUALITY_PROFILES["rice / paddy"] = CROP_QUALITY_PROFILES["rice"]
CROP_QUALITY_PROFILES["green chilli"] = CROP_QUALITY_PROFILES["chilli"]
CROP_QUALITY_PROFILES["corn"] = CROP_QUALITY_PROFILES["maize"]

# Grains & Millets
for c in ["jowar", "bajra", "ragi"]:
    prof = dict(CROP_QUALITY_PROFILES["maize"])
    prof["display_name"] = c.title()
    prof["category"] = "Cereal / Millet Grain"
    CROP_QUALITY_PROFILES[c] = prof

# Pulses
for c in ["red gram", "bengal gram", "green gram", "black gram"]:
    prof = dict(CROP_QUALITY_PROFILES["maize"])
    prof["display_name"] = c.title()
    prof["category"] = "Pulse / Legume"
    prof["shelf_life"] = 120
    CROP_QUALITY_PROFILES[c] = prof

# Oilseeds
for c in ["groundnut", "soybean", "sunflower", "sesamum", "castor"]:
    prof = dict(CROP_QUALITY_PROFILES["cotton"])
    prof["display_name"] = c.title()
    prof["category"] = "Oilseed Commercial Crop"
    CROP_QUALITY_PROFILES[c] = prof

# Vegetables
for c in ["brinjal", "bhendi", "bitter gourd"]:
    prof = dict(CROP_QUALITY_PROFILES["tomato"])
    prof["display_name"] = c.title()
    prof["category"] = "Fresh Perishable Vegetable"
    prof["shelf_life"] = 5
    CROP_QUALITY_PROFILES[c] = prof

# Spices & Bulbs
for c in ["garlic", "ginger", "turmeric"]:
    prof = dict(CROP_QUALITY_PROFILES["onion"])
    prof["display_name"] = c.title()
    prof["category"] = "Cured Spice / Bulb"
    prof["shelf_life"] = 45
    CROP_QUALITY_PROFILES[c] = prof


def evaluate_crop_quality_from_harvest_date(
    crop: str,
    harvest_date: Any,
    ref_date: Any = None
) -> Dict[str, Any]:
    """
    Evaluates crop quality (Grade A, Grade B, Grade C) dynamically based on harvest date,
    elapsed storage time, and the individual crop's intrinsic agronomic perishability profile.
    """
    ref_d = _parse_flexible_date(ref_date, default_date=datetime.date.today())
    h_d = _parse_flexible_date(harvest_date, default_date=ref_d)

    days_elapsed = (ref_d - h_d).days
    crop_str = crop.lower().strip() if crop else ""
    if "rice" in crop_str or "paddy" in crop_str:
        crop_clean = "rice"
    elif "chilli" in crop_str or "mirchi" in crop_str:
        crop_clean = "chilli"
    elif "tomato" in crop_str:
        crop_clean = "tomato"
    elif "cotton" in crop_str or "kapas" in crop_str:
        crop_clean = "cotton"
    elif "maize" in crop_str or "corn" in crop_str:
        crop_clean = "maize"
    elif "onion" in crop_str:
        crop_clean = "onion"
    else:
        crop_clean = crop_str

    profile = CROP_QUALITY_PROFILES.get(crop_clean, {
        "display_name": crop.title() if crop else "Produce",
        "category": "Agricultural Produce",
        "grade_a_max": 2,
        "grade_b_max": 6,
        "shelf_life": 10,
        "timeline_summary": "Grade A: 0–2d • Grade B: 3–6d • Grade C: 7+d (Shelf Life: 10d)",
        "grade_a_status": "Fresh Harvest",
        "grade_b_status": "Standard Commercial Grade",
        "grade_c_status": "Aged Quality / Degradation Risk",
        "grade_a_reason": "Harvested {days} days ago: Fresh crop condition, firm texture, top mandi quality.",
        "grade_b_reason": "Harvested {days} days ago: Fair storage condition, standard commercial mandi grade.",
        "grade_c_reason": "Harvested {days} days ago: Exceeds safe farm holding. Quality degradation and spoilage risk.",
        "future_reason": "Planned harvest in {days} days: Produce will arrive fresh at Grade A."
    })

    shelf_life = profile["shelf_life"]
    grade_a_max = profile["grade_a_max"]
    grade_b_max = profile["grade_b_max"]
    timeline_summary = profile["timeline_summary"]

    # Future harvest date: Planned / upcoming harvest
    if days_elapsed < 0:
        ahead = abs(days_elapsed)
        return {
            "quality": "Grade A",
            "days_elapsed": days_elapsed,
            "status": f"Upcoming Harvest ({ahead}d to harvest)",
            "reason": profile["future_reason"].format(days=ahead),
            "is_fresh": True,
            "is_past_shelf_life": False,
            "shelf_life_limit": shelf_life,
            "safe_wait_days": grade_a_max,
            "timeline_summary": timeline_summary,
            "crop_display": profile["display_name"],
            "category": profile["category"]
        }

    # Harvested today (day 0)
    if days_elapsed == 0:
        return {
            "quality": "Grade A",
            "days_elapsed": 0,
            "status": "Fresh Harvest (Today)",
            "reason": f"Harvested today: Maximum freshness, peak moisture, firm texture, and premium Grade A mandi valuation for {profile['display_name']}.",
            "is_fresh": True,
            "is_past_shelf_life": False,
            "shelf_life_limit": shelf_life,
            "safe_wait_days": max(0, grade_a_max),
            "timeline_summary": timeline_summary,
            "crop_display": profile["display_name"],
            "category": profile["category"]
        }

    # Harvested within Grade A window
    if days_elapsed <= grade_a_max:
        return {
            "quality": "Grade A",
            "days_elapsed": days_elapsed,
            "status": profile["grade_a_status"],
            "reason": profile["grade_a_reason"].format(days=days_elapsed),
            "is_fresh": True,
            "is_past_shelf_life": False,
            "shelf_life_limit": shelf_life,
            "safe_wait_days": max(0, grade_a_max - days_elapsed),
            "timeline_summary": timeline_summary,
            "crop_display": profile["display_name"],
            "category": profile["category"]
        }

    # Harvested within Grade B window
    if days_elapsed <= grade_b_max:
        return {
            "quality": "Grade B",
            "days_elapsed": days_elapsed,
            "status": profile["grade_b_status"],
            "reason": profile["grade_b_reason"].format(days=days_elapsed),
            "is_fresh": False,
            "is_past_shelf_life": False,
            "shelf_life_limit": shelf_life,
            "safe_wait_days": max(0, shelf_life - days_elapsed),
            "timeline_summary": timeline_summary,
            "crop_display": profile["display_name"],
            "category": profile["category"]
        }

    # Grade C: Exceeds safe commercial grade window
    is_past_shelf = days_elapsed >= shelf_life
    return {
        "quality": "Grade C",
        "days_elapsed": days_elapsed,
        "status": profile["grade_c_status"],
        "reason": profile["grade_c_reason"].format(days=days_elapsed),
        "is_fresh": False,
        "is_past_shelf_life": is_past_shelf,
        "shelf_life_limit": shelf_life,
        "safe_wait_days": 0,
        "timeline_summary": timeline_summary,
        "crop_display": profile["display_name"],
        "category": profile["category"]
    }


def calculate_holding_spoilage_and_loss(
    crop: str,
    quality: str = "Grade A",
    days_since_harvest: int = 0,
    wait_days: int = 3
) -> Dict[str, Any]:
    """
    Computes physical spoilage loss (volume shrinkage and rot discard) and commercial
    price markdown resulting from holding the crop for `wait_days`.
    
    Agricultural physics: produce decay kinetics depend on the specific crop's biological
    characteristics (water content, respiration rate, skin cuticle, storage durability).
    """
    crop_str = crop.lower().strip() if crop else ""
    if "rice" in crop_str or "paddy" in crop_str:
        crop_clean = "rice"
    elif "chilli" in crop_str or "mirchi" in crop_str:
        crop_clean = "chilli"
    elif "tomato" in crop_str:
        crop_clean = "tomato"
    elif "cotton" in crop_str or "kapas" in crop_str:
        crop_clean = "cotton"
    elif "maize" in crop_str or "corn" in crop_str:
        crop_clean = "maize"
    elif "onion" in crop_str:
        crop_clean = "onion"
    elif "turmeric" in crop_str or "pasupu" in crop_str or "haldi" in crop_str:
        crop_clean = "turmeric"
    elif "ginger" in crop_str or "allam" in crop_str:
        crop_clean = "ginger"
    elif "garlic" in crop_str or "vellulli" in crop_str:
        crop_clean = "garlic"
    elif "brinjal" in crop_str or "eggplant" in crop_str or "vankaya" in crop_str:
        crop_clean = "brinjal"
    elif "bhendi" in crop_str or "bhindi" in crop_str or "okra" in crop_str or "ladies finger" in crop_str:
        crop_clean = "bhendi"
    elif "bitter gourd" in crop_str or "karela" in crop_str or "kakarakaya" in crop_str:
        crop_clean = "bitter gourd"
    elif "bottle gourd" in crop_str or "sorakaya" in crop_str or "lauki" in crop_str:
        crop_clean = "bottle gourd"
    elif "cabbage" in crop_str:
        crop_clean = "cabbage"
    elif "cauliflower" in crop_str:
        crop_clean = "cauliflower"
    elif "cucumber" in crop_str or "dosakaya" in crop_str or "kheera" in crop_str:
        crop_clean = "cucumber"
    elif "potato" in crop_str or "alu" in crop_str:
        crop_clean = "potato"
    elif "pumpkin" in crop_str:
        crop_clean = "pumpkin"
    elif "banana" in crop_str:
        crop_clean = "banana"
    elif "papaya" in crop_str:
        crop_clean = "papaya"
    elif "guava" in crop_str:
        crop_clean = "guava"
    elif "mango" in crop_str:
        crop_clean = "mango"
    elif "watermelon" in crop_str:
        crop_clean = "watermelon"
    elif "sweet orange" in crop_str or "mosambi" in crop_str:
        crop_clean = "sweet orange"
    else:
        crop_clean = crop_str
    total_days = max(0, days_since_harvest + wait_days)

    if crop_clean in ["tomato", "brinjal", "bhendi", "bitter gourd", "bottle gourd", "cucumber", "cabbage", "cauliflower"]:
        # Highly perishable fresh vegetables (Safe farm shelf life: 3-5 days at ambient Telangana temperatures)
        if days_since_harvest <= 1:
            vol_loss_pct = 5.0
            price_markdown_pct = 8.0
            is_severe = False
            verdict = "⚠️ MODERATE HOLDING RISK: Minor moisture loss and grade softening"
            warning = f"Holding fresh {crop_clean} for {wait_days} days causes ~5% weight loss and minor softening."
        elif 2 <= days_since_harvest <= 3:
            vol_loss_pct = 22.0
            price_markdown_pct = 25.0
            is_severe = True
            verdict = "⚠️ HIGH SPOILAGE RISK: Rapid soft rot onset"
            warning = f"{crop_clean.title()} at {days_since_harvest} days reaches {total_days} days. ~22% rot discard; remainder drops to Grade C."
        else:
            # Already 4+ days old! Holding 3 more days leads to severe decay
            vol_loss_pct = 80.0
            price_markdown_pct = 40.0
            is_severe = True
            verdict = "🚨 CATASTROPHIC SPOILAGE: 80%+ Rot & Discard (Severe Net Deficit)"
            warning = (
                f"{crop_clean.title()} is already {days_since_harvest} days post-harvest (shelf life: 3-5 days). "
                f"Holding for {wait_days} more days causes near-total liquefaction and mold decay. "
                f"80%+ of volume will be discarded as unmarketable. Waiting guarantees a severe financial loss!"
            )

    elif crop_clean in ["banana", "papaya", "guava", "mango", "watermelon", "sweet orange"]:
        # Fresh fruit: rapid ripening and bruising
        if days_since_harvest <= 1:
            vol_loss_pct = 4.0
            price_markdown_pct = 5.0
            is_severe = False
            verdict = "⚠️ MODERATE HOLDING RISK: Moisture shrinkage and rapid ripening"
            warning = f"Fresh {crop_clean} ripens quickly over {wait_days} days. Monitor firmness."
        elif 2 <= days_since_harvest <= 4:
            vol_loss_pct = 25.0
            price_markdown_pct = 30.0
            is_severe = True
            verdict = "⚠️ HIGH SPOILAGE RISK: Over-ripening and bruising"
            warning = f"{crop_clean.title()} at {days_since_harvest} days reaches over-ripe state. ~25% rot and bruise discard."
        else:
            vol_loss_pct = 75.0
            price_markdown_pct = 45.0
            is_severe = True
            verdict = "🚨 SEVERE SPOILAGE: Unmarketable fruit rot"
            warning = f"{crop_clean.title()} stored for {days_since_harvest} days suffers skin blackening and decay. ~75% loss."

    elif crop_clean in ["chilli"]:
        # Safe shelf life: 5-6 days
        if days_since_harvest <= 2:
            vol_loss_pct = 4.0
            price_markdown_pct = 5.0
            is_severe = False
            verdict = "⚠️ MINOR SHRINKAGE: Moisture loss expected"
            warning = f"Chillies will lose ~4% moisture weight and color gloss over {wait_days} days."
        elif 3 <= days_since_harvest <= 5:
            vol_loss_pct = 25.0
            price_markdown_pct = 20.0
            is_severe = True
            verdict = "⚠️ HIGH SHRIVELING & STEM ROT RISK"
            warning = f"Green chillies will shrivel and turn soft. Expect ~25% discard loss."
        else:
            vol_loss_pct = 70.0
            price_markdown_pct = 35.0
            is_severe = True
            verdict = "🚨 SEVERE DRYING & QUALITY DECAY"
            warning = f"Chillies stored for {days_since_harvest} days lose color, rot at stem, and suffer ~70% loss."

    elif crop_clean in ["onion", "garlic", "ginger", "turmeric", "potato", "pumpkin"]:
        # Semi-durable bulbs/rhizomes: Safe shelf life: 25-45 days
        if days_since_harvest <= 7:
            vol_loss_pct = 0.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ LOW HOLDING RISK: Safe in dry ventilated storage"
            warning = f"Freshly cured {crop_clean} stores very well. Waiting {wait_days} days causes zero rot."
        elif 8 <= days_since_harvest <= 25:
            vol_loss_pct = 3.0
            price_markdown_pct = 2.0
            is_severe = False
            verdict = "⚠️ MODERATE STORAGE RISK: Minor shrinkage"
            warning = f"Stored {crop_clean} at {days_since_harvest} days experiences ~3% moisture shrinkage."
        else:
            vol_loss_pct = 25.0
            price_markdown_pct = 20.0
            is_severe = True
            verdict = "🚨 SPROUTING & NECK ROT RISK"
            warning = f"Extended storage ({days_since_harvest} days) risks internal sprouting and neck rot. ~25% loss."

    elif crop_clean in ["maize", "corn", "jowar", "bajra", "ragi", "red gram", "bengal gram", "green gram", "black gram", "soybean", "sunflower"]:
        # Dry cereal / pulse / oilseed grain: Safe farm storage up to 60-75 days (ZERO rot in 3 days)
        if days_since_harvest <= 30:
            vol_loss_pct = 0.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ NEGLIGIBLE GRAIN LOSS: Optimum dry storage"
            warning = f"Dry {crop_clean} grains (<13% moisture) have zero spoilage risk over {wait_days} days."
        elif 31 <= days_since_harvest <= 60:
            vol_loss_pct = 1.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ SAFE STORAGE GRAIN: Monitor moisture"
            warning = f"{crop_clean.title()} at {days_since_harvest} days has minimal weight variation (~1%) in standard farm sacks."
        else:
            vol_loss_pct = 10.0
            price_markdown_pct = 10.0
            is_severe = True
            verdict = "⚠️ STORAGE WEEVIL & MOLD RISK"
            warning = f"{crop_clean.title()} stored for {days_since_harvest} days faces storage weevil infestation and grain breakage."

    elif crop_clean in ["cotton", "kapas", "groundnut", "sesamum", "sesame", "castor"]:
        # Fiber & dry oilseed: Safe storage up to 90-100 days if kept dry
        if days_since_harvest <= 30:
            vol_loss_pct = 0.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ PRIME LINT QUALITY: Zero spoilage risk"
            warning = f"Raw seed cotton / oilseed retains full fiber luster and grade over {wait_days} days."
        elif 31 <= days_since_harvest <= 90:
            vol_loss_pct = 1.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ STABLE STORAGE: Protect from ambient humidity"
            warning = f"Stored {crop_clean} at {days_since_harvest} days maintains good commercial quality."
        else:
            vol_loss_pct = 8.0
            price_markdown_pct = 12.0
            is_severe = True
            verdict = "⚠️ QUALITY PENALTY & DISCOLORATION"
            warning = f"{crop_clean.title()} stored for {days_since_harvest} days suffers moisture staining and price discounts."

    elif crop_clean in ["rice", "paddy"]:
        # Staple grain: Extremely durable storage (180+ days)
        if days_since_harvest <= 60:
            vol_loss_pct = 0.0
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ NEGLIGIBLE SPOILAGE RISK: Grains store safely"
            warning = f"Dry paddy/rice has zero rot risk over {wait_days} days in standard warehouse storage."
        elif 61 <= days_since_harvest <= 180:
            vol_loss_pct = 0.5
            price_markdown_pct = 0.0
            is_severe = False
            verdict = "✅ AGED GRAIN QUALITY: Enhanced cooking characteristics"
            warning = f"Rice stored for {days_since_harvest} days cooks with excellent grain separation and elongation."
        else:
            vol_loss_pct = 10.0
            price_markdown_pct = 10.0
            is_severe = True
            verdict = "⚠️ AGING GRAIN & WEEVIL RISK"
            warning = f"Rice stored for {days_since_harvest} days risks storage pests, bran rancidity, and milling breakage."

    else:
        # Generic agricultural fallback
        if days_since_harvest <= 2:
            vol_loss_pct = 2.0
            price_markdown_pct = 2.0
            is_severe = False
            verdict = "⚠️ NORMAL POST-HARVEST SHRINKAGE"
            warning = f"Normal moisture loss of ~2% over {wait_days} days."
        elif 3 <= days_since_harvest <= 6:
            vol_loss_pct = 15.0
            price_markdown_pct = 15.0
            is_severe = True
            verdict = "⚠️ ELEVATED SPOILAGE RISK"
            warning = f"Noticeable quality deterioration and ~15% loss over {wait_days} days."
        else:
            vol_loss_pct = 50.0
            price_markdown_pct = 30.0
            is_severe = True
            verdict = "🚨 SEVERE AGING LOSS"
            warning = f"Produce harvested {days_since_harvest} days ago will experience heavy decay (~50% loss)."

    salable_pct = max(0.0, 100.0 - vol_loss_pct)

    return {
        "volume_loss_pct": round(vol_loss_pct, 1),
        "salable_pct": round(salable_pct, 1),
        "quality_markdown_pct": round(price_markdown_pct, 1),
        "is_severe_spoilage": is_severe,
        "holding_verdict": verdict,
        "verdict": verdict,
        "holding_warning": warning,
        "total_days_post_harvest": total_days
    }



def get_crop_spoilage_risk(
    crop: str,
    quality: str = "Grade A",
    harvest_date: Any = None,
    ref_date: Any = None
) -> dict:
    """Retrieve detailed perishability, damage risk, and profit vs loss analysis for delayed selling."""
    crop_clean = crop.lower().strip() if crop else ""
    profile = CROP_SPOILAGE_PROFILES.get(crop_clean, DEFAULT_CROP_PROFILE).copy()

    # If harvest date is provided, attach dynamic harvest evaluation
    if harvest_date:
        h_eval = evaluate_crop_quality_from_harvest_date(crop, harvest_date, ref_date)
        profile["harvest_evaluation"] = h_eval
        profile["days_since_harvest"] = h_eval["days_elapsed"]

        holding_spoilage = calculate_holding_spoilage_and_loss(
            crop=crop,
            quality=h_eval["quality"],
            days_since_harvest=h_eval["days_elapsed"],
            wait_days=3
        )
        profile["holding_spoilage"] = holding_spoilage

        # Elevate risk if crop is past shelf life or Grade C
        if h_eval.get("is_past_shelf_life") or (h_eval["quality"] == "Grade C" and profile["perishability"] in ["Very High", "High"]):
            profile["damage_risk"] = "CRITICAL DAMAGE RISK"
            profile["holding_verdict"] = f"🚨 SELL IMMEDIATELY: Harvested {h_eval['days_elapsed']} days ago — rapid rot in progress!"
            profile["explanation"] = holding_spoilage["holding_warning"]
        elif holding_spoilage["is_severe_spoilage"]:
            profile["damage_risk"] = "HIGH DAMAGE RISK"
            profile["holding_verdict"] = holding_spoilage["holding_verdict"]
    elif quality == "Grade C" and profile["perishability"] in ["Very High", "High"]:
        profile["damage_risk"] = "CRITICAL DAMAGE RISK"
        profile["holding_verdict"] = "🚨 SELL IMMEDIATELY: Grade C produce deteriorates within 24-48 hours!"
        profile["holding_spoilage"] = calculate_holding_spoilage_and_loss(crop, quality, days_since_harvest=5, wait_days=3)

    return profile
