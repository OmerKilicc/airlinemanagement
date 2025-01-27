from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer

# ViewSets
class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=True, methods=['get'])
    def flights(self, request, pk=None):
        airplane = self.get_object()
        flights = airplane.flights.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=True, methods=['get'])
    def reservations(self, request, pk=None):
        flight = self.get_object()
        reservations = flight.reservations.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
