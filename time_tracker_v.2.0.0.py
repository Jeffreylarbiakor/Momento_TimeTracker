# We are going to build a time tracking program

#First, we would import the necessary modules
from datetime import datetime
import datetime
import time
import csv

#Next, the general variables will be defined
now = datetime.datetime.now()

#Start time
print("Hello Nana! Ready to start your day?")
start_time = input("Hit 'Enter\' to clock-in\n")
text1 = "Nice! Your current session started at: \n"
time1 = now.strftime("%Y-%m-%d %H:%M:%S")
time3 = now.strftime('%H.%M')
date_only = time.strftime("%Y-%m-%d")
print (text1, time1)
print (' ')

#End time
end_time = input("When you're done, hit 'Enter\' to clock out \n")
text2 = "You clocked out at: \n"
time2 = time.strftime("%Y-%m-%d %H:%M:%S")
time4 = time.strftime('%H.%M')
print (text2, time2)

#Calculations
total_time = float(time4 )- float(time3)
#Pay rate is $5 per hour
wages = (total_time) * 5

#formatted output of calculations
formatted_time = "{:.2f}".format(total_time)
formatted_wage = "{:.2f}".format(wages)
text3 = (("Oops! it seems you didn't do much work today.\nYou have worked " +
 "{:.2f} hours " + "and earned " + "${:.2f}" + " this session.").format(total_time,wages))
text4 = (("Great work!\nYou have worked " + "{:.2f} hours " + 
"and earned " + "${:.2f}" + " this session.").format(total_time,wages))
print(' ')

#concluding message
if total_time < int(1):
    print(text3)
else:
    print(text4)


# Nana is paid $5 per hour
pay_rate = 5
amount = str(total_time * pay_rate)
row = ['Start Date', 'Start Time', 'Stop Date', 'Stop Time', 'Total Hours', 'Amount Earned']
#data = [[csv_date1, csv_time1, csv_date2, csv_time2, diff, amount]]
data = [[date_only, time3, date_only, time4, formatted_time, amount]]

with open('test1.csv', 'a+', newline='\n', encoding='utf8') as f:
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

#Enjoy!