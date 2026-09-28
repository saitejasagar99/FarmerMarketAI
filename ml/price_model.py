from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# LOAD DATA
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "historical_prices.csv"

df = pd.read_csv(DATA_FILE)

CROP_ALIASES = {
    "green chilli": "chilli",
    "paddy": "rice",
    "bhindi": "bhendi",
    "okra": "bhendi",
    "ladies finger": "bhendi",
    "tur": "red gram",
    "arhar": "red gram",
    "kandi": "red gram",
    "chana": "bengal gram",
    "chickpea": "bengal gram",
    "moong": "green gram",
    "pesalu": "green gram",
    "urad": "black gram",
    "minumu": "black gram",
    "peanut": "groundnut",
    "corn": "maize",
    "sorghum": "jowar",
    "pearl millet": "bajra",
    "finger millet": "ragi",
    "kapas": "cotton",
    "pasupu": "turmeric",
    "haldi": "turmeric",
    "allam": "ginger",
    "vellulli": "garlic",
    "eggplant": "brinjal",
    "vankaya": "brinjal",
    "karela": "bitter gourd",
    "sorakaya": "bottle gourd",
    "lauki": "bottle gourd",
    "alu": "potato",
    "kheera": "cucumber",
    "til": "sesame",
    "sesamum": "sesame",
}


# ============================================================
# TRAIN MODEL
# ============================================================

def train_model(crop):
    global df
    target_crop = CROP_ALIASES.get(crop.lower().strip(), crop.lower().strip())

    crop_data = df[
        df["crop"].astype(str).str.lower() == target_crop
    ].copy()

    if len(crop_data) < 5:
        try:
            df = pd.read_csv(DATA_FILE)
            crop_data = df[
                df["crop"].astype(str).str.lower() == target_crop
            ].copy()
        except Exception:
            pass

    # Need enough historical records
    if len(crop_data) < 5:
        return None

    # --------------------------------------------------------
    # CONVERT DATE
    # --------------------------------------------------------

    crop_data["date"] = pd.to_datetime(
        crop_data["date"],
        errors="coerce"
    )

    # Remove invalid dates
    crop_data = crop_data.dropna(
        subset=["date"]
    )

    if len(crop_data) < 5:
        return None

    # --------------------------------------------------------
    # CLEAN PRICE DATA
    # --------------------------------------------------------

    crop_data["price"] = pd.to_numeric(
        crop_data["price"],
        errors="coerce"
    )

    crop_data = crop_data.dropna(
        subset=["price"]
    )

    if len(crop_data) < 5:
        return None

    # --------------------------------------------------------
    # SORT BY DATE
    # --------------------------------------------------------

    crop_data = crop_data.sort_values(
        "date"
    ).reset_index(drop=True)

    # --------------------------------------------------------
    # CREATE NUMERICAL DAY FEATURE
    # --------------------------------------------------------

    crop_data["day"] = (
        crop_data["date"]
        - crop_data["date"].min()
    ).dt.days

    # --------------------------------------------------------
    # FEATURES
    # --------------------------------------------------------

    X = crop_data[
        ["day"]
    ]

    y = crop_data[
        "price"
    ]

    # --------------------------------------------------------
    # TRAIN LINEAR REGRESSION
    # --------------------------------------------------------

    model = LinearRegression()

    model.fit(
        X,
        y
    )

    return model, crop_data


# ============================================================
# MODEL EVALUATION
# ============================================================

def evaluate_model(crop):

    result = train_model(crop)

    if result is None:
        return None

    model, crop_data = result

    X = crop_data[
        ["day"]
    ]

    y = crop_data[
        "price"
    ]

    # Predict historical prices
    predictions = model.predict(X)

    # Mean Absolute Error
    mae = mean_absolute_error(
        y,
        predictions
    )

    # R2 Score
    r2 = r2_score(
        y,
        predictions
    )

    return {
        "mae": round(float(mae), 2),
        "r2": round(float(r2), 2)
    }


# ============================================================
# PREDICT FUTURE PRICE
# ============================================================

def predict_price(
    crop,
    days_ahead=3
):

    result = train_model(
        crop
    )

    if result is None:
        return None

    model, crop_data = result

    # --------------------------------------------------------
    # LAST HISTORICAL DAY
    # --------------------------------------------------------

    last_day = int(
        crop_data["day"].max()
    )

    future_day = (
        last_day +
        int(days_ahead)
    )

    # --------------------------------------------------------
    # CREATE FUTURE DATAFRAME
    # --------------------------------------------------------
    # This fixes:
    # "X does not have valid feature names"
    # --------------------------------------------------------

    future_data = pd.DataFrame(
        {
            "day": [future_day]
        }
    )

    # --------------------------------------------------------
    # PREDICT
    # --------------------------------------------------------

    prediction = model.predict(
        future_data
    )[0]

    prediction = float(
        prediction
    )

    # --------------------------------------------------------
    # CURRENT PRICE
    # --------------------------------------------------------

    current_price = float(
        crop_data.iloc[-1]["price"]
    )

    # --------------------------------------------------------
    # LIMIT EXTREME PREDICTIONS
    # --------------------------------------------------------

    maximum_price = (
        current_price * 1.20
    )

    minimum_price = (
        current_price * 0.80
    )

    prediction = max(
        minimum_price,
        min(
            prediction,
            maximum_price
        )
    )

    # --------------------------------------------------------
    # PREVENT NEGATIVE PRICE
    # --------------------------------------------------------

    prediction = max(
        0,
        prediction
    )

    return round(
        prediction,
        2
    )


