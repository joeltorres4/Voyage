# ------------------------------------------------------------
# VoyageLex.py
# ------------------------------------------------------------
import ply.lex as lex

# Reserved words
reserved = {
    'createpackage': 'CREATEPACKAGE',
    'destinations': 'DESTINATIONS',
    'flights': 'FLIGHTS',
    'fly': 'FLY',
    'hotels': 'HOTELS',
    'reserve': 'RESERVE',
    'stay': 'STAY',
    'cars': 'CARS',
    'tours': 'TOURS',
    'visit': 'VISIT',
    'book': 'BOOK'
}

# List of token names. This is always required
tokens = ['NAME',
          'DESTINATION',
          'DATE',
          'AIRLINE',
          'HOTEL',
          'RENTAL',
          'TOUR',
          'DAYS',
          'ID'
          ] + list(reserved.values())

# Regular expression rules for simple tokens
t_NAME = r'[a-zA-Z]+'
t_DESTINATION = r'[a-zA-Z]+'
t_DATE = r'/(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d/'
t_AIRLINE = r'[a-zA-Z]+'
t_HOTEL = r'[a-zA-Z]+'
t_RENTAL = r'[a-zA-Z]+'
t_TOUR = r'[a-zA-Z]+'


# Define a rule for rental days number
def t_DAYS(t):
    r'[0-9]{3}'
    t.value = int(t.value)
    return t


# Define a rule for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    print(t.value+" is a keyword!")
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
