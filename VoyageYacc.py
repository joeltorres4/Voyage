
# ------------------------------------------------------------
# VoyageYacc.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from VoyageLex import tokens

# Import intermediate code module here
import VoyageTools

# Primary reduce statement
def p_statement(p):
    '''statement :  statement_createpackage
                  | statement_destinations
                  | statement_flights
                  | statement_fly
                  | statement_hotels
                  | statement_reserve
                  | statement_stay
                  | statement_cars
                  | statement_tours
                  | statement_visit
                  | statement_book'''
    p[0] = p[1]
    pass


def p_statement_createpackage(p):
    'statement_createpackage : CREATEPACKAGE NAME NAME'
    res = VoyageTools.createpackage(p[2], p[3])
    print(res)


def p_statement_destinations(p):
    'statement_destinations : DESTINATIONS'
    res = VoyageTools.destinations()
    print(res)


def p_statement_flights(p):
    'statement_flights : FLIGHTS DESTINATION DATE DATE'
    res = VoyageTools.flights(p[2], p[3], p[4])
    print(res)


def p_statement_fly(p):
    'statement_fly : FLY DESTINATION AIRLINE'
    res = VoyageTools.fly(p[2], p[3])
    print(res)


def p_statement_hotels(p):
    'statement_hotels : HOTELS DESTINATION'
    res = VoyageTools.hotels(p[2])
    print(res)


def p_statement_reserve(p):
    'statement_reserve : RESERVE RENTAL DAYS'
    res = VoyageTools.reserve(p[2], p[3])
    print(res)


def p_statement_stay(p):
    'statement_stay : STAY HOTEL'
    res = VoyageTools.stay(p[2])
    print(res)


def p_statement_cars(p):
    'statement_cars : CARS DESTINATION'
    res = VoyageTools.cars(p[2])
    print(res)


def p_statement_tours(p):
    'statement_tours : TOURS DESTINATION'
    res = VoyageTools.tours(p[2])
    print(res)


def p_statement_visit(p):
    'statement_visit : VISIT DESTINATION TOUR'
    res = VoyageTools.visit(p[2], p[3])
    print(res)


def p_statement_book(p):
    'statement_book : BOOK'
    res = VoyageTools.book()
    print(res)


# ------------------------------------------------------------
# statement for error handling.
# ------------------------------------------------------------
def p_error(p):
    #print("Syntax error in input!")
    print("Syntax error at '%s'" % repr(p))  # p.value)

# Build the parser
parser = yacc.yacc()
