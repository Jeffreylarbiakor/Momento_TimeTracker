from datetime import datetime, date
import csv


def salary(hr):
    pay = hr*s
    return pring(f'your salary is ${pay}')


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


with open('time_tracker.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Time work started", "Time work finished", "Number of hours worked", "Pay awarded"])

# the function below is to append time tracking info for Nana anytime he works on a task


def time_tracking_info(time_tracker_file, item):
    # a+ is used instead of r+ because the file time_tracker_file is not in existence
    with open(time_tracker_file, 'a+', newline='') as append_item:
        csv_writer = writer(append_item)
     csv_writer.writerow(item)


work_hours = hours_spent
int_hours = int_of_hours_spent
items = [track_date, time_work_start, time_work_finished, work_hours, salary(int_hours)]
time_tracking_info('time_tracker.csv', items)
