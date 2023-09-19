# Name: Cian Cripps
# Student Number: 121474322

from typing import ClassVar

### INCOME ###

# classes 
class Income:
    """
    Base class for Student income 
    """
    
    num_income: ClassVar[int] = 0

    # instance attributes
    # Encapsulation 
    # having private variables
    __type_of_income: ClassVar[str]
    __source_of_income: ClassVar[str]
    __amount_of_income: ClassVar[int]

    # class constructor
    def __init__(self, toi:str, soi:str, aoi:int) -> None:
        # private variables with 
        # Abstraction
        self.__type_of_income = toi
        self.__source_of_income = soi
        self.__amount_of_income = aoi
        Income.num_income += 1

    # class property - more concise way of using setters and getters - to ensure encapsulation
    @property
    def type_of_income(self):
        return self.__type_of_income

    @type_of_income.setter
    def type_of_income(self, toi: str):
        self.__type_of_income = toi

    @property
    def source_of_income(self):
        return self.__source_of_income

    @source_of_income.setter
    def source_of_income(self, soi: str):
        self.__source_of_income = soi

    # traditional setters and getters method of ensuring encapsulation
    def get__amount_of_income(self) -> int:
        return self.__amount_of_income

    def set__amount_of_income(self, aoi: int) -> None:
        self.__amount_of_income = aoi

    # string method to display income details
    def __str__(self) -> str:
        return self.__type_of_income +\
            " From " + self.__source_of_income +\
                 ":€" + str(self.__amount_of_income)

# Wages - child class of Income Parent class 
# Inheritance
class Wages(Income):
    '''
    Wages Class
    '''
    num_Wages: ClassVar[int] = 0

    # constructor
    def __init__(self, toi:str, soi:str, aoi:str) -> None:
        # get name of class
        toi = self.__class__.__name__
        # call to super/parent constructor
        super().__init__(toi, soi, aoi)

        # increment the number of wages
        Wages.num_Wages += 1

# Grants - child class of Income Parent class 
# Inheritance
class Grants(Income):
    '''
    Grants Class
    '''
    num_Grants: ClassVar[int] = 0

    # constructor
    def __init__(self, toi:str, soi:str, aoi:str) -> None:
        # get name of class
        toi = self.__class__.__name__
        # call to super/parent constructor
        super().__init__(toi, soi, aoi)

        # increment the number of grants
        Grants.num_Grants += 1

incomes = []
types_of_incomes = []
sources_of_incomes = []
amount_of_incomes = []

# Parent / Child class 
# Inheritance
class UserIncome(Income):
    '''
    UserIncome Class
    '''
    num_userIncomes: ClassVar[int] = 0

    # constructor
    def __init__(self, *args:str) -> None:
        # get name of class
        # call to super/parent constructor
        toi = self.__class__.__name__
        preBuiltIncome = str(input("Select type of income: Wages / Grant / Custom: "))
        preBuiltIncome.strip()     #remove whitespace in case user mistyped
        preBuiltIncome.capitalize() # capitalize user input
        if preBuiltIncome == "Wages":
            type = "Wages"
        elif preBuiltIncome == "Grant":
            type = "Grant"
        else:
            type = str(input("Enter type of income: "))
        toi = type
        types_of_incomes.append(type)
        source = str(input("Enter source: "))
        soi = source
        sources_of_incomes.append(source)
        amount = int(input("Enter amount(€): "))
        aoi = amount
        total = type, source, amount
        incomes.append(total)
        amount_of_incomes.append(amount)
        super().__init__(toi, soi, aoi)
        if preBuiltIncome == "Wages":
            Wages(preBuiltIncome,source,amount)
        elif preBuiltIncome == "Grant":
            Grants(preBuiltIncome,source,amount)
        # increment the number of incomes
       
        UserIncome.num_userIncomes += 1
        
args = int(input("How many incomes are you adding?"))


for i in range(args):

    income: UserIncome = UserIncome()
    print(income, "added to your income details")
print("Your updated income details are:", incomes) 
    
print("types of income:", types_of_incomes)
print("sources of income:", sources_of_incomes)
print("total amount of income is: €", sum(amount_of_incomes))

### EXPENSES ### 

