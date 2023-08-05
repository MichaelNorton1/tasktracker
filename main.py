from sqlconnect import create_server_connection
from local import sqlpassword


connection = create_server_connection("localhost","root",sqlpassword)