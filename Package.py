
class Package:
    def __init__(self):
        self.name = ""
        self.lastName = ""
        self.destination = ""
        self.flight = ""
        self.date1 = ""
        self.date2 = ""
        self.totalNight = 0
        self.hotel = ""
        self.price = 0
        self.car = ""
        self.tours = []

    def create(self,name, lastName):
        self.name = name
        self.lastName = lastName

    def dest(self, destination):
        self.destination = destination

    def flight(self, flight):
        self.flight = flight

    def date(self,date1,date2):
        self.date1 = date1
        self.date2 = date2

    def hotel(self,hotel, price):
        self.hotel = hotel
        self.price = price

    def car(self, car):
        self.car = car

    def tours(self,tour):
        self.tours.append(tour)

    def summary(self):
        print("Name: " + self.name + " " + self.lastName)
        print("Destination: " + self.destination)
        #print("Flight: ")
