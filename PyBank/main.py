# Pybank
# Henry Poe
# Last changed: 03/17/2021

# Module for creating file paths
import os
# Module for reading CSV files
import csv
# Module for mean
from statistics import mean

# Create the path for our data set
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize some variable that need starting values
numMonths = 0
netProfit = 0
changes = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and file variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # Print all rows of the csv
        #print(row)
        
        # Set the current row to the 
        currentAmount = int(row[1])
        # Add current row to netProfit
        netProfit += currentAmount
        # Add the change from the previous row amount to the list of changes from month to month
        # previousAmount will not exist while we are on the first row(and the value in the first month isn't a change it's a starting value)
        if 'previousAmount' in globals():
            changes.append([row[0], currentAmount - previousAmount])        
        # Increment the number of months(rows)
        numMonths += 1
        # Set the previousAmount to the current right before moving to the next row
        previousAmount = currentAmount

    for row in changes:
        # Print all rows of the csv
        print(row)

# Calculate avg change/largest growth/largest loss
#for row in changes:
    
# Output
print("Financial Analysis\n----------------------")
print("Total Months:", numMonths)
print(f"Total: ${netProfit}")
