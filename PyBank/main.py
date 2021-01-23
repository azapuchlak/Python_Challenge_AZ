# Modules
import os
import csv

# Open the CSV & Name the File
with open("budget_data.csv") as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")

    #Skip Header of CSV File
    next(budgetdata)

    # Question 1 - 
    #Gather the total number of months included in the dataset
    #Add loop for month count
    #Get month count - Setting aside a place to add
    month_count = []
    
    # Question 2 -
    #Get sum of profits and losses
    sum_rev = []
    #loop through CSV to get both total number of months and the sum of profits and losses in the budget data 
    for row in budgetdata:
        month_count.append(row[0])
        sum_rev.append(int(row[1]))

    # Question 3 -
    # Calculate the changes in profits and losses 
    monthly_changes = []
    for revenue_row in range(len(sum_rev)-1):
        #Loop through the sum revenue list by taking the second number and subtracting the
        #first number until you reach the end of the list... Add to monthly changes list.
        monthly_changes.append(int(sum_rev[revenue_row+1]-sum_rev[revenue_row]))

    # Question 4/5 -
    #Calculate the maximum/minimum increase in profits. Report it along side the date it occured.
    max_number = max(monthly_changes)

    min_number = min(monthly_changes)

    #Get the correlating months for the correlating Max - The +1 works because the differece is in the next month.
    max_number_increase = monthly_changes.index(max(monthly_changes))+1

    #Get the correlating months for the correlating Min - Again, the +1 is necessary because the difference takes place in the following month.
    min_number_decrease = monthly_changes.index(min(monthly_changes))+1
#--------------------------------------------------------------------------------------------------------------------------------------------
    #Print totals of all calculations
    print(f"Total Months: {len(month_count)}")
    print(f"Total Revenue: ${sum(sum_rev)}")
    #Taking the sum of the monthly changes and dividing it by the length of the monthly change list.
    #Round in the beginning is closed by 2 at the end to trigger round to two decimal places.
    print(f"Average Change: ${round(sum(monthly_changes)/len(monthly_changes),2)}")
    # Print is where we will add in the code to pull the month from the index. 
    print(f"Greatest Increase in Profits: {month_count[max_number_increase]} (${str(max_number)})")
    print(f"Greatest Decrease in Profits: {month_count[min_number_decrease]} (${str(min_number)})")

#---------------------------------------------------------------------------------------------------------------------------------------------
    # Create New File 
    # note - W means write - open this file and if it doesn't exist write a new one

    file = open("results.txt", "w")

    #Write lines over to the new file created
    # note - \n helps split it into new lines
    file.write("Financial Analysis"+"\n")
    file.write("------------------"+"\n")
    file.write(f"Total Months: {len(month_count)}"+"\n")
    file.write(f"Total Revenue: ${sum(sum_rev)}"+"\n")
    file.write(f"Average Change: ${round(sum(monthly_changes)/len(monthly_changes),2)}"+"\n")
    file.write(f"Greatest Increase in Profits: {month_count[max_number_increase]} (${str(max_number)})"+"\n")
    file.write(f"Greatest Decrease in Profits: {month_count[min_number_decrease]} (${str(min_number)})"+"\n")


 


   
      





