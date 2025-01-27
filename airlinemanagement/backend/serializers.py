from rest_framework import serializers
from .models import Airplane, Flight, Reservation

# Serializers
class AirplaneSerializer(serializers.ModelSerializer):
    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Capacity must be a positive integer.")
        return value

    def validate_production_year(self, value):
        if value < 1903:  # First airplane invented in 1903
            raise serializers.ValidationError("Production year must be after 1903.")
        return value

    class Meta:
        model = Airplane
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['departure'] == data['destination']:
            raise serializers.ValidationError("Departure and destination cannot be the same.")
        if data['departure_time'] >= data['arrival_time']:
            raise serializers.ValidationError("Departure time must be before arrival time.")
        return data

    class Meta:
        model = Flight
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    def validate_passenger_email(self, value):
        if not value or '@' not in value:
            raise serializers.ValidationError("A valid email address is required.")
        return value

    class Meta:
        model = Reservation
        fields = '__all__'