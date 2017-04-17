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


def createpackage(name, lastname):
    global package
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
            print(x, y)
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
    return "displaying available tours on given destination..."


# tours is a list of places to visit
def visit(tours):
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
