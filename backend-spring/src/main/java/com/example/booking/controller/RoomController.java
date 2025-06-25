package com.example.booking.controller;

import com.example.booking.entity.Room;
import com.example.booking.service.RoomService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/rooms")
public class RoomController {
    private final RoomService service;

    public RoomController(RoomService service) {
        this.service = service;
    }

    @PostMapping
    public Room createRoom(@RequestBody Room room) {
        return service.createRoom(room.getName());
    }

    @GetMapping
    public List<Room> listRooms() {
        return service.listRooms();
    }
}
