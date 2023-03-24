# File path
file = r"C:\\Users\\Chase\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv"

import csv

# Make lists
dates = []
profits_losses = []

# Add data to lists
with open(file) as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file, delimiter=",")
    next(budget_data_reader)  # Skip the header row
    for row in budget_data_reader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the total number of months included in the dataset
total_months = len(dates)

# Calculate the net total amount of profits and losses
net_total = sum(profits_losses)

# Calculate the changes in profits/losses, get average
changes = []
for i in range(1, len(profits_losses)):
    changes.append(profits_losses[i] - profits_losses[i - 1])
average_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

# Calculate the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export a text file with the results
with open(r"C:\\Users\\Chase\\Desktop\\python-challenge\\PyBank\\analysis\\financial_analysis.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