# classes 
class Expenses:

    # instance attributes
    # Encapsulation - restricting access to methods and attributes in a class
    # having private variables
    __type_of_expense: ClassVar[str]
    __date_of_expense: ClassVar[str]
    __cost_of_expense: ClassVar[int]

    # class constructor
    def __init__(self, toe:str, doe:str, coe:int) -> None:
        # private variables 
        # Abstraction
        self.__type_of_expense = toe
        self.__date_of_expense = doe
        self.__cost_of_expense = coe

    # class property - more concise way of using setters and getters - to ensure encapsulation
    @property
    def type_of_expense(self):
        return self.__type_of_expense

    @type_of_expense.setter
    def type_of_expense(self, toe: str):
        self.__type_of_expense = toe

    @property
    def date_of_expense(self):
        return self.__date_of_expense

    @date_of_expense.setter
    def date_of_expense(self, doe: str):
        self.__date_of_expense = doe

    # traditional setters and getters method of ensuring encapsulation
    def get__cost_of_expense(self) -> int:
        return self.__cost_of_expense

    def set__cost_of_expense(self, coe: int) -> None:
        self.__cost_of_expense = coe

    # string method to display income details
    def __str__(self) -> str:
        return self.__type_of_expense +\
            " On " + self.__date_of_expense +\
                 ": " + str(self.__cost_of_expense)

# Leisure expenses - child class of Expenses Parent class 
# Inheritance
class Leisure(Expenses):
    '''
    Leisure expenses Class
    '''
    num_leisure: ClassVar[int] = 0

    # constructor
    def __init__(self, toe:str, doe:str, coe:int) -> None:
        # get name of class
        toe = self.__class__.__name__
        # call to super/parent constructor
        super().__init__(toe, doe, coe)

        # increment the number of leisure expenses
        Leisure.num_leisure += 1

# Fixed expenses - child class of Expenses Parent class 
# Inheritance
class Fixed(Expenses):
    '''
    Fixed expenses Class
    '''
    num_Fixed: ClassVar[int] = 0

    # constructor
    def __init__(self, toe:str, doe:str, coe:str) -> None:
        # get name of class
        toe = self.__class__.__name__
        # call to super/parent constructor
        super().__init__(toe, doe, coe)

        # increment the number of fixed expenses
        Fixed.num_Fixed += 1

expenses = []
types_of_expenses = []
date_of_expenses = []
cost_of_expenses = []

# Parent / Child Class / Inheritance
class UserExpenses(Expenses):
    '''
    UserIncome Class
    '''
    num_userExpenses: ClassVar[int] = 0

    # constructor
    def __init__(self, *args:str) -> None:
        # get name of class
        # call to super/parent constructor
        toe = self.__class__.__name__
        # Prompts the user to choose their desired Expense
        preBuiltExpense = str(input("Select type of Expense: Fixed / Leisure / Custom:  "))
        # removes whitespace 
        preBuiltExpense.strip() 
        # capitalizes user input    
        preBuiltExpense.capitalize() 
        if preBuiltExpense == "Fixed":
            type = "Fixed"
        elif preBuiltExpense == "Leisure":
            type = "Leisure"
        else:
            type = str(input("Enter type of expense: "))
        toe = type
        types_of_expenses.append(type)
        date = str(input("Enter day: "))
        doe = date
        date_of_expenses.append(date)
        cost = int(input("Enter cost (€): "))
        coe = cost
        total = type, date, cost
        expenses.append(total)
        date_of_expenses.append(date)
        cost_of_expenses.append(cost)
        # call to the parent constructor
        super().__init__(toe, doe, coe)
        if preBuiltExpense == "Fixed":
            # create a subclass of fixed expense
            Fixed(preBuiltExpense,date,cost)
            # create a subclass of leisure expense
        elif preBuiltExpense == "Leisure":
            Leisure(preBuiltExpense,date,cost)
        # increment the number of Expenses
       
        UserExpenses.num_userExpenses += 1

args = int(input("How many expenses are you adding?"))

for i in range(args):

    expense: UserExpenses = UserExpenses()
    print(expense, "added to your expenses")
print("Your updated expenses: ", expenses) 
    
print("types of expenses: ", types_of_expenses)
print("days when expenses were taken: ", date_of_expenses)
print("total cost of expenses: ", sum(cost_of_expenses))

# Polymorphism
class Budget:
    '''
    Budget class
    '''
    def __init__(self, *args):
        pass

    def result(self):
        # gets the users profit / loss
        amount = (sum(amount_of_incomes) - sum(cost_of_expenses))
        if sum(amount_of_incomes) == sum(cost_of_expenses):
            return("Whew that was close! It's gonna be a tough week but you'll survive!")
        elif sum(amount_of_incomes) > sum(cost_of_expenses):
            return("Your in profit! Congratulations you've saved %s spend wisely" % (amount))
        elif sum(amount_of_incomes) < sum(cost_of_expenses):
            return("It seems you've over spent by %s time to call the parents" % (amount))
         





