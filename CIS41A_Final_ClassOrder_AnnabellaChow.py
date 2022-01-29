class Order:
    '''
Something
    '''
    def __init__(self):
        #Price before tax
        self._priceBtax = 0

        #Price after tax
        self._priceAtax = 0

        #Tax
        self._tax = 0
        
        #Menu
        self._priceDict = {"De Anza Burger" : 5.25 , "Bacon Cheese" : 5.75,

                                    "Mushroom Swiss" : 5.95, "Western Burger" : 5.95,

                                    "Don Cali Burger" : 5.95}
        #Initializing variable
        #User Order
        self._orderDict = {"De Anza Burger" : 0 , "Bacon Cheese" : 0,

                                     "Mushroom Swiss" : 0, "Western Burger" : 0,

                                     "Don Cali Burger" : 0}

    def show_order(self):
        '''
Prints out the menu for user to read.
        '''
        print("\t  ~Menu for De Anza Grill~\t")
        number = 1
        #Prints out each of the dictionary key and value and the number
        #associated with it
        for key in self._priceDict:
            print("\t{a}. {b:15s} {c:8.2f}".format(a= number, b= key, \
                                                   c=self._priceDict[key]))
            number +=1
        print("\t6. Exit")


    
