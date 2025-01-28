from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer

class FlightFilter(filters.FilterSet):
    departure = filters.CharFilter(lookup_expr='icontains')
    destination = filters.CharFilter(lookup_expr='icontains')
    departure_time_after = filters.DateTimeFilter(field_name='departure_time', lookup_expr='gte')
    departure_time_before = filters.DateTimeFilter(field_name='departure_time', lookup_expr='lte')
    arrival_time_after = filters.DateTimeFilter(field_name='arrival_time', lookup_expr='gte')
    arrival_time_before = filters.DateTimeFilter(field_name='arrival_time', lookup_expr='lte')

    class Meta:
        model = Flight
        fields = ['departure', 'destination', 'departure_time_after', 'departure_time_before', 
                 'arrival_time_after', 'arrival_time_before']

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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightFilter

    @action(detail=True, methods=['get'])
    def reservations(self, request, pk=None):
        flight = self.get_object()
        reservations = flight.reservations.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
