package com.example.booking;

import com.example.booking.service.BookingService;
import com.example.booking.service.RoomService;
import com.example.booking.entity.Booking;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.context.annotation.Import;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

@DataJpaTest
@Import({BookingService.class, RoomService.class})
class BookingServiceTest {
    @Autowired
    BookingService bookingService;
    @Autowired
    RoomService roomService;

    @Test
    void testOverlap() {
        var room = roomService.createRoom("Room A");
        LocalDateTime start = LocalDateTime.now();
        LocalDateTime end = start.plusHours(1);
        Booking b1 = bookingService.createBooking(room.getId(), "First", start, end);
        assertNotNull(b1.getId());
        assertThrows(IllegalArgumentException.class, () ->
                bookingService.createBooking(room.getId(), "Overlap", start.plusMinutes(30), end.plusMinutes(30)));
    }
}
