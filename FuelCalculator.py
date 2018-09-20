# Constants Values
# Constant for fuel l
ONE = 130.9
# Constant for fuel 2
TWO = 132.9
# Constant for fuel 3
THREE = 145.9
# Constant for fuel 4
FOUR = 153.9
# Constant for fuel 5
FIVE = 71.9
# Constant for fuel 6
SIX = 125.9

HUNDRED = 100


# To ask to continue using the app or exit
def continueApp():
    global cont
    cont = input('Continue [y/n]: ')
    if cont == 'y':
        main()
    elif cont == 'n':
        exit()


# To Calculate Litre
def calculateLitre():
    # Made globLitre Global Variable
    global globLitre
    globLitre = float(input(' Please input the volume (in litres):'))

    # Check if the input litre is valid or not
    if globLitre <= 0 or globLitre > 11000:
        print('Invalid Litre!!!')
        print('Please Select different litre')
        print('----------------')
        main()
    else:
        return globLitre


# To calculate the first choice "Unleaded 94 with E10"
def unleaded94():
    print('You selected: Unleaded 94 with E10')
    calculateLitre()

    # Assigning local variable to the global variable for further calculation
    litre = globLitre
    unleaded94 = float(float(ONE) * litre) / HUNDRED
    print(' The cost of the fuel in AUD($):', format(unleaded94, '.2f'), 'AUD')
    continueApp()
    return globLitre


# To calculate the second choice "Unleaded 91"
def unleaded91():
    print('You selected: Unleaded 91')
    calculateLitre()
    litre = globLitre
    unleaded91 = float(float(TWO) * litre) / HUNDRED
    print(' The cost of the fuel in AUD($):', format(unleaded91, '.2f'), 'AUD')
    continueApp()
    return globLitre


# Welcome Message
def main():
    print('==================================================')
    print(' Welcome to Cheap Fuel Station (CFS)');
    print('==================================================')

    print('1. Unleaded 94 with E10')
    print('2. Unleaded 91')
    print('3. Unleaded 95')
    print('4. Super Unleaded 98')
    print('5. LPG')
    print('6. Diesel')

    y = input('Please select the fuel type you would like to calculate the cost for (1-6):')
    y = int(y)

    if y == 1:
        unleaded94()

    elif y == 2:
        unleaded91()

    # elif y == 3:
    #     unleaded95()
    #
    # elif y == 4:
    #     superUnleaded98()
    #
    # elif y == 5:
    #     lpg()
    #
    # elif y == 6:
    #     disel()

    else:
        print('The input you provided is not in the range between 1 and 6')
        print('Please select from 1 - 6')
        print('Thank You')
        print('---------------------------------------------------------------------------')
        main()


main()
