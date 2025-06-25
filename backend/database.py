import sqlite3
from contextlib import contextmanager

DB_PATH = 'booking.db'

def init_db():
    """Create tables if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            start DATETIME NOT NULL,
            end DATETIME NOT NULL,
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        );
        """
    )
    conn.commit()
    conn.close()

# initialize at import
init_db()

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
