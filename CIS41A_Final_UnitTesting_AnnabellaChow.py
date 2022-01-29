'''
CIS41A Final - Unit Testing
Annabella Chow

This code runs the unit testing for the final project
'''

import unittest
from CIS41A_Final_ClassBill_AnnabellaChow import *

class TestCalculation(unittest.TestCase):
        
    def test_total(self):
        '''
    Test total cost after tax calculation.
        '''
        dut = Bill()
        dut._orderDict['De Anza Burger'] = 5
        self.assertAlmostEqual(dut.compute_pay(2), round(5*5.25 + 5*5.25*0.09, 2))

        
if __name__ == '__main__':
    unittest.main()
