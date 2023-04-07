# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import gjennomsnittsmåling
import pickle
# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
CHECK_SPEED_TICKETS = 6
QUIT_CHOICE = 7

FILENAME1 = "box_a.txt"
FILENAME2 = "box_b.txt"
speedingTickets = gjennomsnittsmåling.listSpeeders(FILENAME1, FILENAME2, 60, 5)

def main():
    FILENAME = 'vehicles.p'
    
        
    
    # Create empty list for vehicles
    vehicles_list = load_vehicles(FILENAME)
   

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = get_choice()

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Add a new car')
            print('Input car data: ')
            make = input('Make: ')
            year = input('Year: ')
            mileage = input('Mileage: ')
            price = input('Price: ')
            doors = input('Doors: ')
            registreringsNr = input("Licence Plate: ")
            car = vehicles.Car(make, year, mileage, price, registreringsNr, doors)
            vehicles_list.append(car)
        elif choice == NEW_TRUCK_CHOICE:
            print('Add a new truck')
            print('Input truck data: ')
            make = input('Make: ')
            year = input('Year: ')
            mileage = input('Mileage: ')
            price = input('Price: ')
            driveType = input('Drive type: ')
            registreringsNr = input("Licence Plate: ")
            truck = vehicles.Truck(make, year, mileage, price, registreringsNr, driveType)
            vehicles_list.append(truck)
        elif choice == NEW_SUV_CHOICE:
            print('Add a new SUV')
            print('Input SUV data: ')
            make = input('Make: ')
            year = input('Year: ')
            mileage = input('Mileage: ')
            price = input('Price: ')
            passCap = input('Passenger Capacity: ')
            registreringsNr = input("Licence Plate: ")
            SUV = vehicles.SUV(make, year, mileage, price, registreringsNr, passCap) 
            vehicles_list.append(SUV)
        elif choice == FIND_VEHICLE_CHOICE:
            make = input("Find vehicle by make: ")
            print('\n')
            find_vehicles(vehicles_list, make)
            
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:\n')
            for item in vehicles_list:
                print(item)
        elif choice == CHECK_SPEED_TICKETS:
            checkSpeedingTickets(speedingTickets, vehicles_list)
            for car in vehicles_list:
                car.print_speedingTickets()
                
        elif choice == QUIT_CHOICE:
            save_vehicles(FILENAME, vehicles_list)
            print('Exiting the program...')    
        else:
            print('Error: invalid selection.')    

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Check Speeding Tickets')
    print('7) Quit')    

def get_choice():
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Please enter your choice as an integer between 1 and 7.')
        choice = 0
    return choice
        
    
def find_vehicles(vehicles_list, make):
    for object in vehicles_list:
         if make.lower() in object.get_make().lower():
             print(object)

def load_vehicles(FILENAME):
    try:
        with open(FILENAME, 'rb') as cars:
            vehicleList = pickle.load(cars)
    except:
        vehicleList = []
    return vehicleList

def save_vehicles(FILENAME, vehicles_list):
    with open(FILENAME, 'wb') as cars:
        pickle.dump(vehicles_list, cars)

def checkSpeedingTickets(speedingTickets, vehicles_list):
    for licence, tuple in speedingTickets.items():
                for car in vehicles_list:
                    if licence == car.get_licence():
                        addTicket = True
                        for ticket in car.get_speedingTickets(): 
                            if ticket.get_time() == tuple[1]: #Sjekker om denne spesifikke speeding ticket allerede er lagret
                                addTicket = False
                        if addTicket:
                            ticket = vehicles.speedTicket(licence, tuple[1], tuple[0], tuple[2])
                            car.set_speedingTicket(ticket)
    
        
        

# Call the main function.
if __name__ == '__main__':
      main()