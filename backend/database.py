import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE = DATA_DIR / "market_data.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT NOT NULL,
            market TEXT NOT NULL,
            location TEXT NOT NULL,
            price_per_kg REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_sample_data():
    connection = get_connection()
    cursor = connection.cursor()

    data = [
        # ====================================================
        # TOMATO
        # ====================================================
        ("Tomato", "Bowenpally", "Hyderabad", 30, "2026-09-05"),
        ("Tomato", "Gudimalkapur", "Hyderabad", 27, "2026-09-05"),
        ("Tomato", "Warangal Market", "Warangal", 25, "2026-09-05"),
        ("Tomato", "Nalgonda Market", "Nalgonda", 28, "2026-09-05"),

        # ====================================================
        # RICE
        # ====================================================
        ("Rice", "Bowenpally", "Hyderabad", 42, "2026-09-05"),
        ("Rice", "Warangal Market", "Warangal", 40, "2026-09-05"),
        ("Rice", "Nalgonda Market", "Nalgonda", 43, "2026-09-05"),

        # ====================================================
        # COTTON
        # ====================================================
        ("Cotton", "Bowenpally", "Hyderabad", 75, "2026-09-05"),
        ("Cotton", "Warangal Market", "Warangal", 72, "2026-09-05"),
        ("Cotton", "Nalgonda Market", "Nalgonda", 74, "2026-09-05"),

        # ====================================================
        # CHILLI
        # ====================================================
        ("Chilli", "Bowenpally", "Hyderabad", 110, "2026-09-05"),
        ("Chilli", "Warangal Market", "Warangal", 105, "2026-09-05"),
        ("Chilli", "Nalgonda Market", "Nalgonda", 108, "2026-09-05"),

        # ====================================================
        # MAIZE
        # ====================================================
        ("Maize", "Bowenpally", "Hyderabad", 24, "2026-09-05"),
        ("Maize", "Warangal Market", "Warangal", 22, "2026-09-05"),
        ("Maize", "Nalgonda Market", "Nalgonda", 23, "2026-09-05"),

        # ====================================================
        # ONION
        # ====================================================
        ("Onion", "Bowenpally", "Hyderabad", 28, "2026-09-05"),
        ("Onion", "Warangal Market", "Warangal", 25, "2026-09-05"),
        ("Onion", "Nalgonda Market", "Nalgonda", 27, "2026-09-05"),
    ]

    # ========================================================
    # INSERT ONLY IF RECORD DOES NOT ALREADY EXIST
    # ========================================================

    for crop, market, location, price, date in data:

        cursor.execute("""
            SELECT COUNT(*)
            FROM market_prices
            WHERE crop = ?
            AND market = ?
            AND date = ?
        """, (crop, market, date))

        exists = cursor.fetchone()[0]

        if exists == 0:

            cursor.execute("""
                INSERT INTO market_prices
                (crop, market, location, price_per_kg, date)
                VALUES (?, ?, ?, ?, ?)
            """, (
                crop,
                market,
                location,
                price,
                date
            ))

    connection.commit()
    connection.close()