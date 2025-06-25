package com.example.booking.service;

import com.example.booking.entity.Room;
import com.example.booking.repository.RoomRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RoomService {
    private final RoomRepository repository;

    public RoomService(RoomRepository repository) {
        this.repository = repository;
    }

    public Room createRoom(String name) {
        Room room = new Room();
        room.setName(name);
        return repository.save(room);
    }

    public List<Room> listRooms() {
        return repository.findAll();
    }
}
