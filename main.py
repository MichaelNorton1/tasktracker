from sql_functions.sqlconnect import create_db_connection
from sql_functions.local import sqlpassword
from sql_functions.execute_query_db import execute_query
from sql_functions.read_query import read_query

dbname="school"


connection = create_db_connection("localhost","root",sqlpassword,dbname)


q1 = """
SELECT language
FROM course
WHERE course_id = 19
 ;
"""
update = """
DELETE FROM course 
WHERE course_id = 19;
"""

#execute_query(connection,update)


results = read_query(connection,q1)
print(results)