# ============================================================
# DETAILED PRICE PREDICTION
# ============================================================

def predict_price_details(
    crop,
    days_ahead=3
):

    result = train_model(
        crop
    )

    if result is None:
        return None

    model, crop_data = result

    # --------------------------------------------------------
    # LAST DAY
    # --------------------------------------------------------

    last_day = int(
        crop_data["day"].max()
    )

    future_day = (
        last_day +
        int(days_ahead)
    )

    # --------------------------------------------------------
    # FUTURE DATA
    # --------------------------------------------------------

    future_data = pd.DataFrame(
        {
            "day": [future_day]
        }
    )

    # --------------------------------------------------------
    # RAW PREDICTION
    # --------------------------------------------------------

    raw_prediction = float(
        model.predict(
            future_data
        )[0]
    )

    # --------------------------------------------------------
    # CURRENT PRICE
    # --------------------------------------------------------

    current_price = float(
        crop_data.iloc[-1]["price"]
    )

    # --------------------------------------------------------
    # LIMIT EXTREME MOVEMENT
    # --------------------------------------------------------

    minimum_price = (
        current_price * 0.80
    )

    maximum_price = (
        current_price * 1.20
    )

    prediction = max(
        minimum_price,
        min(
            raw_prediction,
            maximum_price
        )
    )

    prediction = max(
        0,
        prediction
    )

    # --------------------------------------------------------
    # MODEL EVALUATION
    # --------------------------------------------------------

    evaluation = evaluate_model(
        crop
    )

    if evaluation is None:

        mae = 0
        r2 = 0

    else:

        mae = evaluation["mae"]
        r2 = evaluation["r2"]

    # --------------------------------------------------------
    # PREDICTION RANGE
    # --------------------------------------------------------

    lower_bound = max(
        0,
        prediction - mae
    )

    upper_bound = (
        prediction + mae
    )

    # --------------------------------------------------------
    # CONFIDENCE
    # --------------------------------------------------------

    if r2 >= 0.80:

        confidence = "High"

    elif r2 >= 0.50:

        confidence = "Moderate"

    else:

        confidence = "Low"

    # --------------------------------------------------------
    # RETURN DETAILS
    # --------------------------------------------------------

    return {

        "current_price": round(
            current_price,
            2
        ),

        "predicted_price": round(
            prediction,
            2
        ),

        "lower_bound": round(
            lower_bound,
            2
        ),

        "upper_bound": round(
            upper_bound,
            2
        ),

        "confidence": confidence,

        "mae": round(
            mae,
            2
        ),

        "r2": round(
            r2,
            2
        )
    }


# ============================================================
# TEST MODEL
# ============================================================

if __name__ == "__main__":

    crop = "Tomato"

    # --------------------------------------------------------
    # CHECK DATA
    # --------------------------------------------------------

    crop_data = df[
        df["crop"].astype(str).str.lower()
        == crop.lower()
    ].copy()

    if crop_data.empty:

        print(
            f"❌ No data found for {crop}"
        )

    else:

        # ----------------------------------------------------
        # CURRENT PRICE
        # ----------------------------------------------------

        crop_data["price"] = pd.to_numeric(
            crop_data["price"],
            errors="coerce"
        )

        crop_data = crop_data.dropna(
            subset=["price"]
        )

        current_price = float(
            crop_data.iloc[-1]["price"]
        )

        # ----------------------------------------------------
        # PREDICT
        # ----------------------------------------------------

        predicted_price = predict_price(
            crop,
            days_ahead=3
        )

        # ----------------------------------------------------
        # DETAILED PREDICTION
        # ----------------------------------------------------

        details = predict_price_details(
            crop,
            days_ahead=3
        )

        print()
        print(
            "🌾 Farmer Market Intelligence"
        )
        print(
            "================================"
        )

        print(
            f"Crop: {crop}"
        )

        print(
            f"Current Price: "
            f"₹{current_price:.2f}/kg"
        )

        # ----------------------------------------------------
        # PREDICTION
        # ----------------------------------------------------

        if predicted_price is not None:

            print(
                f"Predicted Price (3 days): "
                f"₹{predicted_price:.2f}/kg"
            )

            change = (
                predicted_price -
                current_price
            )

            percentage = (
                (change / current_price) * 100
                if current_price > 0
                else 0
            )

            print(
                f"Expected Change: "
                f"{percentage:+.2f}%"
            )

        else:

            print(
                "Predicted Price: "
                "Not enough data"
            )

        # ----------------------------------------------------
        # ML DETAILS
        # ----------------------------------------------------

        if details is not None:

            print()
            print(
                "📊 ML MODEL EVALUATION"
            )
            print(
                "================================"
            )

            print(
                f"Prediction Range: "
                f"₹{details['lower_bound']:.2f}"
                f" - "
                f"₹{details['upper_bound']:.2f}/kg"
            )

            print(
                f"Confidence: "
                f"{details['confidence']}"
            )

            print(
                f"MAE: "
                f"₹{details['mae']:.2f}"
            )

            print(
                f"R² Score: "
                f"{details['r2']:.2f}"
            )

        else:

            print()
            print(
                "⚠️ Model evaluation unavailable"
            )