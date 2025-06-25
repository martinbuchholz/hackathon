# Hackathon Meeting Room Booking Tool

This repository contains a minimal meeting room booking application. Two implementations of the backend are provided:

* **Python FastAPI** (directory `backend`)
* **Java Spring Boot** (directory `backend-spring`)

A simple Angular prototype is available in `frontend-angular` in addition to the plain HTML example in `frontend`.

## Python Backend

* FastAPI with SQLite database (`booking.db`).
* Basic CRUD endpoints for rooms and bookings.
* Booking creation prevents overlapping bookings in the same room.

Run the API:

```bash
python3 -m uvicorn backend.main:app --reload
```

API docs are available at `http://localhost:8000/docs`.

## Spring Boot Backend

The Spring Boot variant uses an in-memory H2 database.

Run it with Maven:

```bash
cd backend-spring
mvn spring-boot:run
```

## Angular Frontend

A simple Angular client resides in `frontend-angular`.
After installing the dependencies you can start it with:

```bash
cd frontend-angular
npm install
npm start
```

## Tests

Python unit tests are located in `tests` and can be executed with:

```bash
python3 -m pytest -q
```
