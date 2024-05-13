import csv

# Define the file path
file_path = "/Users/davidtecuatl/Desktop/SS Bootcamp/python-challenge_-/Starter_Code-11/PyPoll/Resources/election_data.csv"

# Initialize variables to store election data
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Count total number of votes
        total_votes += 1

        # Collect candidate names and their respective vote counts
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {
        "votes": votes,
        "percentage": percentage
    }

# Determine the winner of the election based on popular vote
winner = max(candidates, key=lambda x: candidates[x]['votes'])

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the analysis results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, data in candidates.items():
        txtfile.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
