#EX.1 configurations
request_timeout=60

prefix_path='please add the path of your activity before running the projet, example C:/Users/myname/Desktop/'
project_path= prefix_path + 'DummyAPI_processing/datasets/'
filetype='.json'
filetype_full='_full.json'

headers = {'App-ID': '6255d030d3bc7bd6d9468a1a'}
USERS_URL = 'https://dummyapi.io/data/v1/user'
POSTS_URL = 'https://dummyapi.io/data/v1/post'
COMMENTS_URL = 'https://dummyapi.io/data/v1/comment'

#EX.2 configurations

data_path1= prefix_path + 'DummyAPI_processing/datasets/users_full.json'
data_path2= prefix_path + 'DummyAPI_processing/datasets/posts_full.json'
data_path3= prefix_path + 'DummyAPI_processing/datasets/comments_full.json'

ds1_columns = ['id', 'title', 'firstname', 'lastname','picture','gender','email','dateofbirth','phone','registerdate', 'updateddate' , 'street', 'city', 'state', 'country', 'timezone']
ds2_columns = ['id', 'image', 'likes','link','text', 'publishdate','owner_id','owner_title','owner_firstname','owner_lastname','owner_picture', 'tag1','tag2','tag3']	
ds3_columns = ['id', 'message', 'post','publishdate', 'owner_id','owner_title','owner_firstname','owner_lastname','owner_picture',]

# Connect to POSTGRESQL database

database="lw_db"
user='postgres'
password='sD4dtjkw'
host='localhost'
port= '5432'

engine='postgresql://postgres:sD4dtjkw@localhost:5432/lw_db'


#EX.3 configurations



query1= ''' CREATE TABLE DAILY_USER_REGISTRATION AS (
										SELECT count(id),TO_DATE(registerdate,'YYYY-MM-DD"T"HH24:MI:SSS"Z"') as registerdate from users 
										group by TO_DATE(registerdate,'YYYY-MM-DD"T"HH24:MI:SSS"Z"'));'''


query2= '''CREATE TABLE DIFF_BTW_REGISTR_AND_COMMENT AS (
										SELECT 
											TO_DATE(publishdate,'YYYY-MM-DD"T"HH24:MI:SSS"Z"') -  TO_DATE(registerdate,'YYYY-MM-DD"T"HH24:MI:SSS"Z"')  as time_difference  , B.owner_id 
											from users A
										inner join 
										comments B
										on A.id=B.owner_id)'''


query3= '''CREATE TABLE MOST_ACTIVE_CITIES_POSTING AS (
									SELECT COUNT(*) as top_cities, A.city
									FROM users A 
									INNER JOIN posts B 
									on A.id=B.owner_id 
									GROUP BY A.city
									order by top_cities desc limit 10 )	'''


query4= ''' CREATE TABLE MOST_USED_TAGS_POSTING AS 
									(
									select (T1.c1+ T1.c2 + T2.c3) as tag_frequency, T1.tag1 as tags 
									from
									((select tag1, count(*) as C1 from posts  group by tag1 order by count(*) desc) A
									inner join
									(select tag2, count(*) as C2 from posts  group by tag2 order by count(*) desc) B
									on A.tag1=B.tag2) T1
									inner join
									(select tag3, count(*) as C3 from posts group by tag3 order by count(*) desc) T2
									on T1.tag1=T2.tag3
									order by tag_frequency desc
									)'''
