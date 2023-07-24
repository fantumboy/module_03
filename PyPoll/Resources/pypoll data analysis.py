import os
import csv
poll_data = os.path.join('/Users/theresakim/Documents/northwestern/module 03 python/Starter_Code/PyPoll/Resources/election_data.csv')

vote_count = []
candidate_names = []
candidate_votes = {}
percent = {}
highest_vote = 0

with open(poll_data, 'r') as file:

# inspiration from:
#   https://blog.finxter.com/convert-csv-to-dictionary-in-python/

    csvreader = csv.DictReader(file)

    for row in csvreader:
        candidate = row['Candidate']
        ballotid = row['Ballot ID']
        vote_count.append(ballotid)

        total_votes = len(vote_count)

# found serendipitiously at https://realpython.com/python-in-operator/

        if candidate not in candidate_names: #which candidate_names is new list being created
            candidate_names.append(candidate)
            candidate_votes[candidate]= 1 #which is new library being added to
            percent[candidate] = 100 * (candidate_votes[candidate] / total_votes)
        else:
            candidate_votes[candidate] += 1
            percent[candidate] = 100 * (candidate_votes[candidate] / total_votes)

# inspiration from:
#   https://www.w3schools.com/python/ref_dictionary_items.asp
#   not sure how i got here, but thought i'd play around with calling the values and somehow it worked!

for item in percent.items():
    if item[1] > highest_vote:
        highest_vote = item[1]
        winner = item[0]

# inspiration from: 
#   https://sparkbyexamples.com/python/append-or-add-multiple-values-to-set-in-python/#:~:text=In%20Python%2C%20there%20are%20several,sets%20to%20the%20existing%20set.
#   https://www.w3schools.com/python/ref_string_format.asp#:~:text=The%20format()%20method%20formats,defined%20using%20curly%20brackets%3A%20%7B%7D.

results = []
for candidate in candidate_names:
    results.append("{}: ".format(candidate) + "{:.3f}% ".format(percent[candidate]) + "({})".format(candidate_votes[candidate]))

# inspiration from:
#   https://www.geeksforgeeks.org/python-split-dictionary-keys-and-values-into-separate-lists/
#   below was going to be last resort if above didnt work...
# keys = []
# values = []
# items = candidate_votes.items()
# for item in items:
#    keys.append(item[0])
#    values.append(item[1])

print("")
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(results)
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

file_to_output = os.path.join('/Users/theresakim/Documents/northwestern/module 03 python/Starter_Code/PyPoll/Resources/output_election_data.txt')

with open(file_to_output, "w") as out:
    out.write("\n")
    out.write("Election Results\n")
    out.write("----------------------\n")
    out.write(f"Total Votes: {total_votes}\n")
    out.write("----------------------\n")
    out.write(f"{results}\n")
    out.write("----------------------\n")
    out.write(f"Winner: {winner}\n")
    out.write("----------------------\n")
    out.close()