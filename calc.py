from pva import getPVA
from fva import getFVA

possibleValues = ['FV', 'PV', 'EIR', 'FVA', 'PVA']

formula = input("What are you calculating for (FV|PV|EIR|FVA|PVA): ")

if formula not in possibleValues:
    exit()

if formula == 'PVA':
    getPVA()
elif formula == 'FVA':
    getFVA()
