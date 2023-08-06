from flask import Flask

from sql_functions.local import sqlpassword
from sql_functions.read_query import read_query
from sql_functions.sqlconnect import create_db_connection

dbname="school"
# adding Folder_2 to the system path


connection = create_db_connection("localhost", "root", sqlpassword, dbname)
app = Flask(__name__)
q1 = """
SELECT *
FROM course

 ;
"""
results = read_query(connection, q1)





@app.route("/")
def hello_world():
    return "<h1>hey</h1>"
