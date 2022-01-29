'''
CIS41A - Final Project - Driver
Annabella Chow

This is the driver for the final project that runs everything.
'''

from CIS41A_Final_ClassBill_AnnabellaChow import *

if __name__ == '__main__':
    
    order = Bill()
    order.show_order()
    status, kill = order.get_input()
    if not kill:
        order.compute_pay(status)
        order.update_order()
        order.delete()
        order.show_bill()
        order.saveToFile()
        order.shutdown()
    
'''
Output:
	  ~Menu for De Anza Grill~	
	1. De Anza Burger      5.25
	2. Bacon Cheese        5.75
	3. Mushroom Swiss      5.95
	4. Western Burger      5.95
	5. Don Cali Burger     5.95
	6. Exit


Please enter your order. Enter "6" to exit: 1
Enter the quantity: 2


Please enter your order. Enter "6" to exit: 5
Enter the quantity: 6


Please enter your order. Enter "6" to exit: 67

Error! Please enter a valid input!


Please enter your order. Enter "6" to exit: 6

If a student, please enter 1 
If a staff, please enter 2: 2
--------------------------------------------------


Are you ready to proceed or would you like to update your order?
 Please enter 'y' for yes (to update) or 'n' for no (to continue): y
If you would like to update your order, press '1'.
 If you would like to update your status, press '2'.
 If you do not want to update your order, please press '6'.

Would you like to update your order or status? 2

If a student, please enter 1 
If a staff, please enter 2: 3
Error: Please enter either 1 for student or 2 for staff!

If a student, please enter 1 
If a staff, please enter 2: 1
--------------------------------------------------


Are you ready to proceed or would you like to update your order?
 Please enter 'y' for yes (to update) or 'n' for no (to continue): n

Do you want to cancel your order? Press 'y' for yes or press 'n' for no: n

***************************************************************************

 ~ De Anza Grill Bill ~ 

Thank you for ordering!
This is what you have ordered:
 De Anza Burger       Qty: 2          Price: $5.25       Total: $10.50     
 Don Cali Burger      Qty: 6          Price: $5.95       Total: $35.70     
--------------------------------------------------
Price before tax: 46.20
Tax: 0.09
Price after tax: 50.36


Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!
'''
    
    
