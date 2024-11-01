import csv #import CSV module
import os #clear screen module
os.system('cls') #clear screen

#variables stored for menu DISPLAY
welcomeMessage=("Welcome to Personal Finance Calculator")

choisesDisplay=("1. Enter Income\n2. Add Expences\n3. View Budget Summary\n4. Exit")
endBanner =("--------------------------------------------------------------------------------------------------------")
choice =("Enter your choise: ")
wrongInput=("***Invalid option. Please Try again***")
inputError_str=("Invalid Input!Please enter a number.")

#dictionary for storing ESSENTIAL EXPENSES
essentialExpenses={
"rent":0,
"electricity":0,
"water":0,
"gas":0,
"phone":0,
"internet":0,
"supermarket":0
}
#dictionary for storing NON-ESSENTIAL EXPENSES
non_essentialExpenses={
"dining_out":0,
"events":0,
"gym":0,
"streaming_services":0,
"haircut_salon":0,
"clothing_accessories":0,
"skincare_cosmentics":0,
"travel":0
}
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
def essentialsMenu_Display():#MENU DISPLAY ESSENTIALS(to avoid repetition)
    os.system('cls')
    print(welcomeMessage)
    print("-Essential Expenses-\n1. Rent/Mortgage Payment\n2. Electricity\n3. Water\n4. Gas/Heating\n5. Internet\n6. Phone \n7. Supermarket\n8. Exit")
    print(endBanner)
def non_essentialsMenu_Display():#MENU DISPLAY ESSENTIALS(to avoid repetition)
    os.system('cls')
    print(welcomeMessage)
    print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
    print(endBanner)
def expensesMenu_Display():
    os.system('cls')#clear screen before
    print(welcomeMessage)
    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
    print(endBanner)

def enterExpense():#ENTER EXPENSES method
    os.system('cls')#clear screen before
    print(welcomeMessage)
    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
    print(endBanner)
    while True:
        expenses_category=input(choice)

        if expenses_category=='3':#if CHOOSE to EXIT
            os.system('cls')#clear screen before breaking/going back to the previous menu
            break
        elif expenses_category=='1':#if CHOOSES ESSENTIAL 
            essentialsMenu_Display()
            while True:
                essential_option=input(choice)
                
                if essential_option=='8':#exit
                    os.system('cls')
                    expensesMenu_Display()
                    break
                elif essential_option == '1':
                    while True:
                        try:
                            essentialExpenses["rent"] = float(input("Enter your Rent/Mortgage Payment: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '2':
                    while True:
                        try:
                            essentialExpenses["electricity"] = float(input("Enter your Electricity cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '3':
                    while True:
                        try:
                            essentialExpenses["water"] = float(input("Enter your Water cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '4':
                    while True:
                        try:
                            essentialExpenses["gas"] = float(input("Enter your Gas/Heating cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '5':
                    while True:
                        try:
                            essentialExpenses["internet"] = float(input("Enter your Internet cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '6':
                    while True:
                        try:
                            essentialExpenses["phone"] = float(input("Enter your Phone cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif essential_option == '7':
                    while True:
                        try:
                            essentialExpenses["supermarket"] = float(input("Enter your Supermarket/Groceries cost: "))
                            essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                else:
                    os.system('cls')
                    print("Invalid option. Please choose a number between 1 and 8.")
                    print("-Essential Expenses-\n1. Rent/Mortgage Payment\n2. Electricity\n3. Water\n4. Gas/Heating\n5. Internet\n6. Phone \n7. Supermarket\n8. Exit")
                    print(endBanner)
        elif expenses_category=='2':#if CHOOSES NON-ESSENTIAL
            non_essentialsMenu_Display()
            while True:
                nonEssential_option=input(choice)
                if nonEssential_option=='9':#if CHOOSES to EXIT EXPENSES CATEGORIES
                    os.system('cls')
                    expensesMenu_Display()
                    break
                elif nonEssential_option=='1':
                    while True:
                        try:
                            non_essentialExpenses["dining_out"]=abs(float(input("Enter your Dining Out cost:")))#we can accept even negative numbs as expenses-->abs()method turning negative to positive
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='2':
                    while True:
                        try:
                            non_essentialExpenses["events"]=abs(float(input("Enter your Events cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='3':
                    while True:
                        try:
                            non_essentialExpenses["gym"]=abs(float(input("Enter your Gym Membership cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='4':
                    while True:
                        try:
                            non_essentialExpenses["streaming_services"]=abs(float(input("Enter your Streaming Services cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='5':
                    while True:
                        try:
                            non_essentialExpenses["haircut_salon"]=abs(float(input("Enter your Haircut and Salon cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='6':
                    while True:
                        try:
                            non_essentialExpenses["clothing_accessories"]=abs(float(input("Enter your Clothing and Accessories cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='7':
                    while True:
                        try:
                            non_essentialExpenses["skincare_cosmentics"]=abs(float(input("Enter your Skincare and Cosmetics cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='8':
                    while True:
                        try:
                            non_essentialExpenses["travel"]=abs(float(input("Enter your Travel expenses cost:")))
                            non_essentialsMenu_Display()
                        except ValueError:
                            print(inputError_str)
                else:
                    os.system('cls')
                    print("Invalid option. Please choose a number between 1 and 8.")
                    print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
                    print(endBanner)
        else:#WRONG INPUT
            os.system('cls')#clear screen before
            print("Invalid option. Please choose a number between 1 and 3.")
            print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
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
    #monthlyExpenses=None
    summary=0


    while True:
        optionFromMenu=input(choice)
        if optionFromMenu == '4':#EXIT
            
            return False #returns false to the main_menu to exit while loop.
            break
        elif optionFromMenu== '1':#ENTER INCOME
            monthlyIncome=enterIncome()#returns INCOME value
            mainMenuDisplay()
        elif optionFromMenu== '2':#ENTER EXPENSES
            os.system('cls')
            enterExpense() 
            #stores EXPENSES value and stores on var.
            mainMenuDisplay()
        elif optionFromMenu== '3':#SUMMATY
            if monthlyIncome is None:
                os.system('cls')
                print("Please enter both \"income\" and \"expenses\" before viewing the summary.\n")
                mainMenuDisplay()
            else:
                os.system('cls')
                essExp=sum(essentialExpenses.values())#summarry of values in the dictionary
                non_essExp=sum(non_essentialExpenses.values())# -||-
                monthlyExpenses= essExp-non_essExp
                summary=monthlyIncome-monthlyExpenses
                print(f"Summary: {summary}\nMonthly Income: {monthlyIncome}\nMonthly Expenses: {monthlyExpenses}")
                print(endBanner)
                print("Personal Finance Calculator")
                print("1. Main Menu\n2. Exit Program")
                print(endBanner)
                exitSummary=input(choice)
                if exitSummary=='2':
                    break
                elif exitSummary=='1':
                    os.system('cls')
                    mainMenuDisplay()
                else:
                    print(wrongInput)
        else:
            os.system('cls')#clear screen before
            print(wrongInput)
            print(choisesDisplay)
            print(endBanner)

#PROGRAM
while True:
    checker=main_menu()
    if checker== False:
        print(essentialExpenses, non_essentialExpenses)
        #print(monthlyIncome)
        print("Exiting...")
        break