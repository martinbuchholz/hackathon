import os
import unittest
from datetime import datetime, timedelta

# ensure fresh DB
if os.path.exists('booking.db'):
    os.remove('booking.db')

from backend.database import init_db
from backend.service import RoomService, BookingService

class BookingServiceTest(unittest.TestCase):
    def setUp(self):
        # start with a fresh database for each test
        if os.path.exists('booking.db'):
            os.remove('booking.db')
        init_db()
        self.room_id = RoomService.create_room('Room A')

    def test_no_overlap(self):
        start = datetime.now()
        end = start + timedelta(hours=1)
        booking_id = BookingService.create_booking(self.room_id, 'Meeting', start, end)
        self.assertIsNotNone(booking_id)

    def test_overlap(self):
        start = datetime.now()
        end = start + timedelta(hours=1)
        BookingService.create_booking(self.room_id, 'First', start, end)
        with self.assertRaises(ValueError):
            BookingService.create_booking(self.room_id, 'Overlap', start + timedelta(minutes=30), end + timedelta(minutes=30))

if __name__ == '__main__':
    unittest.main()
