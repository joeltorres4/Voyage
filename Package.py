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

    def __call__(self, *args, **kwargs):
        return self

    def create(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def dest(self, destination):
        self.destination = destination

    def airline(self, flight, flight_price):
        self.flight = flight
        self.price += flight_price

    def date(self, date1, date2):
        self.date1 = date1
        self.date2 = date2

    def setHotel(self, hot, price, days):
        self.hotel = hot
        self.price += price * days

    def setCar(self, car, price, days):
        self.car = car
        self.price += price * days

    def setTours(self, tour, price):
        self.tours.append(tour)
        self.price += price

    def summary(self):
        return "\nName: " + self.name + " " + self.lastName + \
               "\nDestination: " + self.destination + "\nAirline: " + self.flight + \
               "\nHotel: " + self.hotel + "\nCheck-in: " + self.date1 + "\nCheck-out: " + self.date2 + \
               "\nRental Car: " + self.car + "\nTours: " + repr(self.tours) + \
               "\nTotal Price: $" + repr(self.price) + "\n"
