from django.contrib import admin

from flights.models import AirPort, Flight, Passenger

# Register your models here.

class AirPortAdmin(admin.ModelAdmin):
    list_display=("id","code", "city" )

class FlightAdmin ( admin.ModelAdmin ):
    list_display =("id","origin", "destination", "duration")

class PassengerAdmin ( admin.ModelAdmin ):
    filter_horizontal = ("flights", )

admin.site.register(AirPort, AirPortAdmin)
admin.site.register(Flight, FlightAdmin)
#admin.site.register(Flight)
admin.site.register(Passenger, PassengerAdmin)