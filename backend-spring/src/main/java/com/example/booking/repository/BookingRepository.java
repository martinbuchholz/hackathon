package com.example.booking.repository;

import com.example.booking.entity.Booking;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.time.LocalDateTime;
import java.util.List;

public interface BookingRepository extends JpaRepository<Booking, Long> {
    @Query("select b from Booking b where b.room.id = :roomId and not (b.end <= :start or b.start >= :end)")
    List<Booking> findOverlap(Long roomId, LocalDateTime start, LocalDateTime end);
}
