import csv

# Define the file path
file_path = "/Users/davidtecuatl/Desktop/SS Bootcamp/python-challenge_-/Starter_Code-11/PyBank/Resources/budget_data.csv"

# Variables to store financial data
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # The total number of months included in the dataset
        total_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(profit_loss_change)
        previous_profit_loss = int(row[1])

        # The greatest increase in profits (date and amount) over the entire period
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # The greatest decrease in profits (date and amount) over the entire period
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average of changes in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the analysis results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
