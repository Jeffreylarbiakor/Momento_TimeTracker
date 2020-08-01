from datetime import datetime, date
import csv


def salary(hr):
    pay = hr*5
    return print(f'your salary is ${pay}')


track_date = date.today()  # getting the system's date and assigning it to a variable
# #asking Nana to input the time he started the work
work_start = input("Hi Nana please input the time you started the work in 24hr format")
time_work_start = datetime.strptime(work_start, '%H:%M')  # converting string input to time in hours and minutes

# asking Nana to input the time he finished the work in 24 hour format
work_finished = input("Hi Nana please input the time you finished the work in 24hr format")
time_work_finished = datetime.strptime(work_finished, '%H:%M')  # converting string input to time in hours and minutes

while time_work_finished > time_work_start:
    # finding the difference between time Nana started the work and the time Nana finished the task
    hours_spent = time_work_finished - time_work_start
    hours_spent_to_sec = hours_spent.seconds  # converting the hours spent into seconds
    # converting time spent from seconds into an integer to be able to calculate the pay
    int_of_hours_spent = hours_spent_to_sec / 60 / 60
    print("you started the work on:", track_date, time_work_start)
    print('You finished the work on:', track_date, time_work_finished)
    print(f'you spent: {hours_spent} hour(s)')
    salary(int_of_hours_spent)
    break
else:
    print('the time you completed the task should be ahead of the time you started')


# We need to convert the time from hours and minutes to do the calculations
conv_start = datetime.strptime(work_start, '%H:%M')
conv_end = datetime.strptime(work_finished, '%H:%M')
diff = (conv_end - conv_start).total_seconds()/3600

#define variables for csv data
csv_date1 = str(conv_start.date())
csv_date2 = str(conv_end.date())
csv_time1 = str(conv_start.time())
csv_time2 = str(conv_end.time())

# Nana is paid $5 per hour
pay_rate = 5
amount = str(diff * pay_rate)
row = ['Start Date', 'Start Time', 'Stop Date', 'Stop Time', 'Total Hours', 'Amount Earned']
data = [[csv_date1, csv_time1, csv_date2, csv_time2, diff, amount]]


with open('productivity_info.csv', 'a+', newline='\n', encoding='utf8') as f:
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
