import sys
import datetime as dt,time
import requests,json
from requests.auth import HTTPBasicAuth
import logging
import pandas as pd
from pandas import json_normalize
#Read configuration file -- Please set the path you are using
sys.path.insert(1, 'https://github.com/KalaitziVasiliki/DummyAPI_processing/blob/main/config/')
sys.path.insert(1, '/DummyAPI_processing/blob/main/config/')
import configuration as conf

#Set max retries
requests.adapters.DEFAULT_RETRIES=3

def mylog(msg,level='info'):
	if (level == 'error'): 
		logging.error(msg)
	else:
		logging.info(msg)
	print(msg)

def chunks(lst, n):
	'''Yield successive n-sized chunks from lst.'''
	for i in range(0, len(lst), n):
		yield lst[i:i + n]


def write_datasets(filename,DATASET,headers):
	date=(dt.datetime.now()).strftime('%d/%m/%Y')
	data_list=[]	
	try: 
		data_req = requests.get(url = DATASET, verify= True, headers=headers, timeout=conf.request_timeout)	
		if (data_req.status_code == 200):
			mylog('Starting API export')
			myfile = open(conf.project_path +filename + conf.filetype, 'w', encoding="utf-8")
			myfile.write("%s\n" % data_req.text)
			myfile.close()
		else:
			mylog('Request Failed with status:%d'%(r.status_code),'error')  
	except Exception as e:
		mylog(e)
		mylog('FAIL to get data_list')
	return data_list


	
def write_datasets_full(filename,DATASET,headers):
	date=(dt.datetime.now()).strftime('%d/%m/%Y')
	data_list=[]	
	try: 
		data_req = requests.get(url = DATASET, verify= True, headers=headers)	
		if (data_req.status_code == 200):
			mylog('Starting API export')
			data_df = pd.read_json(data_req.text)
			df_fin = pd.json_normalize(data_df['data'])
			myfile = open(conf.project_path +filename + conf.filetype_full, 'w', encoding="utf-8")
			for item in df_fin['id'].values:
				USERS_URL = DATASET +'/'+	item
				data_req = requests.get(url = USERS_URL, verify= True, headers=headers)
				myfile.write("%s\n" % data_req.text)
			myfile.close()
		else:
			mylog('Request Failed with status:%d'%(r.status_code),'error')  
	except Exception as e:
		mylog(e)
		mylog('FAIL to get data_list')
	return data_list

def write_comments_dataset_full(filename,DATASET,headers):
	date=(dt.datetime.now()).strftime('%d/%m/%Y')
	data_list=[]	
	try: 
		data_req = requests.get(url = DATASET, verify= True, headers=headers)	
		if (data_req.status_code == 200):
			mylog('Starting API export')
			myfile = open(conf.project_path +filename + conf.filetype_full, 'w', encoding="utf-8")
			myfile.write("%s\n" % data_req.text)
			myfile.close()
		else:
			mylog('Request Failed with status:%d'%(r.status_code),'error')  
	except Exception as e:
		mylog(e)
		mylog('FAIL to get data_list')
	return data_list

	

if __name__ == '__main__':
	start = time.time()
	#Always start at least one day behind start=1
	start=1
	
	users_list=(write_datasets_full('users',conf.USERS_URL,conf.headers))
	posts_list=(write_datasets_full('posts',conf.POSTS_URL,conf.headers))
	comments_list=(write_comments_dataset_full('comments',conf.COMMENTS_URL,conf.headers))
	
	scriptDuration = time.time() - start
	mylog('\nProcess ended and lasted %s\n'%(scriptDuration))
	
	sys.exit(0)


