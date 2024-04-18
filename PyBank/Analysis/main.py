import os
import csv

#create path
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#define variable
total_net = 0
great_inc_change = 0
great_dec_change = 0
great_inc_date = ''
great_dec_date = ''
row_count = 0
prev_prof_loss = 0
rows = []
monthly_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #test to see if able to read csv correctly
    #for rows in csvreader:
    #    print(rows)
    
    #had some help from Xpert learning assistance here
    # and the avg change/monthly change
    #counting the rows and total profit/loss 
    #as it goes down the file
    
    for row in csvreader:
        row_count +=1
        total_net += int(row[1])

        if row_count > 1:
            month_change = int(row[1]) - (prev_prof_loss)
            monthly_change.append(month_change)

            #if statement to find max and min date and value
            if month_change > great_inc_change:
                great_inc_change = month_change
                great_inc_date = row[0]
                #great_inc_change = row[1]
            elif month_change < great_dec_change:
                great_dec_change = month_change
                great_dec_date = row[0]
                #great_inc_change = row[1]

        prev_prof_loss = int(row[1])
    
    #testing the great inc/dec
        #print(great_inc_change)
        #print(great_inc_date)
        #print(great_dec_change)
        #print(great_dec_date)
    
    #test print for total number of 
    # months/rows in data and total net
    #print(f"Total Months: {row_count}")
    #print(f"Total: ${total_net}")

    #for row in csv.reader(csvfile):
    #    if row_count > 1:
    #       month_change = int(row[1]) - prev_prof_loss
    #       monthly_change.append(monthly_change)
    
    #   prev_prof_loss = int(row[1])

#average monthly change set up and round to 2 decimal points
avg_monthly_change = sum(monthly_change) / len(monthly_change)
rounded_avg_monthly_change = round(avg_monthly_change, 2)
#print(rounded_avg_monthly_change)            

#printing to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + f"{row_count}")
print("Total: " + f"${total_net}")
print("Average Change: " + f"${rounded_avg_monthly_change}")
print("Greatest Increase in Profits: " + f"{great_inc_date} (${great_inc_change})")
print("Greatest Decrease in Profits: " + f"{great_dec_date} (${great_dec_change})")

#module 3.2 slides/activities - first attempt
output_file = os.path.join('PyBank','Analysis','results.csv')
with open(output_file, 'w') as csvfile:
    results_file = csv.writer(csvfile, delimiter=',')
    results_file.writerow(["Financial Analysis"])
    results_file.writerow(["----------------------------"])
    results_file.writerow(["Total Months: " + f"{row_count}"])
    results_file.writerow(["Total: " + f"${total_net}"])
    results_file.writerow(["Average Change: " + f"${rounded_avg_monthly_change}"])
    results_file.writerow(["Greatest Increase in Profits: " + f"{great_inc_date}" + " (" + f"${great_inc_change}" + ")"])
    results_file.writerow(["Greatest Decrease in Profits: " + f"{great_dec_date}" + " (" + f"${great_dec_change}" + ")"])

#printing out all to check results shown on the assignment
#print(f"Total Months: {row_count}")
#print(f"Total: ${total_net}")
#print(f"Average Change: ${rounded_avg_monthly_change}")