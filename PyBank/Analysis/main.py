import os
import csv

#create path
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#define variable
total_net = 0
great_inc = 0
great_dec = 0
row_count = 0
prev_prof_loss = 0
rows = []
monthly_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #test to print out all rows in csv file
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
        
        prev_prof_loss = int(row[1])

    #test print for total number of 
    # months/rows in data and total net
    #print(f"Total Months: {row_count}")
    #print(f"Total: ${total_net}")

#may delete this entire chunk
#with open(csvpath) as csvfile:
    #header = next(csvfile)
    #total net $
    #for row in csv.reader(csvfile):
    #total_net += int(row[1])
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

print(f"Total Months: {row_count}")
print(f"Total: ${total_net}")
print(f"Average Change: ${rounded_avg_monthly_change}")