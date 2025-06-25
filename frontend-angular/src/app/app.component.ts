import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Room { id: number; name: string; }
interface Booking { id: number; title: string; start: string; end: string; room: Room; }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent implements OnInit {
  rooms: Room[] = [];
  bookings: Booking[] = [];
  form = { roomId: 0, title: '', start: '', end: '' };

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.loadRooms();
    this.loadBookings();
  }

  loadRooms() {
    this.http.get<Room[]>('/rooms').subscribe(r => this.rooms = r);
  }

  loadBookings() {
    this.http.get<Booking[]>('/bookings').subscribe(b => this.bookings = b);
  }

  addRoom(name: string) {
    this.http.post<Room>('/rooms', { name }).subscribe(() => this.loadRooms());
  }

  createBooking() {
    this.http.post<Booking>('/bookings', {
      roomId: this.form.roomId,
      title: this.form.title,
      start: this.form.start,
      end: this.form.end
    }).subscribe({
      next: () => this.loadBookings(),
      error: err => alert(err.error.detail)
    });
  }
}
