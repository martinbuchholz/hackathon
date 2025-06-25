# Hackathon Meeting Room Booking Tool

This project is a minimal MVP for reserving meeting rooms.

## Backend

* Python **FastAPI** with an SQLite database (file `booking.db`).
* Basic CRUD endpoints for rooms and bookings.
* Booking creation prevents overlapping bookings in the same room.

Start the API:

```bash
python3 -m uvicorn backend.main:app --reload
```

API docs are available at `http://localhost:8000/docs`.

## Frontend

A simple HTML/JavaScript page is located in `frontend/index.html`.
Open it in your browser after starting the backend. It calls the API to list
and create rooms and bookings.

## Tests

Run unit tests with:

```bash
python3 -m pytest -q
```
