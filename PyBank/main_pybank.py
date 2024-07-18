# OS & CSV

import os
import csv

# Path for CSV

PyBankcsv = os.path.join('..', 'Resources', 'budget_data.csv')

# Lists for data

profit = []
monthly_changes = []
date = []

# Initialize counts
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open and read CSV

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Counting rows
    for row in csvreader:    
      count = count + 1 

      # Row Name
      date.append(row[0])

      # Append for total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculation for final profit
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Monthly change storage
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculation for average chg profits
      average_change_profits = (total_change_profits/count)
      
      #Calculation for increase and decrease of profits
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
