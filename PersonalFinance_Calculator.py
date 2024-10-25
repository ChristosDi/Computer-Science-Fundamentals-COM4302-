import csv #import CSV module
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
