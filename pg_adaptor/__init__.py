#? this file is necessary to declare a directory as a python package

import psycopg2  #? Adaptor to interact with postgres server
from dotenv import load_dotenv  #? A function to load .env files
import os  #? To interact with the OS and its functionalities

#? Path where you .env file is present
env_path = 'D:/Coding-Applications/VS Code/VSC Code files/AWS-postgreSQL/.env'
load_dotenv(dotenv_path=env_path)


#? Load the environment variables into local variables 
hostname = os.getenv('HOSTNAME1')
port = os.getenv('PORT')
username = os.getenv('USERNAME1')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')


#? To connect to the database
def connect():
    try:
        connection = psycopg2.connect(
            host=hostname,
            port=port,
            user=username,
            password=password,
            dbname=database
        )
        return connection
    except Exception as e:
        print("Couldn't establish connection to the database")
        print(e)