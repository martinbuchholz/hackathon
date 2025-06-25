package com.example.booking.controller;

import com.example.booking.entity.Booking;
import com.example.booking.entity.BookingDTO;
import com.example.booking.service.BookingService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/bookings")
public class BookingController {
    private final BookingService service;

    public BookingController(BookingService service) {
        this.service = service;
    }

    @PostMapping
    public Booking createBooking(@RequestBody BookingDTO dto) {
        return service.createBooking(dto.getRoomId(), dto.getTitle(), dto.getStart(), dto.getEnd());
    }

    @GetMapping
    public List<Booking> listBookings() {
        return service.listBookings();
    }
}
