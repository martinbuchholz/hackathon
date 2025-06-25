from datetime import datetime
from fastapi import FastAPI, HTTPException
from .models import RoomCreate, Room, BookingCreate, Booking
from .service import RoomService, BookingService

app = FastAPI(title="Meeting Room Booking API")

@app.post("/rooms", response_model=Room)
def create_room(room: RoomCreate):
    room_id = RoomService.create_room(room.name)
    return Room(id=room_id, **room.dict())

@app.get("/rooms", response_model=list[Room])
def list_rooms():
    rooms = RoomService.list_rooms()
    return [Room(**r) for r in rooms]

@app.post("/bookings", response_model=Booking)
def create_booking(b: BookingCreate):
    try:
        bid = BookingService.create_booking(b.room_id, b.title, b.start, b.end)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return Booking(id=bid, **b.dict())

@app.get("/bookings", response_model=list[Booking])
def list_bookings():
    bookings = BookingService.list_bookings()
    # convert ISO strings to datetime
    result = []
    for row in bookings:
        row['start'] = datetime.fromisoformat(row['start'])
        row['end'] = datetime.fromisoformat(row['end'])
        result.append(Booking(**row))
    return result
