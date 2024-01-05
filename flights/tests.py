from django.test import Client, TestCase
from .models import Flight, AirPort

# Create your tests here.


class FlightTestCase(TestCase):

    def setUp(self):
        # Crear instancias de AirPort para utilizar en las pruebas
        airport1 = AirPort.objects.create(code="AAA", city="Airport A")
        airport2 = AirPort.objects.create(code="BBB", city="Airport B")

        # Crear instancias de Flight para utilizar en las pruebas
        self.flight_valid = Flight.objects.create(
            origin=airport1,
            destination=airport2,
            duration=2,
            state=False
        )

        self.flight_invalid = Flight.objects.create(
            origin=airport1,
            destination=airport1,  # Destino igual al origen, debería ser inválido
            duration=0,  # Duración negativa, debería ser inválido
            state=False
        )

        self.flight_invalid_self_airport = Flight.objects.create(
            origin=airport1,
            destination=airport1,  # Destino igual al origen, debería ser inválido
            duration=5,  # Duración negativa, debería ser inválido
            state=False
        )


    def test_is_valid_flight_valid(self):
        self.assertTrue(self.flight_valid.is_valid_flight())

    def test_is_valid_flight_invalid(self):
        self.assertFalse(self.flight_invalid.is_valid_flight())

    
    def test_is_valid_flight_self_airport_invalid(self):
        self.assertFalse(self.flight_invalid_self_airport.is_valid_flight())

    
    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.context["flights"].count(),3 )
    