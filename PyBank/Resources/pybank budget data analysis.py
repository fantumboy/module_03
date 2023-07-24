import os
import csv
budget_data = os.path.join('/Users/theresakim/Documents/northwestern/module 03 python/Starter_Code/PyBank/Resources/budget_data.csv')

clean_dates = []
clean_revenue = []
rev_delta = 0
max_delta = [0, 0]
min_delta = [0, 0]
net_total = 0

with open(budget_data, 'r') as file:

        csvreader = csv.reader(file)
        header = next(csvreader)

        for row in csvreader:
                date = row[0]
                revenue = row[1]
                clean_dates.append(date)
                clean_revenue.append(revenue)

total_months = len(clean_dates)

for i in range(1, total_months):
        rev_delta = int(clean_revenue[i]) - int(clean_revenue[i-1])
        net_total += rev_delta
        if rev_delta > max_delta[1]:
                max_delta = [clean_dates[i], rev_delta]
        if rev_delta < min_delta[1]:
                min_delta = [clean_dates[i], rev_delta]

average_delta = (max_delta[1] - min_delta[1]) / total_months

print("")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_delta}")
print(f"Greatest Increase in Profits: ${max_delta}")
print(f"Greatest Decrease in Profits: ${min_delta}")

file_to_output = os.path.join('/Users/theresakim/Documents/northwestern/module 03 python/Starter_Code/PyBank/Resources/output_budget_data.txt')

with open(file_to_output, "w") as out:
        out.write("\n")
        out.write("Financial Analysis\n")
        out.write("-----------------------------\n")
        out.write(f"Total Months: {total_months}\n")
        out.write(f"Total: ${net_total}\n")
        out.write(f"Average Change: ${average_delta}\n")
        out.write(f"Greatest Increase in Profits: ${max_delta}\n")
        out.write(f"Greatest Decrease in Profits: ${min_delta}\n")
        out.close()
