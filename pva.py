from sympy.solvers import solve
from sympy import Symbol

possibleValues = ['PV', 'PMT', 'i', 'n']


def getPVA():
    variable = input('What are you looking for (PV|PMT|i|n): ')

    if variable not in possibleValues:
        exit()

    pv = Symbol('pv')
    pmt = Symbol('pmt')
    i = Symbol('i')
    n = Symbol('n')
    missing = 'pv'

    if variable == 'PV':
        pmt = float(input('Enter PMT: '))
        i = float(input('Enter i: '))
        n = int(input('Enter n: '))
    elif variable == 'PMT':
        pv = float(input('Enter PV: '))
        i = float(input('Enter i: '))
        n = int(input('Enter n: '))
        missing = 'pmt'
    elif variable == 'i':
        pv = float(input('Enter PV: '))
        pmt = float(input('Enter PMT: '))
        n = int(input('Enter n: '))
        missing = 'i'
    elif variable == 'n':
        pv = float(input('Enter PV: '))
        pmt = float(input('Enter PMT: '))
        i = float(input('Enter i: '))
        missing = 'n'

    sol = solve(pv - pmt * ((1 - 1/((1+i)**n)) / i), missing)
    print(sol)
