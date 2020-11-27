from vehicle import *
import argparse
import sys

if sys.version_info[0] == 2:
    input = raw_input

class Parking:
    def __init__(self):
        self.max_parking = 0
        self.slot_number = 0
        self.already_parked_slots = 0

    def make_parking_lot(self,max_parking):
        self.slots = [-1] * max_parking
        self.max_parking = max_parking
        return self.max_parking

    def empty_slots(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self,registration_number,car_colour):
        if self.already_parked_slots < self.max_parking: 
            slot_number = self.empty_slots()
            self.slots[slot_number] = Car(registration_number,car_colour)
            self.slot_number = self.slot_number+1
            self.already_parked_slots = self.already_parked_slots + 1
            return slot_number+1
        else:
            return -1

    def car_exiting_from_parking(self,slot_number):

        if self.already_parked_slots > 0 and self.slots[slot_number-1] != -1:
            self.slots[slot_number-1] = -1
            self.already_parked_slots = self.already_parked_slots - 1
            return True
        else:
            return False

    def slot_status(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1) + "\t\t" +str(self.slots[i].registration_number) + "\t\t" + str(self.slots[i].car_colour))
            else:
                continue

    def get_registration_number_by_colour(self,car_colour):

        registration_number = []

        if self.max_parking ==0:
            print("Sorry No parking lot is created yet ")

        else:
            for i in self.slots:
                
                if i == -1:
                    continue

                if i.car_colour == car_colour:
                    registration_number.append(i.registration_number)

            return registration_number
                
    def parking_slot_number_by_car_registration(self,registration_number):

        if self.max_parking == 0:
            return -1
        
        else:

            for i in range(len(self.slots)):
                if self.slots[i].registration_number == registration_number:
                    return i+1
                else:
                    continue
            return -1
            

    def parking_slot_info_by_car_colour(self,car_colour):
        
        slot_number = []

        if self.slot_number == 0:
            return -1
        
        else:

            for i in range(len(self.slots)):

                if self.slots[i] == -1:
                    continue

                if self.slots[i].car_colour == car_colour:
                    slot_number.append(str(i+1))
            return slot_number

    def show(self,line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.make_parking_lot(n)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            registration_number = line.split(' ')[1]
            car_colour = line.split(' ')[2]
            res = self.park(registration_number,car_colour)
            if res == -1:
                print("Sorry, The parking lot is full")
            else:
                print('Slot Allocated for car : '+str(res))

        elif line.startswith('car_exiting_from_parking'):
            car_exiting_slot_vacated = int(line.split(' ')[1])
            parking_slot_status = self.car_exiting_from_parking(car_exiting_slot_vacated)
            if parking_slot_status:
                print('Slot number '+str(car_exiting_slot_vacated)+' is free')
            else: 
                print("slot is already empty, Cant perform exit command. please provide only parked car input")

        elif line.startswith('parking_slot_status'):
            self.parking_slot_status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            car_colour = line.split(' ')[1]
            registration_number = self.get_registration_number_by_colour(car_colour)
            print(', '.join(registration_number))

        elif line.startswith('slot_numbers_for_cars_with_colour'):

            car_colour = line.split(' ')[1]

            if self.parking_slot_info_by_car_colour(car_colour):
                print("Sorry no provided colour car is parked yet")
            else:
                slot_number = self.parking_slot_info_by_car_colour(car_colour)
                print(', '.join(slot_number))
            

        elif line.startswith('slot_number_for_registration_number'):
            registration_number = line.split(' ')[1]
            slot_number = self.parking_slot_number_by_car_registration(registration_number)
            if slot_number == -1:
                print("Not found")
            else:
                print(slot_number)
        elif line.startswith('exit'):
            exit(0)

def main():

    parkinglot = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()
    
    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parkinglot.show(line)
    else:
            while True:
                line = input("$ ")
                parkinglot.show(line)

if __name__ == '__main__':
    main()