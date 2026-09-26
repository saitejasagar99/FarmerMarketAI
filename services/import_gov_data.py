import pandas as pd
from pathlib import Path

from backend.database import get_connection, create_tables


# ============================================================
# FILE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_FILE = BASE_DIR / "data" / "Data Gov.csv"


# ============================================================
# CROP MAPPING
# ============================================================

GOVERNMENT_CROPS = [
    "Tomato",
    "Rice",
    "Cotton",
    "Chilli",
    "Green Chilli",
    "Maize",
    "Onion"
]


# ============================================================
# IMPORT GOVERNMENT DATA
# ============================================================

def import_government_data():

    print("Loading Government mandi dataset...")

    # --------------------------------------------------------
    # CHECK FILE
    # --------------------------------------------------------

    if not CSV_FILE.exists():

        print("ERROR: Government dataset not found!")
        print(f"Expected file: {CSV_FILE}")

        return

    # --------------------------------------------------------
    # READ CSV
    # --------------------------------------------------------

    df = pd.read_csv(CSV_FILE)

    print(f"Total records found: {len(df)}")

    # --------------------------------------------------------
    # DATABASE CONNECTION
    # --------------------------------------------------------

    connection = get_connection()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # REMOVE OLD GOVERNMENT RECORDS
    #
    # Demo records such as Bowenpally, Warangal Market and
    # Nalgonda Market are NOT removed because this deletion
    # only targets records whose crop belongs to the
    # government crop list AND whose market is not our demo
    # market set.
    # --------------------------------------------------------

    print("Cleaning old government records...")

    demo_markets = [
        "Bowenpally",
        "Warangal Market",
        "Nalgonda Market"
    ]

    placeholders = ",".join(
        ["?"] * len(GOVERNMENT_CROPS)
    )

    demo_placeholders = ",".join(
        ["?"] * len(demo_markets)
    )

    cursor.execute(
        f"""
        DELETE FROM market_prices
        WHERE crop IN ({placeholders})
        AND market NOT IN ({demo_placeholders})
        """,
        GOVERNMENT_CROPS + demo_markets
    )

    deleted = cursor.rowcount

    print(
        f"Old government records removed: {deleted}"
    )

    # --------------------------------------------------------
    # IMPORT COUNTERS
    # --------------------------------------------------------

    imported = 0
    skipped = 0

    # --------------------------------------------------------
    # PROCESS DATA
    # --------------------------------------------------------

    for _, row in df.iterrows():

        try:

            commodity = str(
                row["Commodity"]
            ).strip()

            market = str(
                row["Market"]
            ).strip()

            state = str(
                row["State"]
            ).strip()

            district = str(
                row["District"]
            ).strip()

            # ------------------------------------------------
            # MODAL PRICE
            # ------------------------------------------------

            modal_price = row[
                "Modal_x0020_Price"
            ]

            if pd.isna(modal_price):

                skipped += 1
                continue

            # ------------------------------------------------
            # CONVERT PRICE
            #
            # Government dataset:
            # ₹ / quintal
            #
            # Database:
            # ₹ / kg
            # ------------------------------------------------

            price_per_kg = (
                float(modal_price) / 100
            )

            # ------------------------------------------------
            # NORMALIZE DATE
            #
            # Example:
            # 06-09-2026
            #
            # becomes:
            # 2026-09-06
            # ------------------------------------------------

            date_value = pd.to_datetime(
                row["Arrival_Date"],
                dayfirst=True,
                errors="coerce"
            )

            if pd.isna(date_value):

                skipped += 1
                continue

            date = date_value.strftime(
                "%Y-%m-%d"
            )

            # ------------------------------------------------
            # CHECK DUPLICATE
            # ------------------------------------------------

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM market_prices
                WHERE crop = ?
                AND market = ?
                AND date = ?
                """,
                (
                    commodity,
                    market,
                    date
                )
            )

            exists = cursor.fetchone()[0]

            # ------------------------------------------------
            # INSERT
            # ------------------------------------------------

            if exists == 0:

                cursor.execute(
                    """
                    INSERT INTO market_prices
                    (
                        crop,
                        market,
                        location,
                        price_per_kg,
                        date
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        commodity,
                        market,
                        f"{district}, {state}",
                        price_per_kg,
                        date
                    )
                )

                imported += 1

        except Exception as e:

            skipped += 1

            print(
                f"Skipped row: {e}"
            )

    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    connection.commit()

    connection.close()

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print("--------------------------------")
    print(
        f"Total records : {len(df)}"
    )
    print(
        f"Old records   : {deleted}"
    )
    print(
        f"Imported      : {imported}"
    )
    print(
        f"Skipped       : {skipped}"
    )
    print("--------------------------------")

    print(
        "Government mandi data imported successfully!"
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    create_tables()

    import_government_data()