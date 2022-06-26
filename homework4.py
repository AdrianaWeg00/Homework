# TASK 2

import sys

def pin_number():
    password = 1234
    trials = 3

    while trials != 0:
        pin_code = int(input('Enter your pin: '))
        if password != pin_code:
            trials -= 1
            print ("Try Again!")
        elif password == pin_code:
            print('PIN Correct')
            Balance()

    else:
         print('Wrong PIN')

def Balance():
    try:
        balance = 100
        withdrawal = int(input('How much would you like to withdraw?: '))
        new_balance = int(balance) - int(withdrawal)
        if withdrawal > balance:
            sys.exit("Error")
        if withdrawal < 0:
            raise ValueError
    except ValueError as e:
        print ('please enter a positive number')
    else:
        print("Your new balance is {}".format(new_balance))

pin_number()

