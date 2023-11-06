import os
import csv

budget_csv = os.path.join("..","Resources", "budget_data.csv")

#things we need to print
total_months = 0
total_amount = 0
average_change = 0
change = 0
previous = 0
total_change = 0
increase_month = ""
decrease_month = ""
greatest_increase = 0
greatest_decrease = 0

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #save header
    header = next(csv_reader)
    

    # Read through each row of data after the header
    for row in csv_reader:
        # count amount of mounts
        total_months = total_months + 1
        # add profits
        total_amount = total_amount + int(row[1])

        #get total change
        if previous != 0:
            change = int(row[1]) - previous
        previous = int(row[1])
        total_change = total_change + change

        # save greatest increase and the month of
        if greatest_increase < change:
            greatest_increase = change
            increase_month = row[0]

        # save the greatest decrease and the month of
        if greatest_decrease > change:
            greatest_decrease = change
            decrease_month = row[0]

#gets average change
average_change = total_change/(total_months-1)
#rounds average change
average_change_rounded = round(average_change,2)

#prints into terminal
print("Financial Analysis")
print("----------------------------")
print ("Total Months: " + str(total_months))
print ("Total: $" + str(total_amount))
print ("Averange Change: $" + str(average_change_rounded))
print ("Greatest Increase in Profits: " + increase_month + " ($" + str(greatest_increase) + ")")
print ("Greatest Decrease in Profits: " + decrease_month + " ($" + str(greatest_decrease) + ")")

#prints into a file
with open('../Output/output.txt', 'w') as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print ("Total Months: " + str(total_months), file=text_file)
    print ("Total: $" + str(total_amount), file=text_file)
    print ("Averange Change: $" + str(average_change_rounded), file=text_file)
    print ("Greatest Increase in Profits: " + increase_month + " ($" + str(greatest_increase) + ")", file=text_file)
    print ("Greatest Decrease in Profits: " + decrease_month + " ($" + str(greatest_decrease) + ")", file=text_file)
