# This module helps us create a file path across operating systems
# Find the following:
# total number of months included in the dataset
# Net total amount of Profit/losses over the entire period
# changes in the profit/losses over the entire period, and then the average of those changes
# the greatest increase in profits (date and amount) over the entire period
# the greatest decrease in profits (date and maount) over the entire period

import os
# Module for reading CSV files
import csv

# path for budget data csv and txt file
csvpath = os.path.join('Resources', 'budget_data.csv')


# Info we're finding
total_months = 0
net_total_profit = 0
prior_net_profit = 0
iterative_change_list = []
months = []


with open(csvpath) as csvfile:

# csv reader specifies delimiter and vriable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# print(csvreader)
    print(csvreader)

# read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    first_row = next(csvreader)
    total_months += 1
    net_total_profit += int(first_row[1])
    prior_net_profit = int(first_row[1])

# Read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        date = row[0]
        profit_loss=int(row[1])

        # prior_net_profit = int(row[1])
        # calculate net profit
        # net_total_profit = int(row[1]) + net_total_profit
        net_total_profit += profit_loss



        # calculate iterative profit/losses as  the loop goes through the code
        delta = profit_loss - prior_net_profit
        iterative_change_list.append(delta)
        months.append(date)
        
        #iteration for the next month
        prior_net_profit = profit_loss
        # denominator = len(iterative_change_list) - 1


        # prior_net_profit = int(row[1])
        

average_delta = sum(iterative_change_list) / len(iterative_change_list)

greatest_increase = max(iterative_change_list)
greatest_decrease = min(iterative_change_list)
       
 #month of the greatest increase and decrease
month_greatest_increase = months[iterative_change_list.index(greatest_increase)]
month_greatest_decrease = months[iterative_change_list.index(greatest_decrease)]

# analysis of financial records
output = (
f"\nFinancial Analysis\n"
f"______________________\n"
f"Total Months: {total_months}\n"
f"Total: ${net_total_profit}\n"
f"Average Change: ${average_delta:.2f}\n"
f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})\n"
)

print(output)
# Export the analysis to a txt file titled analysis
txtpath = os.path.join('Resources', 'Analysis.txt')
with open(txtpath, 'w') as txt_file:
    txt_file.write(output)

