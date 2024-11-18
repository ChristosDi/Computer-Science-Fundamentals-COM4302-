import os #clear screen module
os.system('cls') #clear screen

#variables stored for menu DISPLAY
welcomeMessage=("Welcome to Personal Finance Calculator")

choisesDisplay=("1. Enter Income\n2. Add Expenses\n3. View Budget Summary\n4. Exit")
endBanner =("--------------------------------------------------------------------------------------------------------")
choice =("Enter your choice: ")
wrongInput=("***Invalid option. Please Try again***")
inputError_str=("Invalid Input!Please enter a number.")
ask_CalcPercentage=("Would you like to calculate the percentage of the remaining amount you would like to save?\nY--> Yes\nN--> No")


#dictionary for storing INCOME CATEGORIES
income={
"primarySalary":0,
"secondarySalary":0,
"bonuses":0,
"overtime":0,
"capitalGains":0,
"rentalIncome":0,
"selfEmployment":0,
"gift":0,
"taxRefund":0
}
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

#METHODS ONLY DISPLAYING MESSAGES FOR USER FRIENDLY EXP:
def essentialsMenu_Display():#MENU DISPLAY ESSENTIAL options(to avoid repetition)
    os.system('cls')
    print(welcomeMessage)
    print("-Essential Expenses-\n1. Rent/Mortgage Payment\n2. Electricity\n3. Water\n4. Gas/Heating\n5. Internet\n6. Phone \n7. Supermarket\n8. Exit")
    print(endBanner)
def non_essentialsMenu_Display():#MENU DISPLAY NON-ESSENTIALS options (to avoid repetition)
    os.system('cls')
    print(welcomeMessage)
    print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
    print(endBanner)
def expensesMenu_Display():#MENU DISPLAY EXPENSE categories essential-non
    os.system('cls')#clear screen before
    print(welcomeMessage)
    print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
    print(endBanner)
def mainMenuDisplay():#DISPLAY MAIN MENU options
    print("Welcome to Personal Finance Calculator")
    print(choisesDisplay)
    print(endBanner)
def enterIncomeMenu_Display():#MENU DISPLAY INCOME options
    os.system('cls')#clear screen before
    print(welcomeMessage)
    print("-Income Options-\n1. Primary Salary\n2. Secondary Salary\n3. Bonuses-Commissions\n4. Overtime Pay\n5. Capital Gains\n6. Rental Income\n7. Self-Employment Income\n8. Gift Money\n9. Tax Refund\n10. Exit")
    print(endBanner)
    
