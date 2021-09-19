from pva import getPVA
from fva import getFVA
from pa import getPA

possibleValues = ['FV', 'PV', 'EIR', 'FVA', 'PVA', 'PA']

while True:
    formula = input("What are you calculating for (FV|PV|EIR|FVA|PVA|PA): ")
    if formula in possibleValues:
        break

if formula == 'PVA':
    getPVA()
elif formula == 'FVA':
    getFVA()
elif formula == 'PA':
    getPA()
