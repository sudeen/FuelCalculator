# Constants Values
# Constant price for fuel l
FUEL_ONE_RATE = 130.9
# Constant price for fuel 2
FUEL_TWO_RATE = 132.9
# Constant price for fuel 3
FUEL_THREE_RATE = 145.9
# Constant price for fuel 4
FUEL_FOUR_RATE = 153.9
# Constant price for fuel 5
FUEL_FIVE_RATE = 71.9
# Constant price for fuel 6
FUEL_SIX_RATE = 125.9

HUNDRED = 100

THREE_DOLLAR_DISCOUNT = 3

SIX_DOLLAR_DISCOUNT = 6

# Initially Discount is set to zero
DISCOUNT = 0

# Initially Fuel is set to zero
FUEL = 0

DISCOUNT_TEN_PERCENT = 0.1

DISCOUNT_FIFTEEN_PERCENT = 0.15

DISCOUNT_TWENTY_PERCENT = 0.2

MAX_DISCOUNT = 26


# To ask to continue using the app or exit
def continueApp():
    global continue_again
    continue_again = input('Do you want to enter fuel volume for another customer (Y/N)?: ')
    if continue_again == 'y' or continue_again == 'Y':
        main()
    elif continue_again == 'n':
        print('See you again!')
        exit()


# To Calculate Litre
def calculateLitre():
    # Made globLitre Global Variable
    global global_litre
    try:
        global_litre = float(input(' Please input the volume (in litres):'))
    except ValueError:
        print('Invalid value of litre')
        print('Please use integer as an input')
        calculateLitre()
    # Check if the input litre is valid or not
    if global_litre <= 0 or global_litre > 11000:
        print('Invalid Litre!!!')
        print('Please Select different litre')
        print('********************************************')
        main()
    else:
        return global_litre


# Print Cost of fuel function
def print_cost(FUEL):
    dis = check_price_and_discount(FUEL)
    print('The cost of fuel in AUD($): ', format(FUEL, '.2f'))
    FUEL -= dis
    print('Your saving in this purchase is AUD($): ', format(dis, '.2f'))
    print(' The cost of the fuel in AUD($):', format(FUEL, '.2f'), 'AUD')
    print('Thanks for using CFS Fuel cost calculator!')
    print('See you again!')
    continueApp()


# Discount Policy is listed here
def check_price_and_discount(FUEL):
    global DISCOUNT
    if 0 < FUEL < 20:
        DISCOUNT = 0
    elif 20 < FUEL <= 30:
        DISCOUNT = DISCOUNT_TEN_PERCENT * (FUEL - 20)
    elif 30 < FUEL <= 50:
        DISCOUNT = THREE_DOLLAR_DISCOUNT + (DISCOUNT_FIFTEEN_PERCENT * (FUEL - 30))
    elif 50 < FUEL <= 150:
        DISCOUNT = SIX_DOLLAR_DISCOUNT + (DISCOUNT_TWENTY_PERCENT * (FUEL - 50))
    else:
        DISCOUNT = MAX_DISCOUNT
    return DISCOUNT


# To calculate the first choice "Unleaded 94 with E10"
def unleaded94():
    print('You selected: Unleaded 94 with E10')
    calculateLitre()
    FUEL = float(float(FUEL_ONE_RATE) * global_litre) / HUNDRED
    print_cost(FUEL)
    return FUEL


# To calculate the second choice "Unleaded 91"
def unleaded91():
    print('You selected: Unleaded 91')
    calculateLitre()
    FUEL = float(float(FUEL_TWO_RATE) * global_litre) / HUNDRED
    print_cost(FUEL)
    return FUEL


# To calculate the third choice "Unleaded 95"
def unleaded95():
    print('You selected: Unleaded 95')
    calculateLitre()
    FUEL = float(float(FUEL_THREE_RATE) * global_litre) / HUNDRED
    print_cost(FUEL)
    return FUEL


# To calculate the fourth choice "Super Unleaded 98"
def superUnleaded98():
    print('You selected: Super Unleaded 98')
    calculateLitre()
    FUEL = float(float(FUEL_FOUR_RATE) * global_litre) / HUNDRED
    print_cost(FUEL)
    return FUEL


# To calculate the fifth choice "LPG"
def lpg():
    print('You selected: LPG')
    calculateLitre()
    FUEL = float(float(FUEL_FIVE_RATE) * global_litre) / HUNDRED
    print_cost(FUEL)
    return FUEL


# To calculate the sixth choice "Disel"
def diesel():
    print('You selected: Disel')
    calculateLitre()
    litre = globLitre
    disel = float(float(SIX) * litre) / HUNDRED
    print(' The cost of the fuel in AUD($):', format(disel, '.2f'), 'AUD')
    continueApp()
    return globLitre


# Welcome Message
def main():
    print('==================================================')
    print(' Welcome to Cheap Fuel Station (CFS)')
    print('==================================================')

    print('1. Unleaded 94 with E10')
    print('2. Unleaded 91')
    print('3. Unleaded 95')
    print('4. Super Unleaded 98')
    print('5. LPG')
    print('6. Diesel')

    fuel_type = input('Please select the fuel type you would like to calculate the cost for (1-6):')

    try:
        user_input = int(fuel_type)

    except ValueError:
        print('\nYou did not enter a valid integer')
        print('Please user integer as an input, select from 1 - 6')
        main()

    if user_input == 1:
        unleaded94()
    elif user_input == 2:
        unleaded91()

    elif user_input == 3:
        unleaded95()

    elif user_input == 4:
        superUnleaded98()

    elif user_input == 5:
        lpg()

    elif user_input == 6:
        diesel()

    else:
        print('The input you provided is not in the range between 1 and 6')
        print('Please select from 1 - 6')
        print('Thank You')
        print('---------------------------------------------------------------------------')
        main()


main()
