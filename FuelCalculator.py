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


# Welcome Message
def main():
    print('==================================================');
    print(' Welcome to Cheap Fuel Station (CFS)');
    print('==================================================');

    print('1. Unleaded 94 with E10');
    print('2. Unleaded 91');
    print('3. Unleaded 95');
    print('4. Super Unleaded 98');
    print('5. LPG');
    print('6. Disel');

    y = input('Please select the fuel type you would like to calculate the cost for (1-6):')
    y = int(y);

    # if (y == 1):
    #     unleaded94()

    # elif (y == 2):
    #     unleaded91()
    #
    # elif (y == 3):
    #     unleaded95()
    #
    # elif (y == 4):
    #     superUnleaded98()
    #
    # elif (y == 5):
    #     lpg()
    #
    # elif (y == 6):
    #     disel()

    else:
        print('The input you provided is not in the range between 1 and 6')
        print('Please select from 1 - 6')
        print('Thank You')
        print('---------------------------------------------------------------------------')
        main()


main()
