
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
    '''statement : statement_createpackage
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
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.createpackage(p[2], p[3])
    print(res)


def p_statement_destinations(p):
    'statement_destinations : DESTINATIONS'
    p[0] = p[1]
    res = VoyageTools.destinations()
    print(res)


def p_statement_flights(p):
    'statement_flights : FLIGHTS DESTINATION DATE DATE'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = VoyageTools.flights(p[2], p[3], p[4])
    print(res)


def p_statement_fly(p):
    'statement_fly : FLY DESTINATION AIRLINE'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.fly(p[2], p[3])
    print(res)


def p_statement_hotels(p):
    'statement_hotels : HOTELS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.hotels(p[2])
    print(res)


def p_statement_reserve(p):
    'statement_reserve : RESERVE RENTAL DAYS'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.reserve(p[2], p[3])
    print(res)


def p_statement_stay(p):
    'statement_stay : STAY HOTEL'
    p[0] = p[1] + p[2]
    res = VoyageTools.stay(p[2])
    print(res)


def p_statement_cars(p):
    'statement_cars : CARS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.cars(p[2])
    print(res)


def p_statement_tours(p):
    'statement_tours : TOURS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.tours(p[2])
    print(res)


def p_statement_visit(p):
    'statement_visit : VISIT DESTINATION TOUR'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.visit(p[2], p[3])
    print(res)


def p_statement_book(p):
    'statement_book : BOOK'
    p[0] = p[1]
    res = VoyageTools.book()
    print(res)


# ------------------------------------------------------------
# Expression for error handling.
# ------------------------------------------------------------
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
