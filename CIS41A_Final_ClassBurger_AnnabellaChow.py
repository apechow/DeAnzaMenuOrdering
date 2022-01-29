'''
CIS41A - Final Project - Class Burger
Annabella Chow

This class Burger gets the input of the burger order.
'''
from CIS41A_Final_ClassOrder_AnnabellaChow import *

#constant
ORDER_NUMBER_DICT = {"De Anza Burger" : 1 , "Bacon Cheese" : 2,

                                 "Mushroom Swiss" : 3, "Western Burger" : 4,

                                 "Don Cali Burger" : 5}
class Burger(Order):
    def __init__(self):
        super().__init__()
        
        
        
    def get_input(self):
        '''
    Gets input for order and quantity.
        '''
        #initializes variables
        flag = True
        self._total = 0
        
        while flag:
            flag1 = True
            try:
                #the order variable
                order = int(input("\n\nPlease enter your order. \
Enter \"6\" to exit: "))

                #If order is invalid, exception will be raised
                if order < 0 or order > 6 or not str(order).isdigit():
                    raise var

                #If user enters 6, the program does not ask for order or quantity.
                if order == 6:
                    flag = False
                    
                else:
                    while flag1:
                        try:
                            #Quantity variable
                            quantity = int(input("Enter the quantity: "))

                            #Ensures no invalid input that will cause the program to crash
                            if quantity > 0 and str(quantity).isdigit():
                                break

                            else:
                                raise var1
                        except Exception as var1:
                            print("\nError! Please enter a postive integer!")
                #Computes quantity into correct key
                for key in ORDER_NUMBER_DICT:
                    if ORDER_NUMBER_DICT[key] == order:
                        self._orderDict[key] = quantity

            #Catches all raised exception
            except Exception as var:
                print("\nError! Please enter a valid input!")

            finally:
                
                #checks that order is not empty
                for key in self._orderDict:
                    self._total += self._orderDict[key]

                if self._total == 0:
                    kill = True
                else:
                    kill = False

        return kill


 
