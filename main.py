from read_query import read_query
from sqlconnect import create_db_connection
from local import sqlpassword
from execute_query_db import execute_query
from createdb import create_database

dbname="school"


connection = create_db_connection("localhost","root",sqlpassword,dbname)


q1 = """
SELECT 
teacher.teacher_id
FROM teacher
WHERE teacher.language_1 = "FRA"
 ;
"""
update = """
DELETE FROM course 
WHERE course_id = 20;
"""

execute_query(connection,update)


#results = read_query(connection,q1)

