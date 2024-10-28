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

#Expenses MENU:
    #ESSENTIAL
        #CREATE ESSENTIAL CATEGORIES
        

    #NON-ESSENTIAL
        #CREATE NON ESSENTIAL CATEGORIES




def enterExpense():#ENTER EXPENSES method
    os.system('cls')#clear screen before
    print(welcomeMessage)
    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
    print(endBanner)
    #dictionary for ESSENTIAL EXPENSES
    essentialExpenses={
    "rent":0,
    "electricity":0,
    "water":0,
    "gas":0,
    "phone":0,
    "internet":0,
    "supermarket":0
    }
    #dictionary for NON-ESSENTIAL EXPENSES
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
    while True:
        expenses_category=input(choice)

        if expenses_category=='3':#if CHOOSE to EXIT
            os.system('cls')#clear screen before breaking/going back to the previous menu

            break
        elif expenses_category=='1':#if CHOOSES ESSENTIAL 
            os.system('cls')
            print(welcomeMessage)
            print("-Essential Expenses-\n1. Rent/Mortgage Payment\n2. Electricity\n3. Water\n4. Gas/Heating\n5. Internet\n6. Phone \n7. Supermarket\n8. Exit")
            print(endBanner)
            
            while True:
                essential_option=input(choice)
                if essential_option=='8':
                    os.system('cls')
                    print(welcomeMessage)
                    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
                    print(endBanner)
                    break
                elif essential_option == '1':
                    essentialExpenses["rent"] = float(input("Enter your Rent/Mortgage Payment: "))
                elif essential_option == '2':
                    essentialExpenses["electricity"] = float(input("Enter your Electricity cost: "))
                elif essential_option == '3':
                    essentialExpenses["water"] = float(input("Enter your Water cost: "))
                elif essential_option == '4':
                    essentialExpenses["gas"] = float(input("Enter your Gas/Heating cost: "))
                elif essential_option == '5':
                    essentialExpenses["internet"] = float(input("Enter your Internet cost: "))
                elif essential_option == '6':
                    essentialExpenses["phone"] = float(input("Enter your Phone cost: "))
                elif essential_option == '7':
                    essentialExpenses["supermarket"] = float(input("Enter your Supermarket/Groceries cost: "))
                else:
                    os.system('cls')
                    print("Invalid option. Please choose a number between 1 and 8.")
                    print("-Essential Expenses-\n1. Rent/Mortgage Payment\n2. Electricity\n3. Water\n4. Gas/Heating\n5. Internet\n6. Phone \n7. Supermarket\n8. Exit")
                    print(endBanner)
        elif expenses_category=='2':#if CHOOSES NON-ESSENTIAL
            os.system('cls')
            print(welcomeMessage)
            print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
            print(endBanner)

            while True:
                nonEssential_option=input(choice)
                if nonEssential_option=='9':
                    os.system('cls')
                    print(welcomeMessage)
                    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
                    print(endBanner)
                    break
                elif nonEssential_option=='1':
                    non_essentialExpenses["dining_out"]=abs(float(input("Enter your Dining Out cost:")))#we can accept even negative numbs as expenses-->abs()method turning negative to positive
                elif nonEssential_option=='2':
                    non_essentialExpenses["events"]=abs(float(input("Enter your Events cost:")))
                elif nonEssential_option=='3':
                    non_essentialExpenses["gym"]=abs(float(input("Enter your Gym Membership cost:")))
                elif nonEssential_option=='4':
                    non_essentialExpenses["streaming_services"]=abs(float(input("Enter your Streaming Services cost:")))
                elif nonEssential_option=='5':
                    non_essentialExpenses["haircut_salon"]=abs(float(input("Enter your Haircut and Salon cost:")))
                elif nonEssential_option=='6':
                    non_essentialExpenses["clothing_accessories"]=abs(float(input("Enter your Clothing and Accessories cost:")))
                elif nonEssential_option=='7':
                    non_essentialExpenses["skincare_cosmentics"]=abs(float(input("Enter your Skincare and Cosmetics cost:")))
                elif nonEssential_option=='8':
                    non_essentialExpenses["travel"]=abs(float(input("Enter your Travel expenses cost:")))
                else:
                    os.system('cls')
                    print("Invalid option. Please choose a number between 1 and 8.")
                    print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
                    print(endBanner)
        else:
            os.system('cls')#clear screen before
            print("Invalid option. Please choose a number between 1 and 3.")
            print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
            print(endBanner)
    return essentialExpenses, non_essentialExpenses #return the dictionaries to be used out of this method

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
        elif optionFromMenu== '2':
            os.system('cls')
            essentialExpenses, nonEssentialExpenses = enterExpense() #stores EXPENSES value and stores on var.
            mainMenuDisplay()
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
            os.system('cls')#clear screen before
            print(wrongInput)
            print(choisesDisplay)
            print(endBanner)

        

#PROGRAM
while True:
    checker=main_menu()
    if checker== False:
        print("Exiting...")
        break