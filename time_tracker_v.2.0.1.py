# We are going to build a time tracking program
 
#First, we would import the necessary modules
from datetime import datetime
import datetime
import time
import csv

#Start time
print("Hello Nana! Ready to start your day?")
start_time = input("Hit 'Enter\' to clock-in\n")
text1 = "Nice! Your current session started at: \n"
time1 = time.strftime("%Y-%m-%d %H:%M:%S")
time3 = time.strftime('%H:%M')
conv_time3 = datetime.datetime.strptime(time3, '%H:%M')
date_only = time.strftime("%Y-%m-%d")
print (text1, time1)
print (' ')

#End time
end_time = input("When you're done, hit 'Enter\' to clock out \n")
text2 = "You clocked out at: \n"
time2 = time.strftime("%Y-%m-%d %H:%M:%S")
time4 = time.strftime('%H:%M')
conv_time4 = datetime.datetime.strptime(time4, '%H:%M')
print (text2, time2)


#Calculations
# The time is converted from hours and minutes to seconds to do the calculations
total_time = (conv_time4 - conv_time3).total_seconds()/3600
hours_spent = conv_time4 - conv_time3

#Nana earns $5 per hour
pay_rate = 5
wages = (total_time) * pay_rate
formatted_wage = "{:.2f}".format(wages)

text3 = ("Oops! it seems you didn't spend much time on this project.\n")
text4 = (f'You have worked {hours_spent} hours and earned ${formatted_wage} this session.')
text5 = ("Great work!\nYou have worked " + f'{hours_spent}'
"and earned " + f'${wages}' + " in this session.")
print(' ')

#output message
if total_time < float(0.5):
    print(text3, text4)
else:
    print(text5)


# Write output data to csv file
row = ['Date Started', 'Start Time', 'Date Finished', 'Stop Time', 'Total Time spent', 'Amount Earned']
data = [[date_only, time3, date_only, time4, hours_spent, formatted_wage]]

with open('time_tracking_data.csv', 'a+', newline='\n', encoding='utf8') as f:
	f.seek(0)
	#Check if the file is empty
	file_data = f.read(100)
	if len(file_data) > 0:
		writer = csv.writer(f) 
		writer.writerows(data)
	else:
		writer = csv.writer(f)
		writer.writerow(row)
		writer.writerows(data)

#Thank you Azubi!!!
