from datetime import datetime
from .database import get_db

class RoomService:
    @staticmethod
    def create_room(name: str) -> int:
        with get_db() as db:
            cur = db.execute("INSERT INTO rooms(name) VALUES (?)", (name,))
            db.commit()
            return cur.lastrowid

    @staticmethod
    def list_rooms():
        with get_db() as db:
            cur = db.execute("SELECT id, name FROM rooms")
            return [dict(row) for row in cur.fetchall()]

class BookingService:
    @staticmethod
    def create_booking(room_id: int, title: str, start: datetime, end: datetime) -> int:
        if end <= start:
            raise ValueError("End must be after start")
        with get_db() as db:
            # check overlap
            cur = db.execute(
                """SELECT 1 FROM bookings WHERE room_id=? AND NOT (end<=? OR start>=?)""",
                (room_id, start.isoformat(), end.isoformat()),
            )
            if cur.fetchone():
                raise ValueError("Booking overlaps with existing booking")
            cur = db.execute(
                "INSERT INTO bookings(room_id, title, start, end) VALUES (?,?,?,?)",
                (room_id, title, start.isoformat(), end.isoformat()),
            )
            db.commit()
            return cur.lastrowid

    @staticmethod
    def list_bookings():
        with get_db() as db:
            cur = db.execute("SELECT * FROM bookings")
            rows = cur.fetchall()
            return [dict(row) for row in rows]
