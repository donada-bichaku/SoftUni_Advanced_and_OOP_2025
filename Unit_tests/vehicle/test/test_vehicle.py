from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 80.5)

    def test_correct_init(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(80.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_should_reduce_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(18.0, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(40)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_amount_of_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(20.5)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_correct_string_is_returned_for_instance_of_class_printed(self):
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption", f"{self.vehicle}")

if __name__=="__main__":
    main()