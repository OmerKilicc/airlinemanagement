from django.contrib import admin
from .models import Airplane,Flight,Reservation

# Register your models here.
modelsToRegister = [Airplane,Flight,Reservation]
admin.site.register(modelsToRegister)