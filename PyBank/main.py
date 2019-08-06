import os
import csv

budgetdata_csv = os.path.join( 'Resources', 'budget_data.csv')

with open(budgetdata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    totalMonths = 0
    totalNetPL = 0
    averagePL=0
    pnl=[]
    dates=[]
    diff = 0
    diffTotal = 0
    maxprofit = -10000000
    maxloss = 10000000
    maxcounter = 0
    losscounter = 0

    for row in csvreader:
        totalMonths += 1
        totalNetPL = totalNetPL + int(row[1])
        pnl.append(float(row[1]))
        dates.append(row[0])
        
    
    x=1
    while x < len(pnl):
        diff = pnl[x] - pnl[x-1] 
        diffTotal = diffTotal + diff
        x+=1
        if(diff > maxprofit):
            maxprofit = diff
            maxcounter = x -1
        if(diff<maxloss):
            maxloss = diff
            losscounter = x -1
    averagePL = diffTotal/(totalMonths-1)
    
    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {totalMonths}" )
    print(f'Total: ${totalNetPL}')
    print(f'Average Change: ${averagePL:.2f}')
    print(f'Greatest Increase in Profits: {dates[maxcounter]} (${maxprofit})')
    print(f'Greatest Decrease in Profits: {dates[losscounter]} (${maxloss})')
    
output_path = os.path.join("new.csv")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Total Months:", totalMonths])
    csvwriter.writerow(["Total: $", totalNetPL])
    csvwriter.writerow(["Average Change: $", averagePL])
    csvwriter.writerow(["Greatest Increase in Profits:", dates[maxcounter],maxprofit])
    csvwriter.writerow(["Greatest Decrease in Profits:", dates[losscounter],maxloss])

