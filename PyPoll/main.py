# File path
file = r'C:\\Users\\Chase\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv'

import csv

# Variables
total_votes = 0
candidates = {} #dict of candidates
winner = ""
winner_votes = 0

# Open CSV, read data
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the rows
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1

        # Read candidate name
        candidate = row[2]

        # If this is the first vote for this candidate, add them to the dictionary
        if candidate not in candidates:
            candidates[candidate] = 0

        # Increment the candidate's vote count
        candidates[candidate] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through the candidates and calculate their percentage of the vote
for candidate in candidates:
    votes = candidates[candidate]
    percent = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percent}% ({votes})")

    # Check if this candidate has the most votes so far
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open(r'C:\\Users\\Chase\\Desktop\\python-challenge\\PyPoll\\analysis\\election_results.txt', "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        votes = candidates[candidate]
        percent = round((votes / total_votes) * 100, 3)
        txtfile.write(f"{candidate}: {percent}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
