# Python-Coders-TimeTracker
# MOMENTO TRACKER DOCUMENTATION

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [What is MOMENTO TRACKER version 1](#what-is-momento-tracker)
- [How MOMENTO TRACKER version 1 works](#how-it-works-use)
- [Addition](#addition)
- [Constraint](#constraint)
- [MOMENTO TRACKER version 2](#momento-tracker version 2)
- [Developers](#developers)
- [Modules Imported](#modules-imported)

---
#### What is MOMENTO TRACKER:
This application (momento tracker) is designed for a user called Nana
to help him calculate the salary due him based on the number of hours he works in a consulting business he recently started.
MOMENTO TRACKER records the time Nana started the work and the time Nana finished the work.
It is then able to detect the number of hours he spent on each task and calculate the salary he deserves.

#### How MOMENTO TRACKER version 1 works:
A prompt appears for Nana to enter the time he started the work
A prompt appears for Nana to enter the time he finished the work
MOMENTO TRACKER then calculates the hours spent and then find the salary the business needs to pay Nana
MOMENTO then displays the following:
    *the time work started including the day's date
	*the time work ended including the day's date
	*the hours he spent on the task
	*the salary due him


#### Addition:
What makes MOMENTO TRACKER stand out is that, it automatically record the necessary information in a csv file for Nana to make reference from it.
The columns are the date, time work started, time work finished, Number of hours worked and pay awarded


#### Constraint:
MOMENTO TRACKER has been designed to accept time in 24 hour format(00:00 - 23:59)
If Nana input time for when he finished the task and it backward against the time he finished the work,
the application will prompt him to ensure time work finished is ahead of time work started.
The application will end and so Nana has to start the application again and input the right info.


#### MOMENTO TRACKER version 2:
This application is an update of MOMENTO TRACKER version 1.
What is new in MOMENTO TRACKER version 2 is, Nana will only press enter when he is about starting the work and the system will capture the current date and time.
When Nana completes the task, he will press enter in the prompt provided by time tracker for the system to capture the current date and time.
The sytem then do the salary calculation and bring out the required output.


#### Developers:
Isaac Mbreye Quartey, 
Ivy Odametey,
Jeffrey Larbi-Akor 


#### Modules Imported:
*Datetime
*Time
*Date
*CSV


##### Note: this application was built with Python version 3.8.2
