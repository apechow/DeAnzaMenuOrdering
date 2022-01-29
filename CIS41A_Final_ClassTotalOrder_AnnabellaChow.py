'''
CIS41A - Final Project - class Total_Order
Annabella Chow

This class Total_Order gets the input from both parents, Burger and Person.
It calculates the total cost and updates and/or delete the order when requested.
'''

from CIS41A_Final_ClassBurger_AnnabellaChow import *
from CIS41A_Final_ClassPerson_AnnabellaChow import *

class Total_Order(Burger, Person):

    def __init__(self):
        super().__init__()

    def get_input(self):
        '''
    gets input of both the burger order and the input of the user status.
        '''
        kill = Burger.get_input(self)
        status = Person.get_input(self)

        return status, kill
    
        
    def compute_pay(self, status):
            '''
    This method computes the pay base on user order.
            '''
            #impose tax if user is a Staff
            if status == 2:
                self._tax = 0.09
                
            #Uses a for loop to calculate the individual price before and after tax
            for key in self._priceDict:
                   self._priceBtax += self._orderDict[key] * self._priceDict[key]
                   self._priceAtax = round(self._priceBtax + (self._priceBtax * self._tax), 2)
            return self._priceAtax #used for unit testing

    def update_order(self):
        '''
    This method updates the order or status if the user wants to.
        '''
        #initialize variable
        repeat = True
        
        while repeat:
            repeat1 = True
            try:
                print('-' *50)
                #Ask user if it wants to update order
                update = input('\n\nAre you ready to proceed or would you like to update your order?\n Please enter \
\'y\' for yes (to update) or \'n\' for no (to continue): ')

                if update == 'y':
                    print('If you would like to update your order, press \'1\'.\n If you would like to update\
 your status, press \'2\'.\n If you do not want to update your order, please press \'6\'.')

                    while repeat1:
                        try:
                            #Ask input if it wants to change its status or order
                            choice = int(input('\nWould you like to update your order or status? '))

                            if choice == 1:
                                Burger.get_input(self)
                                break
                            elif choice == 2:
                                Person.get_input(self)
                                break
                            elif choice == 6:
                                repeat = False
                                break
                            else:
                                raise var3
                        except Exception as var3:
                            print('\nPlease enter either 1 for order, 2 for status, or 6 to quit')

                elif update == 'n':
                    break
                
                else:
                    #if user enters an invalid input other than y or n
                    raise var2
                
            except Exception as var2:
                print('\nPlease enter a valid input!')


    def delete(self):
        '''
    This method deletes the order if user wishes to.
        '''
        flag = True
        while flag:
            try:
                #Ask user if it wants to cancel order
                cancel = input('\nDo you want to cancel your order? Press \'y\' for yes or press \'n\' for no: ')
                if cancel == 'y':
                    self._priceAtax = 0
                    break
                
                elif cancel == 'n':
                    break
                #Checks user does not enter invalid input
                else:
                    raise var
            except Exception as var:
                print('\nPlease enter \'y\' for yes or  \'n\' for no!\n')
                
    def shutdown(self):
        '''
    Method shutsdown the code.
        '''
        print()
        print()
        #Asking user if he wants to continue
        userInputToContinue = input("Continue for another order(Any \
keys= Yes, n= No)?".strip())

        if userInputToContinue.lower() == 'n':

            print("The system is shutting down!")

            flag = False
            return flag
    

