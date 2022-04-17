import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
import pandas as pd
import json
import datetime as dt,time
import logging
import sys
#Read configuration file -- Please set the path you are using
sys.path.insert(1, 'https://github.com/KalaitziVasiliki/DummyAPI_processing/blob/main/config/')
sys.path.insert(1, '/DummyAPI_processing/blob/main/config/')
import configuration as conf


def mylog(msg,level='info'):
	if (level == 'error'): 
		logging.error(msg)
	else:
		logging.info(msg)
	print(msg)


def users_transformation():
	users_df_fin = pd.read_json(conf.data_path1, lines=True)
	users_df_loc= pd.json_normalize(users_df_fin['location'])
	del users_df_fin['location']
	users_df_fin['street'] = users_df_loc['street']
	users_df_fin['city'] = users_df_loc['city']
	users_df_fin['state'] = users_df_loc['state']
	users_df_fin['country'] = users_df_loc['country']
	users_df_fin['timezone'] = users_df_loc['timezone']
	
	users_df_fin.columns = conf.ds1_columns
	users_df_fin= users_df_fin.drop_duplicates(subset=['title', 'firstname', 'lastname','picture'], keep='last')
	return (users_df_fin)
	


def posts_transformation():
	posts_df_fin = pd.read_json(conf.data_path2, lines=True)
	posts_df_owner= pd.json_normalize(posts_df_fin['owner'])
	del posts_df_fin['owner']
	posts_df_fin['owner_id'] = posts_df_owner['id']
	posts_df_fin['owner_title'] = posts_df_owner['title']
	posts_df_fin['owner_firstname'] = posts_df_owner['firstName']
	posts_df_fin['owner_lastname'] = posts_df_owner['lastName']
	posts_df_fin['owner_picture'] = posts_df_owner['picture']
	
	posts_df_tag =  pd.DataFrame(posts_df_fin['tags'].tolist(), columns=['tag1', 'tag2', 'tag3'])
	del posts_df_fin['tags']
	posts_df_fin['tag1'] = posts_df_tag['tag1']
	posts_df_fin['tag2'] = posts_df_tag['tag2']
	posts_df_fin['tag3'] = posts_df_tag['tag3']
	posts_df_fin.columns = conf.ds2_columns
	#keep only posts with positive or zero likes --“No posts with negative likes” 
	posts_df_fin=posts_df_fin[posts_df_fin.likes >=0 ]
	#“No posts without owners”
	posts_df_fin = posts_df_fin.dropna(subset=['owner_firstname','owner_lastname'], how='all')	
	posts_df_fin= posts_df_fin.drop_duplicates(subset=['image', 'likes','text', 'publishdate','owner_id','owner_title','owner_firstname','owner_lastname','owner_picture'], keep='last')
	return (posts_df_fin)

	
def comments_transformation():
	comments_df = pd.read_json(conf.data_path3)
	comments_df = pd.json_normalize(comments_df['data'])
	comments_df_fin =comments_df
	
	#postgres dosnt like capitals in column names
	comments_df_fin.columns = conf.ds3_columns
	
	#“No comments without owners”
	comments_df_fin = comments_df_fin.dropna(subset=['owner_title','owner_firstname','owner_lastname'], how='all')	
	
	#“No duplicates”
	comments_df_fin= comments_df_fin.drop_duplicates(subset=['message', 'owner_id','owner_title','owner_firstname','owner_lastname','owner_picture','post','publishdate'], keep='last')
	return (comments_df_fin)


def postgreSQL_loading(dataset_type, dataframe_type):
	try:
		# Connect to an existing database
		connection = psycopg2.connect(database=conf.database,user=conf.user,password=conf.password,host=conf.host,port= conf.port)
		# Create a cursor to perform database operations
		cursor = connection.cursor()
		# Print PostgreSQL details
		print("PostgreSQL server information")
		print(connection.get_dsn_parameters(), "\n")
	
		engine = create_engine(conf.engine)
		dataframe_type.to_sql(dataset_type, engine)
		
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
	
	users_df_fin=users_transformation()
	posts_df_fin=posts_transformation()
	comments_df_fin=comments_transformation()
	
	print(users_df_fin)
	print(posts_df_fin)
	print(comments_df_fin)
	
	postgreSQL_loading('users',users_df_fin)
	postgreSQL_loading('posts',posts_df_fin)
	postgreSQL_loading('comments',comments_df_fin)

	scriptDuration = time.time() - start
	mylog('\nProcess ended and lasted %s\n'%(scriptDuration))
	
	sys.exit(0)

