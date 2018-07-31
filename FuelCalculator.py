#Constants
ONE= 130.9
TWO= 132.9
THREE= 145.9
FOUR= 153.9
FIVE= 71.9
SIX= 125.9
HUNDRED= 100
FUEL_LIST = ['lead','unlead','aaaa']

def main(FUEL_LIST):

    print('==================================================');
    print(' Welcome to Cheap Fuel Station (CFS)');
    print('==================================================');

    print('1. Unleaded 94 with E10');
    print('2. Unleaded 91');
    print('3. Unleaded 95');
    print('4. Super Unleaded 98');
    print('5. LPG');
    print('6. Disel');

    y=input('Please select the fuel type you would like to calculate the cost for (1-6):')
    y=int(y);

    if y<=6:
        for i in range (len(FUEL_LIST)):
            if i==1:
                print('The fuel type you selected is:', FUEL_LIST[0]);

            elif i==2:
                print('The fuel type you selected is:', FUEL_LIST[1]);

        litre=float(input(' Please input the volume (in litres):'))
        if litre<=0 or litre >11000:
            print('Invalid Litre')
            exit();

    if y == 1:
        y1= float(float(ONE)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y1, '.2f') )

    elif y ==2:
        y2= float(float(TWO)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y2, '.2f') )
    
    elif y==3:
        y3= float(float(THREE)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y3, '.2f') )

    elif y==4:
        y4= float(float(FOUR)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y4, '.2f') )

    elif y==5:
        y5= float(float(FIVE)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y5, '.2f') )

    elif y==6:
        y6= float(float(SIX)*litre)/HUNDRED
        print(' The cost of the fuel in AUD($):', format(y6, '.2f') )

        print('Thanks for using CFS Fuel cost calculator!')
        print('See you again!')

    elif y>6 or y<0:
        print('enter valid number 1-6')
    
   

    

main(FUEL_LIST)
