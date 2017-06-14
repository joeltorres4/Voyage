# ------------------------------------------------------------
# VoyageTools.py
# ------------------------------------------------------------
import Package

# Travel package (Package) instance
travel_package = Package.Package()

# Places (destinations) dictionary
places = {
    'NY': "New York City, NY",
    'FL': 'Orlando, FL',
    'NV': 'Las Vegas, NV',
    'CA': 'Los Angeles, CA',
    'TX': 'Dallas, TX',
    'MA': 'Boston, MA',
    'DC': 'Washington D.C.',
    'WA': 'Seattle, WA',
    'TN': 'Memphis, TN',
    'GA': 'Atlanta, GA',
    'OH': 'Cleveland, OH',
}

# Airlines dictionary
airlines = {
    'AA': 'American Airlines (AA)',
    'UA': 'United Airlines (UA)',
    'JB': 'Jet Blue (JB)',
    'DA': 'Delta Airlines (DA)',
    'CA': 'Continental Airlines (CA)',
    'SA': 'Southwest Airlines (SA)',
}

# Hotels dictionary
hotels_list = {
    'BESTWESTERN': {'80.00': ['NY', 'OH', 'TN', 'CA', 'TX', 'FL']},
    'MARRIOTT': {'125.00': ['NY', 'CA', 'TX', 'MA', 'NV', 'FL']},
    'HOLIDAYINN': {'79.99': ['NY', 'WA', 'GA', 'OH', 'DC']},
    'HILTON': {'150.00': ['MA', 'TX', 'NY', 'WA', 'CA', 'TX']},
    'SHERATON': {'160.00': ['NY', 'MA', 'TX', 'FL', 'DC', 'CA', 'TN']}
}

# Flights dictionary
flight = {
    'NY': {
        'AA': 450,
        'UA': 400
    },
    'FL': {
        'JB': 175,
        'DA': 200
    },
    'NV': {
        'CA': 550,
        'SW': 575

    },
    'CA': {
        'AA': 750,
        'DA': 725
    },
    'TX': {
        'SW': 435,
        'JB': 450
    },
    'MA': {
        'CA': 350,
        'AA': 325
    },
    'DC': {
        'DA': 430,
        'UA': 450
    },
    'WA': {
        'JB': 615,
        'AA': 625
    },
    'TN': {
        'UA': 475,
        'SW': 500
    },
    'GA': {
        'JB': 300,
        'AA': 325
    },
    'OH': {
        'CA': 425,
        'DA': 450
    },
}

# Tours dictionary
listTours = {
    'NY': {'Statue of Liberty (SOL)': '57.00', 'Empire State Building (ESB)': '34.00',
           '9/11 Memorial Museum (NEMM)': '24.00'},
    'FL': {'Universal Studios Theme Park (USTP)': '125.00', 'Kennedy Space Center (KSC)': '54.00',
           'Florida Everglades (FE)': '25.00'},
    'NV': {'Cirque du Soleil (CDS)': '145.00', 'Grand Canyon National Park (GCNP)': '78.00',
           'Titanic: The Artifact Exhibition (TTAE)': '38.00'},
    'CA': {'Hollywood Strip Helicopter Flight (HELI)': '200.00', 'Griffith Observatory (GO)': '50.00',
           'Legends of Hollywood (LOH)': '80.00'},
    'TX': {'Dallas Attraction Tours (DAT)': '25.00',
           'The George W. Bush Presidential Library and Museum (BUSH)': '48.00',
           'Dallas City Pass (DCP)': '50.00'},
    'MA': {'Fenway Park Tour (FPT)': '30.00', 'Museum of Fine Arts (MFA)': '25.00',
           'Cambridge, Lexington and Cocord (CLC)': '48.00'},
    'DC': {'Mount Vernon and Arlington National Cementery (MVANC)': '105.00',
           'Smithsonian National Air and Museum (SNAM)': '25.00',
           'Fords Theater (FORD)': '20.00'},
    'WA': {'Museum of Flight (MOF)': '21.00', 'Space Needle (SN)': '25.00', 'Boeing Factory Tour (BOEING)': '40.00'},
    'TN': {'Elvis Presley Graceland VIP Tour (ELVIS)': '90.00', 'National Civil Rights Museum (NCRM)': '35.00',
           'Sun Studio Tour (SST)': '24.00'},
    'GA': {'Georgia Aquarium (GA)': '44.00', 'CNN Atlanta Studio Tour (CNN)': '16.00',
           'World of Coca Cola (COCA)': '20.00'},
    'OH': {'Rock and Roll Hall of Fame (ROCK)': '25.00', 'Cleveland Museum of Art (CMA)': '30.00',
           'USS Cod Submarine Memorial (USS)': '15.00'}
}

