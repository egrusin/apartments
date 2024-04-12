from django.test import TestCase
from .models import MultistoreyBuilding, session


class ModelTest(TestCase):
    def setUp(self):
        self.building = MultistoreyBuilding(
            id=1000,
            fias_code="12345",
            wall_material="Dark Oak",
            year_built=2020,
            area=36.6,
            apartments_count=1
        )
        session.add(self.building)
        session.commit()

    def test_apartment_creation(self):
        apartment = MultistoreyBuilding.get(1000)
        self.assertEqual(apartment.fias_code, "12345")
        self.assertEqual(apartment.wall_material, "Dark Oak")
        self.assertEqual(apartment.year_built, 2020)
        self.assertEqual(apartment.area, 36.6)
        self.assertEqual(apartment.apartments_count, 1)

    def tearDown(self):
        session.delete(self.building)
        session.commit()
