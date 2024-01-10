from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("hello", views.hello_world, name="hello"),
    path("listFlightsV1", views.listFlightsV1 , name="listFlightsV1"),
    path("listFlightsV2", views.listFlightsV2 , name="listFlightsV2"),
    path("listFlightsV3", views.listFlightsV3 , name="listFlightsV3"),
    path("createFlightV1", views.createFlightV1 , name="createFlightV1"),
    path("createFlightV2", views.createFlightV2 , name="createFlightV2")
    
]