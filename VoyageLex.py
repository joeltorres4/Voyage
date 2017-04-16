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
          'XX',
          'ID'
          ] + list(reserved.values())


def t_XX(t):
    r'[A-Z]{2}'
    return t


def t_DAYS(t):
    r'[0-9]{1,2,3}'
    t.value = int(t.value)
    return t

# Define a rule for reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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
