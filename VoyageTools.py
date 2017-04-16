# ------------------------------------------------------------
# VoyageTools.py
# ------------------------------------------------------------
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
    'OH': 'Cleveland, OH'
}

def createpackage(lastname, name):
    return "creating package..."


def destinations():
   # return "displaying destinations..."
   print "displaying destinations"
   for x in places:
    print (x, ':', places[x])

def flights(destination, date1, date2):
    return "displaying flights to given destination on given dates..."


def fly(destination, airline):
    return "reserving flight to destination through given airline..."


def hotels(destinations):
    return "displaying available hotels in destination..."


# param could be hotel or rental
def reserve(reservation):
    return "reserving hotel/car..."


def cars(destination):
    return "displaying available car rentals in destination..."


def tours(destination):
    return "displaying available tours on given destination..."


# tours is a list of places to visit
def visit(tours):
    return "reserve tour(s) on given destination..."


def book():
    return "complete package reservation..."
