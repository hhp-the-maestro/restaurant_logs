# restaurant_logs

## Problem statement

**A restaurant keeps a log of (eater_id, foodmenu_id) for all the diners. The eater_id
is a unique number for every diner and foodmenu_id is unique for every food item
served on the menu. Write a program that reads this log file and returns the top 3
menu items consumed. If you find an eater_id with the same foodmenu_id more
than once then show an error.**


There are 3 sample log files provided log.csv, success_log.csv, err_log.csv
the success_log and err_log csv files are used for unit testing the poitive and negative conditions
the log.csv is a sample log to run the code 

## Build the DockerFile
### sudo docker build -t "log_reader" .

## Run the DockerFile
### sudo docker run log_reader
