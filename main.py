from sqlconnect import create_server_connection
from local import sqlpassword
from createdb import create_database


connection = create_server_connection("localhost","root",sqlpassword)
dbquery = "CREATE DATABASE school"

create_database(connection,dbquery)


