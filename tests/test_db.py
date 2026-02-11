import sqlite3
import os


def test_manual_database_interaction():
    # 1. SETUP: Skapa en anslutning till en databas i minnet
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

    # 2. ACT: Sätt in data
    cursor.execute("INSERT INTO users (name) VALUES ('Lisa')")
    conn.commit()

    # 3. ASSERT: Hämta och kontrollera data
    cursor.execute("SELECT name FROM users WHERE id = 1")
    result = cursor.fetchone()

    assert result[0] == "Lisa"

    # 4. TEARDOWN: Stäng anslutningen manuellt
    conn.close()


def test_database_is_empty_initially():
    # Ny anslutning betyder en ny tom databas
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    assert len(result) == 0
    conn.close()