# Total number of votes cast
# Complete list of candidates who received votes
# The percentage of votes each candidate won
# the total number of votes each candidate won
# the winner of the election based on popular vote

import os

import csv

# path for election data
csvpath = os.path.join('Resources', 'election_data.csv')


# Vote counter
total_votes_cast = 0

#candidate info 
complete_dictionary = {}
winner = ""
winning_vote_count = 0


with open (csvpath) as csvfile:
# csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    print(csvreader)

    # read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # skip the header row
    # first_row = next(csvreader)

    # begin the iteration
    for row in csvreader:
        # maintain the count of votes
        total_votes_cast = total_votes_cast + 1

        candidate_name = row[2]

        # update individual candidate vote counts
        complete_dictionary[candidate_name] = complete_dictionary.get(candidate_name, 0) + 1

        # vote count check
        if complete_dictionary[candidate_name] > winning_vote_count:
            winning_vote_count = complete_dictionary[candidate_name]
            winner = candidate_name


# the header for the results
# for candidate_name, votes in complete_dictionary.items():
#     percentage = (votes/total_votes_cast) * 100
    


election_heading = (
    f"\nElection Results\n"
    f"---------------------------------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"---------------------------------------------\n"
)
print(election_heading)

txtpath = os.path.join('Resources', 'election_data.txt')
with open(txtpath, 'w') as txt_file:
    
# export the analysis
    txt_file.write(election_heading)

    for candidate_name, votes in complete_dictionary.items():
        percentage = (votes/total_votes_cast) * 100

        voting_results = f"{candidate_name}: {percentage:.3f}% ({votes})\n"
        print(voting_results)
        txt_file.write(voting_results)

    candidate_votes =(
        # candidate_votes = (
        f"---------------------------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------------------------\n"
        # )
    )

    print(candidate_votes)


        
        # txt_file.write(voting_results)
    txt_file.write(candidate_votes)

    # print(candidate_votes) formatting changes
