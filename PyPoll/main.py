# Modules
import os
import csv

# Open the CSV & Name the File
with open("election_data.csv") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    #Skip Header of CSV File
    next(election_data)

    #Calculate the total number of votes cast
    #Create variable(s) you will add data into
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in election_data:
        #append total number of votes by counting how many lines in Voter ID column
        total_votes+=1
        #If statement searches Candidate row for "Kahn" - if Kahn is there it counts 1 and adds to "candidate"
        # repeat with every candidate
        if row[2] == "Khan":
            khan_votes+=1
        if row[2] == "Correy":
            correy_votes+=1
        if row[2] == "Li":
            li_votes+=1
        if row[2] == "O'Tooley":
            otooley_votes+=1
#-------------------------------------------------------------------------------
    #Calculate percentages for each candidate as new variable to avoid confusion
    
    #Create Variables and then calculate percentages by taking ( Candidate Votes / Total Votes ), then multiply by 100 to get percent
    khan_percent = (khan_votes/total_votes)*100
    correy_percent = (correy_votes/total_votes)*100
    li_percent = (li_votes/total_votes)*100
    otooley_percent = (otooley_votes/total_votes)*100

    # Create a dictionary of candidate names to tie them to their totals
    candidates_dict = {
        "Khan":khan_votes,
        "Correy":correy_votes,
        "Li":li_votes,
        "O'Tooley":otooley_votes}

#-------------------------------------------------------------------------------
#Print List

#Note - :.3f formats 3 digits past the decimal point

    print("Election Results")
    print("----------------")
    print(f"Total Votes: {(total_votes)}")
    print("----------------")
    print(f"Khan: {(khan_percent):.3f}% ({(khan_votes)})")
    print(f"Correy: {(correy_percent):.3f}% ({(correy_votes)})")
    print(f"Li: {(li_percent):.3f}%  ({(li_votes)})")
    print(f"O'Tooley: {(otooley_percent):.3f}% ({(otooley_votes)})")
    print("----------------")
    print(f"Winner: {max(candidates_dict,key=lambda key:candidates_dict[key])}")
    print("----------------")

#-------------------------------------------------------------------------------
    #Write lines over to the new file created
    # note - \n helps split it into new lines

    file = open("polling_results.txt", "w")

    file.write("Election Results"+"\n")
    file.write("----------------"+"\n")
    file.write(f"Total Votes: {(total_votes)}"+"\n")
    file.write("----------------"+"\n")
    file.write(f"Khan: {(khan_percent):.3f}% ({(khan_votes)})"+"\n")
    file.write(f"Correy: {(correy_percent):.3f}% ({(correy_votes)})"+"\n")
    file.write(f"Li: {(li_percent):.3f}%  ({(li_votes)})"+"\n")
    file.write(f"O'Tooley: {(otooley_percent):.3f}% ({(otooley_votes)})"+"\n")
    file.write("----------------"+"\n")
    file.write(f"Winner: {max(candidates_dict,key=lambda key:candidates_dict[key])}"+"\n")
    file.write("----------------"+"\n")