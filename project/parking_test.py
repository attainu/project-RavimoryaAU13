import unittest
from Parking import *
class Test_Parking(unittest.TestCase):

	def test_make_parking_lot(self):
		parking = ParkingLot()
		res = parkingLot.make_parking_lot(6)
		self.assertEqual(6,res)

	def test_park(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		self.assertNotEqual(-1,res)

	def test_car_exiting_from_parking(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.car_exiting_from_parking(1)
		self.assertEqual(True,res)

	def test_get_registration_number_by_colour(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		registration_number = parkingLot.get_registration_number_by_colour("White")
		self.assertIn("KA-01-HH-1234",registration_number)
		self.assertIn("KA-01-HH-9999",registration_number)

	def test_parking_slot_number_by_car_registration(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		slot_number = parkingLot.parking_slot_number_by_car_registration("KA-01-HH-9999")
		self.assertEqual(2,slot_number)

	def test_parking_slot_info_by_car_colour(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-9999","White")
		slot_number = parkingLot.parking_slot_info_by_car_colour("White")
		self.assertIn("1",slot_number)
		self.assertIn("2",slot_number)

if __name__ == '__main__':
	unittest.main()