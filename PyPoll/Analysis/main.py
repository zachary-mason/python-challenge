import os
import csv

#create path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#define any and all variables
row_count = 0
winner_votes = 0
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
    #delete this dupe section right below
    #if cand_name not in candidate_votes:
    #    candidate_votes[cand_name] = 1
    #else:
    #    candidate_votes[cand_name] += 1

    for cand_name in candidate_list:
        print(f"{cand_name}")

    # Calculate and print the percentage of votes each candidate received
    print("Percentage of votes per candidate:")
    for cand_name in candidate_list:
        votes = cand_votes[cand_name]
        percent_votes = (votes / row_count) * 100
        print(f"{cand_name} : {percent_votes:.3f}% ({votes})")
