from sympy.solvers import solve
from sympy import Symbol

possibleValues = ['FV', 'PMT', 'i', 'n']


def getFVA():
    variable = input('What are you looking for (FV|PMT|i|n): ')

    if variable not in possibleValues:
        exit()

    fv = Symbol('fv')
    pmt = Symbol('pmt')
    i = Symbol('i')
    n = Symbol('n')

    if variable == 'FV':
        pmt = float(input('Enter PMT: '))
        i = float(input('Enter i: '))
        n = int(input('Enter n: '))
    elif variable == 'PMT':
        fv = float(input('Enter FV: '))
        i = float(input('Enter i: '))
        n = int(input('Enter n: '))
    elif variable == 'i':
        fv = float(input('Enter FV: '))
        pmt = float(input('Enter PMT: '))
        n = int(input('Enter n: '))
    elif variable == 'n':
        fv = float(input('Enter FV: '))
        pmt = float(input('Enter PMT: '))
        i = float(input('Enter i: '))

    sol = solve(fv - pmt * ((((1+i)**n) - 1) / i), variable)
    print(sol)
