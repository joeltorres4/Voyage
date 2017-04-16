# ------------------------------------------------------------
# VoyageTools.py
# ------------------------------------------------------------
import Package

package = Package()
places = {
    'NY': 'New York City, NY',
    'FL': 'Orlando, FL',
    'NV': 'Las Vegas, NV',
    'CA': 'Los Angeles, CA',
    'TX': 'Dallas, TX',
    'MA': 'Boston, MA',
    'NC': 'Charlotte, NC',
    'WA': 'Seattle, WA',
    'TN': 'Memphis, TN',
    'GA': 'Atlanta, GA',
    'OH': 'Cleveland, OH',
}

airlines = {
    'AA': 'American Airlines',
    'UA': 'United Airlines',
    'JB': 'Jet Blue',
    'DA': 'Delta Airlines',
    'CA': 'Continental Airlines',
    'SA': 'Southwest Airlines',
}

hotel = {
    'Best Western': ['NY', 'OH', 'TN', 'CA', 'TX', 'FL'],
    'Marriott': ['NY', 'CA', 'TX', 'MA', 'NV', 'FL'],
    'Holiday Inn': ['NY', 'WA', 'GA', 'OH', 'NC'],
    'Hilton': ['MA', 'TX', 'NY', 'WA', 'CA', 'TX'],
    'Sheraton': ['NY', 'MA', 'TX', 'FL', 'NC', 'CA', 'TN'],
}

flight = {
    'NY': {
        'AA': "$450",
        'UA': "$400"
    },
    'FL': {

    },
    'NV': {

    },
    'CA': {

    },
    'TX': {

    },
    'MA': {

    },
    'NC': {

    },
    'WA': {

    },
    'TN': {

    },
    'GA': {

    },
    'OH': {

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
    package.date(date1, date2)
    try:
        ticket = flight[destination]
        for z in ticket:
            print(airlines[z] + " " + ticket[z])
    except:
        return "invalid location"


def fly(destination, airline):
    return "reserving flight to " + destination + " with " + airline


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
    return "complete package reservation..."
