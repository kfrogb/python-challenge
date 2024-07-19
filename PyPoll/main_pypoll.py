# PyPoll Project: Main Python file
## CSV file contains 3 columns: Ballot ID (Col 0), County (Col 1), and Candidate (Col 2)

# Create file paths across operating systems
import os

# module for reading CSV files
import csv

# CSV file path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Storage lists
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
rounded_percentage = []

# Open the CSV 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Each row
    for row in csvreader:
        # No of votes
        count = count + 1
        # container for candidate names
        candidatelist.append(row[2])
        # unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y = ttl votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z = percent of ttl votes per candidate
        z = (y/count)*100
        vote_percent.append(z)


winning_vote_count = max(vote_count)
winner = unique_candidate[vote_count.index(winning_vote_count)]

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")

# Checking for length
if len(unique_candidate) == len(vote_percent) == len(vote_count):
    # For loop
    for i in range(len(unique_candidate)):
        print(f"{unique_candidate[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})")
else:
    print("Error: Lists have different lengths.")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


# Printing text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")