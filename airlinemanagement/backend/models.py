import string
import random
from django.core.mail import send_mail
from django.db import models
from rest_framework.exceptions import ValidationError

class Airplane(models.Model):
    tail_number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tail_number} ({self.model})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')

    def __str__(self):
        return f"Flight {self.flight_number}: {self.departure} -> {self.destination}"

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=20, unique=True, editable=False)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            self.reservation_code = self.generate_reservation_code()
        # Check flight occupancy
        if self.flight.reservations.filter(status=True).count() >= self.flight.airplane.capacity:
            raise ValidationError("The flight is fully booked.")
        super().save(*args, **kwargs)
        # Send confirmation email
        self.send_confirmation_email()

    @staticmethod
    def generate_reservation_code(length=5):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=length))

    def send_confirmation_email(self):
        subject = f"Reservation Confirmation: {self.reservation_code}"
        message = (
            f"Dear {self.passenger_name},\n\n"
            f"Your reservation has been successfully created.\n"
            f"Reservation Code: {self.reservation_code}\n"
            f"Flight Details: {self.flight.flight_number} from {self.flight.departure} to {self.flight.destination}\n"
            f"Departure: {self.flight.departure_time}\n"
            f"Arrival: {self.flight.arrival_time}\n\n"
            "Thank you for choosing our service."
        )
        send_mail(subject, message, 'no-reply@airline.com', [self.passenger_email])

    def __str__(self):
        return f"Reservation {self.reservation_code} for {self.passenger_name}"
