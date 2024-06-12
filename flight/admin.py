from django.contrib import admin
from flight.models import Flight, Airport, Passenger


# Register your models here.

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)
