# PyPoll
# Henry Poe
# Last changed: 03/20/2021

# Module for creating file paths
import os
# Module for reading CSV files
import csv

numVotes = 0
voteCounter = []

# Create the path for our data set
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and file variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # Count every vote
        numVotes += 1
        # Reset the index for the vote counter list to our value for adding a first vote for a candidate to the list
        counterIndex = -1
        for count, rowCounter in enumerate(voteCounter):
            if row[2] == rowCounter[0]:
                # Set the index for our vote counter to the index of the candidate the vote from the list was for
                counterIndex = count
        
        if counterIndex == -1:        
            voteCounter.append([row[2], 1])
        else:
            voteCounter[counterIndex][1] += 1
            
# Output
winningVotes = 0
print("Election Results\n------------------------")
print(f"Total Votes: {numVotes}\n------------------------")
for row in voteCounter:
    print("{}: {:.2f}% ({})".format(row[0], row[1]/numVotes*100, row[1]))
    if row[1] > winningVotes:
        winner = row[0]
        winningVotes = row[1]
print(f"------------------------\nWinner: {winner}\n------------------------")

output_path = os.path.join('Analysis', 'output.txt')
with open(output_path, 'w') as file:
    file.write("Election Results\n------------------------\n")
    file.write(f"Total Votes: {numVotes}\n------------------------\n")
    for row in voteCounter:
        file.write("{}: {:.3f}% ({})\n".format(row[0], row[1]/numVotes*100, row[1]))
    file.write(f"------------------------\nWinner: {winner}\n------------------------\n")
