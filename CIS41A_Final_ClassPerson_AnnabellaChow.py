'''
CIS41A Final Project - class Person
Annabella Chow

This class Person gets the input for the status of the user.
'''

from CIS41A_Final_ClassOrder_AnnabellaChow import *

class Person(Order):
    '''
    '''
    def __init__(self):
        super().__init__()


    def get_input(self):
        '''
    This method gets input on what user status is.
        '''
        #initializing variable
        flag = True
        self._quantity = 0
        self.unittest_sel = False

        #Checks that the order did order something
        for key in self._orderDict:
            self._quantity += self._orderDict[key]

        if self._quantity != 0:
            while flag:
                try:
                    #Asking user whether he/she is a student or staff to calculate
                    #the tax
                    status = int(input("\nIf a student, please enter 1 \nIf a staff, please enter 2: "))

                    #Checks that user enters correct input
                    if status == 1 or status == 2:
                        break

                    #Checking if input is a valid integer
                    elif status is not str(status).isdigit() or status < 0 \
                         or status > 2:
                        raise var2
                    
                except Exception as var2:
                    print("Error: Please enter either 1 for student or 2 for staff!")
                    #print('ut_sel:', self_unittest_sel)
                    if self.unittest_sel:
                        break
            return status

    

