from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.views import AirplaneViewSet, FlightViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'airplanes', AirplaneViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include API endpoints here
]
