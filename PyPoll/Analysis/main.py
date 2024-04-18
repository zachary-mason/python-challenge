import os
import csv

#create path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#define any and all variables
row_count = 0
winner_votes = 0
#cand_name = ''
candidate_list = []

#open, read the csv file and then skip the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #calculate the total number of votes by rows
    for row in csvreader:
        row_count +=1
    print(f"Total votes: {row_count}")

        #module 3.3 lists/dictionaires
      
        #if/else statement to tally votes and add cand names
        #if not already there
    
    #hannah and dan help   
    #if cand_name in candidate_list:
    
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        cand_name = row[2]
        
        if cand_name not in candidate_list:
            candidate_list.append(cand_name)
        
    print(f"Candidates List: ")

    for cand_name in candidate_list:
        print(f"{cand_name}")
