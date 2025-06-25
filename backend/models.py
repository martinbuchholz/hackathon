from pydantic import BaseModel
from datetime import datetime

class RoomCreate(BaseModel):
    name: str

class Room(RoomCreate):
    id: int

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    room_id: int
    title: str
    start: datetime
    end: datetime

class Booking(BookingCreate):
    id: int

    class Config:
        orm_mode = True
