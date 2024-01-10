#from flights.models import Flight
from flights.models import AirPort, Flight
from rest_framework import serializers

#class FlightSerializer(serializers.ModelSerializer):

    #class Meta:
    #    model = Flight
    #    fields = ('origin', 'destination', 'duration')

class AirPortSerializer(serializers.Serializer):
    code = serializers.CharField()
    city = serializers.CharField()

class FlightSerializer(serializers.Serializer):
    origin = AirPortSerializer()
    destination = AirPortSerializer()
    duration = serializers.IntegerField() 

class CreateFlightSerializer(serializers.Serializer):
    ''' create Fligh Serializer'''
    origin = serializers.PrimaryKeyRelatedField(queryset=AirPort.objects.all())
    destination = serializers.PrimaryKeyRelatedField(queryset=AirPort.objects.all())
    duration = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        return Flight.objects.create(**validated_data)
