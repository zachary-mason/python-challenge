import os
import csv

#create path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#define any and all variables
row_count = 0
winner_votes = 0
winner = ''
cand_name = ''
candidate_list = []
cand_votes = {}

#open, read the csv file and then skip the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #calculate the total number of votes by rows
    for row in csvreader:
        row_count +=1
    print(f"Total Votes: {row_count}")

    #module 3.3 lists/dictionaires
    #hannah and dan help   
    #if cand_name in candidate_list:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        cand_name = row[2]
        
        if cand_name not in candidate_list:
            candidate_list.append(cand_name)
        
        if cand_name not in cand_votes:
            cand_votes[cand_name] = 1
        else:
            cand_votes[cand_name] += 1
    print(f"Candidates List: ")

    for cand_name in candidate_list:
        print(f"{cand_name}")

    # Calculate and print the percentage of votes each candidate received
    print("Percentage of votes per candidate:")
    for cand_name in candidate_list:
        votes = cand_votes[cand_name]
        percent_votes = (votes / row_count) * 100
        print(f"{cand_name} : {percent_votes:.3f}% ({votes})")

    #analyze the votes per candidate and find the winner of of election based on pop vote
    #for cand_name in candidate_list:
        
        if votes > winner_votes:
            winner = cand_name
            winner_votes = votes
print(f"{winner}")

#printing to terminal
print("Election Results")
print("----------------------------")
#print("Total Months: " + f"{row_count}")
print("----------------------------")
#print("Total: " + f"${total_net}")
#print("Average Change: " + f"${rounded_avg_monthly_change}")
#print("Greatest Increase in Profits: " + f"{great_inc_date} (${great_inc_change})")
#print("Greatest Decrease in Profits: " + f"{great_dec_date} (${great_dec_change})")

#output text file with results matching module instructions
#output_file = os.path.join('PyBank','Analysis','analysis.txt')
#with open(output_file, 'w') as txtfile:
#    results_file = csv.writer(txtfile, delimiter=',')
#    results_file.writerow(["Financial Analysis"])
#   results_file.writerow(["----------------------------"])
 #   results_file.writerow(["Total Months: " + f"{row_count}"])
 #   results_file.writerow(["Total: " + f"${total_net}"])
 #   results_file.writerow(["Average Change: " + f"${rounded_avg_monthly_change}"])
 #   results_file.writerow(["Greatest Increase in Profits: " + f"{great_inc_date}" + " (" + f"${great_inc_change}" + ")"])
 #   results_file.writerow(["Greatest Decrease in Profits: " + f"{great_dec_date}" + " (" + f"${great_dec_change}" + ")"])