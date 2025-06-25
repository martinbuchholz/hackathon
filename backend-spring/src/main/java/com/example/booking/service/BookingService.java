package com.example.booking.service;

import com.example.booking.entity.Booking;
import com.example.booking.entity.Room;
import com.example.booking.repository.BookingRepository;
import com.example.booking.repository.RoomRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class BookingService {
    private final BookingRepository bookingRepository;
    private final RoomRepository roomRepository;

    public BookingService(BookingRepository bookingRepository, RoomRepository roomRepository) {
        this.bookingRepository = bookingRepository;
        this.roomRepository = roomRepository;
    }

    public Booking createBooking(Long roomId, String title, LocalDateTime start, LocalDateTime end) {
        if (end.isBefore(start) || end.equals(start)) {
            throw new IllegalArgumentException("End must be after start");
        }
        Room room = roomRepository.findById(roomId)
                .orElseThrow(() -> new IllegalArgumentException("Room not found"));
        if (!bookingRepository.findOverlap(roomId, start, end).isEmpty()) {
            throw new IllegalArgumentException("Booking overlaps with existing booking");
        }
        Booking booking = new Booking();
        booking.setRoom(room);
        booking.setTitle(title);
        booking.setStart(start);
        booking.setEnd(end);
        return bookingRepository.save(booking);
    }

    public List<Booking> listBookings() {
        return bookingRepository.findAll();
    }
}
