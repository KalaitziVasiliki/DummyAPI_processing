#!/bin/bash

#This the main script that reads from API and stores in HDFS for Footfal Analytics 

#Parameters
path='please add the path of your activity'

log_file=C:/Users/kalai/Downloads/learnworlds_assignment/logs/fa_log_$(date +%Y_%m_%d).log
EX1=/C:/Users/kalai/Downloads/learnworlds_assignment/src/Exercise_1.py
EX2=/C:/Users/kalai/Downloads/learnworlds_assignment/src/Exercise_2.py
EX3=/C:/Users/kalai/Downloads/learnworlds_assignment/src/Exercise_3.py


local_datapath=
hdfs_datapath=

#Starting writting in log file
echo "Starting process..." 

#Run python codes 
cd Downloads/learnworlds_assignment/src/

python Exercise_1.py 
echo "\nRunning Python script of Exercise 1: Data Ingestion and Validation" 

python Exercise_2.py 
echo "\nRunning Python script of Exercise 2: Data Loading" 

python Exercise_3.py 
echo "\nRunning Python script of Exercise 3: Data Transformation"}

echo "Process finished..." 


#Clear old logs Retention is on 10 days
#echo -e "\nCleaning old log files\n" 2>&1 | tee -a ${log_file}
