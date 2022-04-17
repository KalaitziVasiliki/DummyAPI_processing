import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
import pandas as pd
import json
import datetime as dt,time
import logging
import sys
#Read configuration file
sys.path.insert(1, 'C:/Users/kalai/Downloads/learnworlds/config')

import configuration as conf


def mylog(msg,level='info'):
	if (level == 'error'): 
		logging.error(msg)
	else:
		logging.info(msg)
	print(msg)


def postgreSQL_aggregation(sql_statement):
	try:
		connection = psycopg2.connect(database=conf.database,user=conf.user,password=conf.password,host=conf.host,port= conf.port)

		# Create a cursor to perform database operations
		cursor = connection.cursor()
		# Print PostgreSQL details
		print("PostgreSQL server information")
		print(connection.get_dsn_parameters(), "\n")
	
		engine = create_engine(conf.engine)
		cursor.execute(sql_statement)
		connection.commit()

	except (Exception, Error) as error:
		print("Error while connecting to PostgreSQL", error)
	finally:
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			
	

if __name__ == '__main__':
	start = time.time()
	#Always start at least one day behind start=1
	start=1
	
	#- How many new users are added daily?
	Q1=postgreSQL_aggregation(conf.query1)
	#------------------------------------------------------------------------------------------------------------									
	#- What is the average time between registration and first comment?
	Q2=postgreSQL_aggregation(conf.query2)
	#-------------------------------------------------------------------------------------------------------------									
   	#- Which cities have the most activity, in terms of posts per day?			 		 
	Q3=postgreSQL_aggregation(conf.query3)
	#-------------------------------------------------------------------------------------------------------------																
	#- Which tags are most frequently encountered, across user posts?
	Q4=postgreSQL_aggregation(conf.query4)
	#-------------------------------------------------------------------------------------------------------------																

	scriptDuration = time.time() - start
	mylog('\nProcess ended and lasted %s\n'%(scriptDuration))
	
	sys.exit(0)
