import os
import csv

#create path
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#defin variable
total_net = 0
great_inc = 0
great_dec = 0
row_count = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
   # print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #for row in csvreader:
       # print(row)
    
    #total number of months
    for row in csvreader:
        row_count +=1
    print(f"Total Months: {row_count}")

with open(csvpath) as csvfile:
    header = next(csvfile)
    #total net $
    for row in csv.reader(csvfile):
        total_net +=int(row[1])
    print(f"Total: ${total_net}")

