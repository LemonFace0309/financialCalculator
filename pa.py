from sympy.solvers import solve
from sympy import Symbol

possibleValues = ['PV', 'PMT', 'i']


def getPA():
    variable = input('What are you looking for (PV|PMT|i): ')

    if variable not in possibleValues:
        exit()

    pv = Symbol('pv')
    pmt = Symbol('pmt')
    i = Symbol('i')

    if variable == 'PV':
        pmt = float(input('Enter PMT: '))
        i = float(input('Enter i: '))
    elif variable == 'PMT':
        pv = float(input('Enter PV: '))
        i = float(input('Enter i: '))
    elif variable == 'i':
        pv = float(input('Enter PV: '))
        pmt = float(input('Enter PMT: '))

    sol = solve((pv - pmt / i), variable)
    print(sol)
