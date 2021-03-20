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

# Initialize some variable with their starting values
numMonths = 0
total = 0
#previousAmount = 0
bigProfit = 0
bigLoss = 0
changes = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and file variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        #Set the current row to the 
        currentAmount = int(row[1])
        #Add current row to total
        total += currentAmount
        #Check for largest Profit
        if currentAmount > bigProfit:
            bigProfit = currentAmount
        #Check for largest Loss
        if currentAmount < bigLoss:
            bigLoss = currentAmount
        #Add the change from the previous row amount to the list
        if 'previousAmount' in globals():
            changes.append(currentAmount - previousAmount)        
        #Increment the number of months(rows)
        numMonths += 1
        #Set the previousAmount to the current for the next row
        previousAmount = currentAmount

# Remove the first item of the changes list
# (The first value in the csv is a starting value not an increase from 0)        
#changes.pop(0)
#Output
print("Financial Analysis\n----------------------")
print("Total Months:", numMonths)
print(f"Total: ${total}")
print(f"Average Change: ${mean(changes)}")