# ------------------------------------------------------------
# Voyage.py
# ------------------------------------------------------------

# Import parser to start execution
from VoyageYacc import parser


def main():
    while True:
        try:
            s = input('\nVoyage > ')
        except EOFError:
            break

        if s == 'quit':
            break
        if not s:
            continue # Empty input, keep scanning...

        parser.parse(s)

if __name__ == '__main__':
    main()