# Rental cars dictionary
rental_spot = {
    'Hertz': {'50.00': ['NY', 'OH', 'FL', 'CA', 'FL']},
    'Avis': {'55.00': ['NV', 'GA', 'TX', 'TN', 'MA']},
    'Enterprise': {'52.00': ['NY', 'OH', 'DC', 'MA', 'CA']},
    'Dollar': {'60.00': ['CA', 'TN', 'MA', 'WA', 'TX']},
    'Thrifty': {'49.00': ['CA', 'TX', 'TN', 'MA', 'DC', 'FL']}
}


# Creates a new travel package for client with given name
def createpackage(name, lastname):
    global travel_package
    travel_package = Package.Package()  # create new travel package
    name = name.title()
    lastname = lastname.title()
    travel_package.create(name, lastname)
    return "Travel package for " + name + " " + lastname + " created successfully!"


# Displays destinations available
def destinations():
    dest = "\n"
    for values in places:
        dest = dest + places[values] + "\n"
    return dest


# Displays available flights to given destination
# Given dates are departure date and return date
def flights(destination, date1, date2):
    global travel_package
    travel_package.date(date1, date2)
    try:
        # dictionary: airline, price
        ticket = flight.get(destination)
        # x is airline, y is price
        for info in ticket:
            print(airlines.get(info) + ", $" + repr(ticket[info]))
    except:
        return "Invalid location"


# Reserves flight for given destination through given airline
# Function assumes flights command was executed before, so date is
# already set
def fly(destination, airline):
    global travel_package
    try:
        travel_package.dest(places[destination])
    except:
        return "invalid destination"

    try:
        flight_price = float(flight.get(destination).get(airline))
        travel_package.airline(airlines[airline], flight_price)
    except:
        return "Invalid airline"
    return "Flight to " + places[destination] + " with " + airlines[airline] + " reserved successfully"


# Displays available hotels for given destination
def hotels(destination):
    try:
        if destination not in places:
            return "Invalid destination"
        for key, value in hotels_list.items():
            for key1, value1 in value.items():
                if destination in value1:
                    print(key.title() + " $" + key1 + "/night")
    except:
        print("Invalid location")


# Reserves given parameter (could be hotel or rental) for given days
def reserve(reservation, days):
    # check if hotel or car
    if reservation in hotels_list:
        hot = hotels_list.get(reservation)  # dictionary (price : locations)
        for hotel_price in hot:  # To extract key (hotel price)
            hotel_price = float(hotel_price)
            travel_package.setHotel(reservation.title(), hotel_price, int(days))
            return "Reserved " + repr(days) + " night(s) in " + reservation + " hotel for $" + repr(
                hotel_price * int(days))
    elif reservation.title() in rental_spot:
        # car rental
        for car_price in rental_spot[reservation.title()]:  # to extract key (price)
            car_price = float(car_price)
            travel_package.setCar(reservation.title(), car_price, int(days))
            return "Reserved " + repr(days) + " days with " + reservation + " car rental"
    else:
        return "Invalid reservation"


# Displays available car rentals for given destination
def cars(destination):
    # check if valid destination
    if destination not in places:
        print("Invalid destination")
        return

    # valid destination
    for company, info in rental_spot.items():
        locations = list(info.values()).pop()
        if destination in locations:
            for price in info:
                print(company + " $" + price)


# Displays available tours for given destination
def tours(destination):
    global travel_package
    try:
        destTours = listTours[destination]
        for tour_name, price in destTours.items():
            print(tour_name + " $" + price)
    except:
        print("Invalid destination")
    return "\n"


# Appends tour to current package tours list. Param tour is the tour keyword.
def visit(tour):
    # check if tour exists on current package destination
    # get current destination
    dest = travel_package.destination
    if dest == "":
        return "Package has no destination set"
    # format destination
    dest = dest[-2:]
    # try to match tour and destination on tours_list
    tours_info = listTours.get(dest)  # tour names and keywords : prices
    # get tour containing param keyword
    for tour_name in tours_info:
        if tour in tour_name:
            # reserve tour
            travel_package.setTours(tour_name, float(tours_info.get(tour_name)))
            return "Reserved " + tour_name + " tour on " + travel_package.destination
    return "Invalid tour"


def book():
    global travel_package
    if not travel_package.flight == "":
        # Save package summary to file
        record = open("record.txt", "a")
        record.write(travel_package.summary())
        record.write("--------------------------------------")
        record.close()
        # Print package summary to console
        return travel_package.summary()
    else:
        return "Package not ready to book"
