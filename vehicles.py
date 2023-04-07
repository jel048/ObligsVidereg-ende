
class Vehicle:
    def __init__(self, merke, arsModell, kmStand, pris, registreringsNr):
        self.merke = merke
        self.arsModell = arsModell
        self.kmStand = kmStand
        self.pris = pris
        self.registreringsNr = registreringsNr
        self.speedingTickets = []
    def get_make(self):
        return self.merke
    
    def set_make(self, make):
        self.merke = make
        
    
    def get_mileage(self):
        return self.kmStand
    
    def set_mileage(self, mileage):
        self.kmStand = mileage
    
    def get_model(self):
        return self.arsModell
    
    def set_model(self, model):
        self.arsModell = model
    
    def get_price(self):
        return self.pris
    
    def set_price(self, price):
        self.pris = price
    
    def get_licence(self):
        return self.registreringsNr
    
    def set_licence(self, licence):
        self.registreringsNr = licence
    
    def set_speedingTicket(self, ticket):
        self.speedingTickets.append(ticket)
        
    def get_speedingTickets(self):
        return self.speedingTickets
    
    def print_speedingTickets(self):
        for ticket in self.speedingTickets:
            print(ticket)
    
    
        
    def __str__(self):
        return f'Make: {self.merke} \nModel: {self.arsModell} \n\
Mileage: {self.kmStand} Km\nPrice: {self.pris} Kr\nLicence: {self.registreringsNr}'
    
class Car(Vehicle):
    def __init__(self, merke, arsModell, kmStand, pris, registreringsNr, doors):
        super().__init__(merke, arsModell, kmStand, pris, registreringsNr)
        self.doors = doors
        
    def get_doors(self):
        return self.doors
    
    def set_doors(self, doors):
        self.doors = doors
        
    def __str__(self):
        return super().__str__() + f'\nDoors: {self.doors}\n\n'
    
class Truck(Vehicle):
    def __init__(self, merke, arsModell, kmStand, pris, registreringsNr, driveType):
        super().__init__(merke, arsModell, kmStand, pris, registreringsNr)
        self.driveType = driveType
        
    def get_driveType(self):
        return self.driveType
    
    def set_driveType(self, driveType):
        self.driveType = driveType
    
    def __str__(self):
        return super().__str__() + f'\nDrive type: {self.driveType} WD\n\n'
    
    
class SUV(Vehicle):
    def __init__(self, merke, arsModell, kmStand, pris, registreringsNr, passCap):
        super().__init__(merke, arsModell, kmStand, pris, registreringsNr)
        self.passCap = passCap
        
    def get_passCap(self):
        return self.passCap
    
    def set_passCap(self, passCap):
        self.passCap = passCap
    
    def __str__(self):
        return super().__str__() + f'\nPassenger capacity: {self.passCap}\n\n'
    
    
class speedTicket:
    def __init__(self, licence, time, speed, speedLimit):
        self.licence = licence
        self.time = time
        self.speed = speed
        self.speedLimit = speedLimit
        
        
    def get_licence(self):
        return self.licence
    
    def get_time(self):
        return self.time
    
    def get_speed(self):
        return self.speed
    
    def get_speedLimit(self):
        return self.speedLimit
    
    def __str__(self):
        return f'Licence number: {self.licence}\nTime: {self.time}\nSpeed: {self.speed}\nSpeed Limit: {self.speedLimit}\n'