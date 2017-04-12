
# ------------------------------------------------------------
# VoyageYacc.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from VoyageLex import tokens

# Import intermediate code module here
import VoyageTools

# Primary reduce expression
def p_expression(p):
    '''expression : expression_createpackage
                  | expression_destinations
                  | expression_flights
                  | expression_fly
                  | expression_hotels
                  | expression_reserve
                  | expression_stay
                  | expression_cars
                  | expression_tours
                  | expression_visit
                  | expression_book'''
    p[0] = p[1]
    pass


def p_expression_createpackage(p):
    'expression_createpackage : CREATEPACKAGE NAME NAME'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.createpackage(p[2], p[3])
    print(res)


def p_expression_destinations(p):
    'expression_destinations : DESTINATIONS'
    p[0] = p[1]
    res = VoyageTools.destinations()
    print(res)


def p_expression_flights(p):
    'expression_flights : FLIGHTS DESTINATION DATE DATE'
    p[0] = p[1] + p[2] + p[3] + p[4]
    res = VoyageTools.flights(p[2], p[3], p[4])
    print(res)


def p_expression_fly(p):
    'expression_fly : FLY DESTINATION AIRLINE'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.fly(p[2], p[3])
    print(res)


def p_expression_hotels(p):
    'expression_hotels : HOTELS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.hotels(p[2])
    print(res)


def p_expression_reserve(p):
    'expression_reserve : RESERVE RENTAL DAYS'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.reserve(p[2], p[3])
    print(res)


def p_expression_stay(p):
    'expression_stay : STAY HOTEL'
    p[0] = p[1] + p[2]
    res = VoyageTools.stay(p[2])
    print(res)


def p_expression_cars(p):
    'expression_cars : CARS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.cars(p[2])
    print(res)


def p_expression_tours(p):
    'expression_tours : TOURS DESTINATION'
    p[0] = p[1] + p[2]
    res = VoyageTools.tours(p[2])
    print(res)


def p_expression_visit(p):
    'expression_visit : VISIT DESTINATION TOUR'
    p[0] = p[1] + p[2] + p[3]
    res = VoyageTools.visit(p[2], p[3])
    print(res)


def p_expression_book(p):
    'expression_book : BOOK'
    p[0] = p[1]
    res = VoyageTools.book()
    print(res)


# ------------------------------------------------------------
# Expression for error handling.
# ------------------------------------------------------------
def p_error(p):
    #print("Syntax error in input!")
    print("Syntax error at '%s'" % repr(p))  # p.value)

# Build the parser
parser = yacc.yacc()
