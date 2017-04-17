# ------------------------------------------------------------
# VoyageTools.py
# ------------------------------------------------------------
import Package

package = Package.Package()
record = open("record.txt", "w")

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

airlines = {
    'AA': "American Airlines",
    'UA': 'United Airlines',
    'JB': 'Jet Blue',
    'DA': 'Delta Airlines',
    'CA': 'Continental Airlines',
    'SA': 'Southwest Airlines',
}

hotel = {
    'Best Western': ['NY', 'OH', 'TN', 'CA', 'TX', 'FL'],
    'Marriott': ['NY', 'CA', 'TX', 'MA', 'NV', 'FL'],
    'Holiday Inn': ['NY', 'WA', 'GA', 'OH', 'DC'],
    'Hilton': ['MA', 'TX', 'NY', 'WA', 'CA', 'TX'],
    'Sheraton': ['NY', 'MA', 'TX', 'FL', 'DC', 'CA', 'TN'],
}

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

listTours = {
    'NY':{'Statue of Liberty':'$57.00','Empire State Building':'$34.00','9/11 Memorial Museum':'$24.00'},
    'FL':{'Universal Studios Theme Park':'$125.00','Kennedy Space Center':'$54.00','Florida Everglades':'$25.00'},
    'NV':{'Cirque du Soleil':'$145.00','Grand Canyon National Park':'$78.00','Titanic: The Artifact Exhibition':'$38.00'},
    'CA':{'Hollywood Strip Helicopter Flight':'$200.00','Griffith Observatory':'$50.00','Legends of Hollywood':'$80.00'},
    'TX':{'Dallas Attraction Tours':'$25.00','The George W. Bush Presidential Library and Museum':'$48.00','Dallas City Pass':'$50.00'},
    'MA':{'Fenway Park Tour':'$30.00','Museum of Fine Arts':'$25.00','Cambridge, Lexington and Cocord':'$48.00'},
    'DC':{'Mount Vernon and Arlington National Cementery':'$105.00','Smithsonian National Air and Museum':'$25.00','Fords Theater':'$20.00'},
    'WA':{'Museum of Flight':'$21.00','Space Needle':'$25.00','Boeing Factory Tour':'$40.00'},
    'TN':{'Elvis Presley Graceland VIP Tour':'$90.00','National Civil Rights Museum':'$35.00','Sun Studio Tour':'$24.00'},
    'GA':{'Georgia Aquarium':'$44.00','CNN Atlanta Studio Tour':'$16.00','World of Coca Cola':'$20.00'},
    'OH':{'Rock and Roll Hall of Fame':'$25.00','Cleveland Museum of Art':'$30.00','USS Cod Submarin Memorial':'$15.00'}
}

def createpackage(name, lastname):
    global package
    package = Package.Package()
    package.create(name, lastname)
    return "creating package for " + name + " " + lastname


def destinations():
    dest = "\n"
    for values in places:
        dest = dest + places[values] + "\n"
    return dest


def flights(destination, date1, date2):
    global package
    package.date(date1, date2)
    try:
        ticket = flight.get(destination)
        for x, y in ticket.items():
            print(airlines[x], y)
    except:
        return "invalid location"


def fly(destination, airline):
    global package
    try:
        package.dest(places[destination])
    except:
        return "invalid destination"

    try:
        flight[destination][airline]
        package.airline(airlines[airline])
    except:
        return "invalid airline"
    return "reserving flight to " + places[destination] + " with " + airlines[airline]


def hotels(destinations):
    hot = "\n"
    for key, value in hotel.items():
        if destinations in value:
            hot = hot + key + "\n"
    return hot  # param could be hotel or rental


def reserve(reservation, days):
    return "reserving " + reservation + " for " + repr(days) + "days"


def cars(destination):
    return "displaying available car rentals in destination..."


def tours(destination):
    global package
    try:
        list = listTours[destination]
        for x,y in list.items():
            print(x,y)
    except:
        print("invalid location")
    return "\n"


# tours is a list of places to visit
def visit(tour):
    return "reserve tour(s) on given destination..."


def book():
    global package
    if not package.flight == "":
        # Save package summary to file
        record.write(package.summary()+"\n")
        # Print package summary to console
        return package.summary()
    else:
        return "Client package not complete"
