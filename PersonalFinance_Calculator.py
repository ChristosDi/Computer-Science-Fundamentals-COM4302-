import csv #import CSV module
import os #clear screen module
os.system('cls') #clear screen

#variables stored for menu DISPLAY
welcomeMessage=("Welcome to Personal Finance Calculator")

choisesDisplay=("1. Enter Income\n2. Add Expences\n3. View Budget Summary\n4. Exit")
endBanner =("--------------------------------------------------------------------------------------------------------")
choice =("Enter your choise: ")
wrongInput=("***Invalid option. Please Try again***")
'''
with open('PersonalFinance_Calculator.csv', 'w', newline='') as file:#opens CSV file in writtin mode (w mode) with the help of open()
    writer = csv.writer(file)#create CSV writter object
    row_list = [
        ["income", "expenses", "budgetSummary", "essential", "non_essential"], 
        ["5000", "2000", "3000", "1200","800"]
        ]# write multiple rows  
    writer.writerow(row_list) # writes the field data and other data to CSV 

# Open the CSV file in read mode
with open('PersonalFinance_Calculator.csv', 'r', newline='') as file:
    reader = csv.reader(file)  # CSV reader object
    for row in reader:
        print(row)  # prints each row in the CSV
'''
def enterExpense():#ENTER EXPENSES method
    while True:
        try:#this try-except process cannot accept strings-input expected is integer
            #we can accept even negative numbers-->abs()method turning negative to positive
            enter_expense=abs(float(input("Enter your monthly expenses: ")))
            os.system('cls')
            print(f"Your Monthly Expenses are {enter_expense}")
            return enter_expense
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print(endBanner)

def enterIncome():#ENTER INCOME method
    while True:
        try:#this try-except process cannot accept strings-input expected is integer
            enter_income=float(input("Enter your monthly income: "))
            if -1>enter_income:#monthly income can't be negative number
                print("***Invalid input. Please enter a number.***")
                print(endBanner)
            elif enter_income >=0:
                os.system('cls')
                print(f"Your monthly income is {enter_income}!")
                return enter_income
                break
            else:#anything else but a number such as strings are invalid input
                print("***Invalid input. Please enter a number.***")
                print(endBanner)
        except ValueError:
            print("Invalid Input. Please enter a number.")
            print(endBanner)

def mainMenuDisplay():#function to DISPLAY MAIN MENU options
    print("Welcome to Personal Finance Calculator")
    print(choisesDisplay)
    print(endBanner)

#MAIN MENU
def main_menu():#function to CALL MAIN MENU with functionality 
    mainMenuDisplay()#DISPLAY main menu

    #initialise
    monthlyIncome=None
    monthlyExpenses=None
    summary=0

    while True:
        optionFromMenu=input(choice)
        if optionFromMenu == '4':
            return False #returns false to the main_menu to exit while loop.
            break
        elif optionFromMenu== '1':
            monthlyIncome=enterIncome()#returns INCOME value and stores on the variable
            mainMenuDisplay()
            #return monthlyIncome #method main_menu RETURNS income value
        elif optionFromMenu== '2':
            monthlyExpenses=enterExpense() #stores EXPENSES value and stores on var.
            mainMenuDisplay()
            #return monthlyExpenses #method main_menu RETURNS expenses value
        elif optionFromMenu== '3':
            if monthlyExpenses is None or monthlyIncome is None:
                os.system('cls')
                print("Please enter both \"income\" and \"expenses\" before viewing the summary.\n")
                mainMenuDisplay()
            else:
                os.system('cls')
                summary=monthlyIncome-monthlyExpenses
                print(f"Summary: {summary}\nMonthly Income: {monthlyIncome}\nMonthly Expenses: {monthlyExpenses}")
                mainMenuDisplay()
        else:
            print(wrongInput)
            print(choisesDisplay)
            print(endBanner)

        

#PROGRAM
while True:
    checker=main_menu()
    if checker== False:
        print("Exiting...")
        break