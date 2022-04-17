#!/bin/bash

#This the main script that reads from API and stores in HDFS for Footfal Analytics 

#Parameters
path='please add the path of your activity'


#Starting writting in log file
echo "Starting process..." 

#Run python codes 
cd DummyAPI_processing/blob/main/src/

python Exercise_1.py 
echo "\nRunning Python script of Exercise 1: Data Ingestion and Validation" 

python Exercise_2.py 
echo "\nRunning Python script of Exercise 2: Data Loading" 

python Exercise_3.py 
echo "\nRunning Python script of Exercise 3: Data Transformation"}

echo "Process finished..." 
