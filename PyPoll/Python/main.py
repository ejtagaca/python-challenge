import os
import csv

election_csv = os.path.join("..","Resources", "election_data.csv")

#things we need to print
candidate = []
votes = []
percent_votes = []
winner = 0
winner_votes = 0
total_votes = 0

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(csv_reader, None)

    # Read through each row of data after the header
    for row in csv_reader:

        # reads our current known candidates
        if row[2] not in candidate:
            #if it is not, adds it to our known candidates
            candidate.append(row[2])
            votes.append(0)
            percent_votes.append(0)
        candidate_len = len(candidate)
        for index in range(candidate_len):
            # since the length of the votes and candidates are the same, this is ok
            if candidate[index] == row[2]:
                votes[index] = votes[index] + 1;


candidate_len = len(candidate)
votes_len = len(votes)

#finds winner and total vote count
for index in range(votes_len):
    if votes[index] > winner_votes:
        winner = index
        winner_votes = votes[index]
    total_votes = total_votes + votes[index]

#finds percent votes for each candidate
for index in range(votes_len):
    percent_votes[index] = round(votes[index]/total_votes*100,3)

#prints into terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for index in range(candidate_len):
    print(candidate[index] + ": " + str(percent_votes[index]) + "% (" + str(votes[index]) + ")")
print("-------------------------")
print("Winner: " + candidate[winner])
print("-------------------------")

#prints into file
with open('../Output/output.txt', 'w') as text_file:
    print("Election Results",file=text_file)
    print("-------------------------",file=text_file)
    print("Total Votes: " + str(total_votes),file=text_file)
    print("-------------------------",file=text_file)
    for index in range(candidate_len):
        print(candidate[index] + ": " + str(percent_votes[index]) + "% (" + str(votes[index]) + ")",file=text_file)
    print("-------------------------",file=text_file)
    print("Winner: " + candidate[winner],file=text_file)
    print("-------------------------",file=text_file)
