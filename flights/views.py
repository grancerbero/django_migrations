from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from flights.models import AirPort, Flight, Passenger
from flights.serializers import CreateFlightSerializer, FlightSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


# Create your views here.
def  index (request):
    return render(request, "flights/index.html", {
                  "flights": Flight.objects.all()
                  })

def flight( request, flight_id ):
    flight = Flight.objects.get(pk = flight_id)
    return render (request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude( flights=flight).all()
    }  )

def book(request, flight_id):
    if  request.method == "POST":
        flight = Flight.objects.get( pk=flight_id )
        passenger =  Passenger.objects.get ( pk = int (request.POST ["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect( reverse("flight", args=(flight.id,  )  ) )
    

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def listFlightsV1(request):
    flights= Flight.objects.all()
    data =[]
    for flight in flights:
        data.append({
            'origin': flight.origin.code,
            'destination': flight.destination.code ,
            'duration': flight.duration
        })
    return Response( data) 


@api_view(['GET'])
def listFlightsV2(request):
    flights= Flight.objects.all()
    data =[]
    for flight in flights:
        data.append(FlightSerializer(flight).data )
    return Response(data)


@api_view(['GET'])
def listFlightsV3(request):
    flights= Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def createFlightV1(request):
    """create Flight"""
   # import ipdb; ipdb.set_trace()
    origin=request.data['origin']
    destination=request.data['destination']
    duration = request.data['duration']
    
    airPort1 = AirPort.objects.get(id=origin)
    airPort2 = AirPort.objects.get(id=destination)
    fligth =Flight.objects.create( origin=airPort1, destination=airPort2, duration= duration )
    serializer = FlightSerializer(fligth)
    return Response(serializer.data)



@api_view(['POST'])
def createFlightV2(request):
    """create Flight"""
   # import ipdb; ipdb.set_trace()
    serializer = CreateFlightSerializer( data = request.data )
   # import ipdb; ipdb.set_trace()
    serializer.is_valid (raise_exception = True)
    fligth = serializer.save()
    return Response( FlightSerializer(fligth).data   )






