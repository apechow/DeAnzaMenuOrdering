'''
CIS41A - Final Project - class Bill
Annabella Chow

This code is for the class Bill which shows and prints the bill.
'''

import time
import datetime
from CIS41A_Final_ClassTotalOrder_AnnabellaChow import *


class Bill(Total_Order):
    def __init__(self):
        super().__init__()
     
    def show_bill(self):
        '''
This method prints out the bill for the user to see.
        '''
        
        #If user did not order anything, the bill will not be print out
        if self._priceAtax != 0:
            print()
            print("*" * 75)
            print()
            print(" ~ De Anza Grill Bill ~ ")
            print("\nThank you for ordering!")
            print("This is what you have ordered:")
            for key in self._orderDict:
                #Only prints out what user ordered
                if self._orderDict[key] != 0:
                      print(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f"\
                            %(key, self._orderDict[key],self._priceDict[key], \
                              (self._orderDict[key]*self._priceDict[key])))
            print("-"*50)
            #print("Price before tax: %.2f" %self._priceBtax)
            print("Price before tax: %.2f" %self._priceBtax)
            print("Tax: %.2f" %self._tax)
            print("Price after tax: %.2f" %self._priceAtax)


    def saveToFile(self):
        '''
This method saves the bill to a new file - like a receipt
        '''
        #Ensures that file will not be created if user did not order anything
        if self._priceAtax != 0:
            #File name base on date and time
            timeStamp = time.time()
            orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).\
                             strftime("%Y-%m-%d %H-%M-%S")
            orderTimeStamp = orderTimeStamp + '.txt'

            #Opens new file
            with open(orderTimeStamp,'w') as fileHandleToSaveTheBill :
                #Writes the bill to the new file
                fileHandleToSaveTheBill.write("\n")
                fileHandleToSaveTheBill.write("*" * 75 + "\n")
                fileHandleToSaveTheBill.write("\n")
                fileHandleToSaveTheBill.write(" ~ De Anza Grill Bill ~ \n")
                fileHandleToSaveTheBill.write("\nThank you for ordering!\n")
                fileHandleToSaveTheBill.write("This is what you have ordered:\
\n")
                for key in self._orderDict:
                    if self._orderDict[key] != 0:
                          fileHandleToSaveTheBill.write(" %-20s Qty: %-10d \
Price: $%-10.2f Total: $%-10.2f\n" %(key, self._orderDict[key],self._priceDict[key],\
                                     (self._orderDict[key]*self._priceDict[key])))
                fileHandleToSaveTheBill.write("-"*50 + "\n")
                fileHandleToSaveTheBill.write("Price before tax: %.2f\n" \
                                              %self._priceBtax)
                fileHandleToSaveTheBill.write("Tax: %.2f\n" %self._tax)
                fileHandleToSaveTheBill.write("Price after tax: %.2f\n" \
                                              %self._priceAtax)

    


