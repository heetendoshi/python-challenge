import os
import csv

budgetdata_csv = os.path.join( 'Resources', 'election_data.csv')

with open(budgetdata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    totalVotes = 0
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    tooleyVotes = 0
    khanPercent = 0
    correyPercent = 0
    liPercent = 0
    tooleyPercent = 0

    for row in csvreader:
        totalVotes +=1
        if(row[2] == candidates[0]):
            khanVotes +=1
            khanPercent = float(khanVotes/totalVotes * 100)
        if(row[2] == candidates[1]):
            correyVotes +=1
            correyPercent = float(correyVotes/totalVotes * 100)
        if(row[2] == candidates[2]):
            liVotes +=1
            liPercent = float(liVotes/totalVotes * 100)
        if(row[2] == candidates[3]):
            tooleyVotes +=1
            tooleyPercent = float(tooleyVotes/totalVotes * 100)

    candidate = {}
    candidate[candidates[0]] = khanPercent
    candidate[candidates[1]] = correyPercent
    candidate[candidates[2]] = liPercent
    candidate[candidates[3]] = tooleyPercent
    

    winner = max(candidate, key=candidate.get)
   

    print("Election Results")
    print("------------------")
    print(f"Total Votes: {totalVotes}" )
    print("------------------")
    print(f'Khan: {khanPercent:.3f}%  ({khanVotes})')
    print(f'Correy: {correyPercent:.3f}%  ({correyVotes})')
    print(f'Li: {liPercent:.3f}%  ({liVotes})')
    print(f"O'Tooley: {tooleyPercent:.3f}%  ({tooleyVotes})")
    print("------------------")
    print(f"Winner: {winner}" )
    print("------------------")
    
output_path = os.path.join("new.csv")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Total Votes:", totalVotes])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Khan:", khanPercent, khanVotes])
    csvwriter.writerow(["Khan:", correyPercent, correyVotes])
    csvwriter.writerow(["Khan:", liPercent, liVotes])
    csvwriter.writerow(["Khan:", tooleyPercent, tooleyVotes])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Winner:", winner])
    csvwriter.writerow(["------------------"])