#METHODS PROVIDING FUNCTIONALITY OF THE PROGRAM:
def enterIncome():#ENTER INCOME method
    enterIncomeMenu_Display()
    while True:
        income_option=input(choice)
        
        if income_option =='10':#exit
            os.system('cls')
            break
        elif income_option == '1':
            while True:
                try:
                    income["primarySalary"] = float(input("Enter your Primary Salary income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '2':
            while True:
                try:
                    income["secondarySalary"] = float(input("Enter your Secondary Salary income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '3':
            while True:
                try:
                    income["bonuses"] = float(input("Enter your Bonus/Commision income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '4':
            while True:
                try:
                    income["ovetime"] = float(input("Enter your Overtime Pay income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '5':
            while True:
                try:
                    income["capitalGains"] = float(input("Enter your Capital Gains income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '6':
            while True:
                try:
                    income["rentalIncome"] = float(input("Enter your Rental Income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '7':
            while True:
                try:
                    income["selfEmployment"] = float(input("Enter your Self-Employment income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '8':
            while True:
                try:
                    income["gift"] = float(input("Enter your Gift Money income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)
        elif income_option == '9':
            while True:
                try:
                    income["taxRefund"] = float(input("Enter your Tax Refund income: "))
                    enterIncomeMenu_Display()
                    break
                except ValueError:
                    print(inputError_str)            
        else:
            os.system('cls')
            print("Invalid option. Please choose a number between 1 and 10.")
            print("-Income Options-\n1. Primary Salary\n2. Secondary Salary\n3. Bonuses-Commissions\n4. Overtime Pay\n5. Capital Gains\n6. Rental Income\n7. Self-Employment Income\n8. Gift Money\n9. Tax Refund\n10. Exit")
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
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='2':
                    while True:
                        try:
                            non_essentialExpenses["events"]=abs(float(input("Enter your Events cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='3':
                    while True:
                        try:
                            non_essentialExpenses["gym"]=abs(float(input("Enter your Gym Membership cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='4':
                    while True:
                        try:
                            non_essentialExpenses["streaming_services"]=abs(float(input("Enter your Streaming Services cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='5':
                    while True:
                        try:
                            non_essentialExpenses["haircut_salon"]=abs(float(input("Enter your Haircut and Salon cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='6':
                    while True:
                        try:
                            non_essentialExpenses["clothing_accessories"]=abs(float(input("Enter your Clothing and Accessories cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='7':
                    while True:
                        try:
                            non_essentialExpenses["skincare_cosmentics"]=abs(float(input("Enter your Skincare and Cosmetics cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                elif nonEssential_option=='8':
                    while True:
                        try:
                            non_essentialExpenses["travel"]=abs(float(input("Enter your Travel expenses cost:")))
                            non_essentialsMenu_Display()
                            break
                        except ValueError:
                            print(inputError_str)
                else:
                    os.system('cls')
                    print("Invalid option. Please choose a number between 1 and 9.")
                    print("-Non-Essential Expenses-\n1. Dining out\n2. Events\n3. Gym membership\n4. Streaming services (Netflix, Spotify, etc.)\n5. Haircuts and salon visits\n6. Clothing and accessories\n7. Skincare and cosmetics\n8. Travel expenses\n9. Exit")
                    print(endBanner)
        else:#WRONG INPUT
            os.system('cls')#clear screen before
            print("Invalid option. Please choose a number between 1 and 3.")
            print("-Expenses Categories-\n1. Essential\n2. Non-Essential\n3. Exit")
            print(endBanner)
def summaryBudget():#SUMMARISE BUDGET
    while True:
        #INCOME Summary :
        incomeSum=float(sum(income.values()))#Summary of the Income dictionary
        #Summary of the Expenses list :
        essentExp=sum(essentialExpenses.values())#summarry of values in the dictionary ESSENTIALS
        non_essentExp=sum(non_essentialExpenses.values())# -||- NON-ESSENTIALS
        #TOTAL MONTHLY EXPENSES summary:
        totalMonthlyExp= float(essentExp+non_essentExp)#DISPLAY as FLOAT
        #Remaining Amount after expenses deducted from income:
        remainingAmount=incomeSum-totalMonthlyExp

        print(welcomeMessage)
        print(f"Monthly Income: {incomeSum}\nTotal Monthly Expenses: {totalMonthlyExp}\nRemaining Budget: {remainingAmount}")
        print(endBanner)

        if totalMonthlyExp>incomeSum:#INCOME LESS THAN EXPENSES
                print(f"You are {remainingAmount} over the budget.")
                #sorting dictionary from the greatest value in descending order, excluding zero values
                sorted_nonEssentials = sorted(((k, v) for k, v in non_essentialExpenses.items() if v > 0), key=lambda item: item[1], reverse=True)
                sorted_essentials = sorted(((k, v) for k, v in essentialExpenses.items() if v > 0), key=lambda item: item[1], reverse=True)
                print("Consider reducing the following expenses to stay within budget:")
                # DISPLAY the sorted list with userfriendly names
                if sorted_nonEssentials:#DISPLAY only the values that don't have zeros(0)
                    print("Non-Essential expenses:")
                    for expense, cost in sorted_nonEssentials:
                        print(f"- {expense.replace('_', ' ').title()}: {cost}")#PRINT NON-ESSENTIAL
                else:
                    print("No non-essential expenses recorded.")
                if sorted_essentials:
                    print("Essential expenses:")
                    for expense, cost in sorted_essentials:
                        print(f"- {expense.title()}: {cost}")#PRINT ESSENTIAL
                else:
                    print("No essential expenses recorded.")        
        elif totalMonthlyExp<incomeSum:#INCOME MORE THAN EXPENSES
            remaining_percentage=(remainingAmount/incomeSum)*100 #FORMULA TO CALCULATE how much percentage of income is left
            print(f"You are under the budget.\nYour remaining amount is: {remainingAmount} which is {remaining_percentage:.2f}% of your income.") #string formating method to control the number of decimal places(:2f)
            #RECOMMENDATIONS BASED ON BUDGET STATUS
            if remaining_percentage<=25:
                print("You're running low on your budget. Consider reducing non-essential spending to avoid overspending.")
            elif remaining_percentage<=50:
                print("You're halfway through your budget. Keep monitoring your expenses to ensure you stay on track.")
            elif remaining_percentage<=75:
                print("Good job! You have a healthy portion of your budget remaining.")
            elif remaining_percentage<100:
                print("Excellent! You still have a large portion of your budget left. This is a great opportunity to increase your savings.")
            elif remaining_percentage>=100:
                print("Amazing! You stayed completely within your budget. Consider transferring the surplus to savings or investments.")
            
            print(ask_CalcPercentage)
            print(endBanner)
            while True:
                choiceForPercentage=input(choice).upper()
                if choiceForPercentage=='N':
                    os.system('cls')
                    print(welcomeMessage)
                    break
                elif choiceForPercentage=='Y':
                    os.system('cls')
                    print(welcomeMessage)
                    while True:
                        try:
                            global percentageCalc
                            percentageCalc=int(input(f"Please write the percentage of {remainingAmount} that you would like to save: "))
                            if percentageCalc>100:
                                os.system('cls')
                                print(f"You have asked to save {percentageCalc}%.\nYou can save up to 100% which is the full amount of {remainingAmount}. Please try again.")
                            elif 0<percentageCalc<=100:
                                global calculation
                                calculation=remainingAmount*percentageCalc/100
                                os.system('cls')
                                print(welcomeMessage)
                                print(f"{percentageCalc}% of {remainingAmount} is the amount of {calculation}! ")
                                print("Would you like to calculate the percentage of the remaining amount again?\nY--> Yes\nN--> No")
                                break
                            else:
                                os.system('cls')
                                print(welcomeMessage)
                                print("Please enter a positive percentage value.")
                                
                        except:
                            os.system('cls')
                            print(welcomeMessage)
                            print(inputError_str)
                else:
                    os.system('cls')
                    print(wrongInput)
                    print(welcomeMessage)
                    print(ask_CalcPercentage)
        elif totalMonthlyExp==incomeSum:#INCOME AND EXPNSES EQUAL
            print("You are neither over nor under budget.")#IF INCOME IS 0 DISPLAYS ONLY THIS MESSAGE
            if incomeSum>0:#IF HAVING INCOME
                print("You're exactly on budget! Keep up the good work managing your expenses carefully. Consider setting aside any extra income in a savings account or toward an emergency fund.")
        print(endBanner)
        print("Personal Finance Calculator")
        print("1. Main Menu\n2. Exit Program")
        print(endBanner)
        exitSummary=input(choice)
        if exitSummary=='2':
            os.system('cls')
            return False
        elif exitSummary=='1':#goes back to MAIN MENU
            os.system('cls')
            mainMenuDisplay()
            break
        else:
            os.system('cls')
            print(wrongInput)
#MAIN MENU
def main_menu():#function to CALL MAIN MENU with functionality 
    mainMenuDisplay()#DISPLAY main menu
    #initialise
    global monthlyIncome #updates the monthlyIncome variable which is public
    summary=0


    while True:
        optionFromMenu=input(choice)
        if optionFromMenu == '4':#EXIT
            return False #returns false to the main_menu to exit while loop.
        elif optionFromMenu== '1':#ENTER INCOME
            monthlyIncome=enterIncome()#returns  monthly INCOME value
            mainMenuDisplay()
        elif optionFromMenu== '2':#ENTER EXPENSES
            os.system('cls')
            monthlyExpenses=enterExpense()#stores EXPENSES value and stores on var..
            mainMenuDisplay()
        elif optionFromMenu== '3':#SUMMARY
            os.system('cls')
            budgetSum=summaryBudget()
            if budgetSum==False:
                return False
            else:
                continue
        else:
            os.system('cls')#clear screen before
            print(wrongInput)
            print(choisesDisplay)
            print(endBanner)

#PROGRAM
while True:
    checker=main_menu()
    if checker== False:#IF INPUT on the MAIN menu is 4 will RETURN FALSE
        os.system('cls')
        print("Thank you for using Personal Finance Calculator!")#Bellow analysis of INCOME, EXPENSES etc will print
        #Sort from the Greatest value:
        sorted_Income = sorted(((k, v) for k, v in income.items() if v > 0), key=lambda item: item[1], reverse=True)
        #DISPLAY the sorted dict with userfriendly names,
        if sorted_Income:#DISPLAY only the values that don't have zeros(0)
            print("Your Income sources:")
            for incomes, cost in sorted_Income:
                print(f"- {incomes.replace('_', ' ').title()}: {cost}")#PRINT INCOME
        #DISPLAY EXPENSES:
        sorted_nonEssentials = sorted(((k, v) for k, v in non_essentialExpenses.items() if v > 0), key=lambda item: item[1], reverse=True)
        sorted_essentials = sorted(((k, v) for k, v in essentialExpenses.items() if v > 0), key=lambda item: item[1], reverse=True)
        # DISPLAY the sorted list with userfriendly names
        if sorted_nonEssentials:#DISPLAY only the values that don't have zeros(0)
            print("Your Non-Essential expenses:")
            for expense, cost in sorted_nonEssentials:
                print(f"- {expense.replace('_', ' ').title()}: {cost}")#PRINT NON-ESSENTIAL
        else:
            print("No non-essential expenses recorded.")
        if sorted_essentials:
            print("Your Essential expenses:")
            for expense, cost in sorted_essentials:
                print(f"- {expense.title()}: {cost}")#PRINT ESSENTIAL
        else:
            print("No essential expenses recorded.")

        if calculation:
            print(f"You asked to save {percentageCalc}% of your income:{calculation} ")     
        break