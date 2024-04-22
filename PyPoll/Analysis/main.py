#import the modules
import os
import csv

#create path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#define any and all variables
row_count = 0 #vote count
winner_votes = 0
winner = ''
cand_name = ''
candidate_list = []
cand_votes = {}

#open, read the csv file, and then store the header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #calculate the total number of votes (total number of rows skipping the header)
    for row in csvreader:
        row_count +=1

#reading the csv file and creating list of candidates, counting votes per candidate
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
    
    #Calculate and store the percentage of votes each candidate received
    for cand_name in candidate_list:
        votes = cand_votes[cand_name]
        percent_votes = (votes / row_count) * 100
        
    #analyze the votes per candidate and find the winner of  election based on pop vote
        if votes > winner_votes:
            winner = cand_name
            winner_votes = votes

#printing results to terminal
print("Election Results")
print("----------------------------")
print("Total Votes: " + f"{row_count}")
print("----------------------------")
for cand_name in candidate_list:
        votes = cand_votes[cand_name]
        percent_votes = (votes / row_count) * 100
        print(f"{cand_name}: {percent_votes:.3f}% ({votes})")
print("----------------------------")
print("Winner: " + f"{winner}")
print("----------------------------")

#create an output text file with results matching module instructions
results_file = os.path.join('PyPoll','Analysis','analysis.txt')
with open(results_file, 'w') as txtfile:
    results_file = csv.writer(txtfile)
    results_file.writerow(["Election Results"])
    results_file.writerow(["----------------------------"])
    results_file.writerow(["Total Votes: " + f"{row_count}"])
    results_file.writerow(["----------------------------"])
    for cand_name in candidate_list:
        votes = cand_votes[cand_name]
        percent_votes = (votes / row_count) * 100
        results_file.writerow([f"{cand_name}: {percent_votes:.3f}% ({votes})"])
    results_file.writerow(["----------------------------"])
    results_file.writerow(["Winner: " + f"{winner}"])
    results_file.writerow(["----------------------------"])
