import os
import csv

#create path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

candidates = []
row_count = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #total number of votes
    for row in csvreader:
        row_count +=1
    print(f"Total votes: {row_count}")

#with open(csvpath, 'r') as csvfile:
   # header = next(csvfile)
    #cand_list = [candidate[2] for candidate in csvreader]
    #cand_info = [[candidate,cand_list.count(candidate)] 
     #                  for candidate in set(cand_list)]
    #print()

   # for row in csvreader:
        
