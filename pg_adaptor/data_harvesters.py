import psycopg2  #? Adaptor to interact with postgres server
from psycopg2.extras import execute_values  #? An helper function designed to insert several rows in a single operation
from pg_adaptor import connect


'''
#? To execute this particular file type in the terminal(from the project's root directory):
-> python -m pg_adaptor.data_harvesters
'''

#! Insert website data here
def insert_website_data(data):
    '''
    :param 'data': List of tuples(each tuple is a single row).
        example:
            data = [
                ('http://example.com/article1', '<html>Content of article 1</html>', 'English'),
                ('http://example.com/article2', '<html>Content of article 2</html>', 'Hindi'),
            ]

    '''
    conn = connect()

    '''
    :dev: 
        -> A 'transaction' is a sequence of DB operations performed as a single unit.
        -> '.commit()' used to permanently save all changes made in the current transaction to the database.
        -> '.rollback()' used to undo all chnages made in the current transaction
    '''
    try:
        #? A 'curosr' is a DB object used to retrieve, manipulate aand iterate through rows of a result set + also used to execute DB commands
        with conn.cursor() as cursor:  #? After this block, the 'cursor' resource will be closed automatically
            insert_query = """
            INSERT INTO "Source".website (url, raw_content, language) VALUES %s;  
            """
            #? '%s' is a place holder, will be replaced by a tuple(from our list of tuples during runtime)
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Insert e-newspaper data here
def insert_e_newspaper_data(data):
    '''
    :param 'data': List of Tuples(see above function for more details)
        example:
            data = [
                ("/path/to/image1.jpg", "The content of the first e-newspaper article as a text string", "Morning Edition"),
                ("/path/to/image2.jpg", "The content of the second e-newspaper article as a text string", "Evening Edition"),
            ]
    '''
    
    conn = connect()

    try:
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO "Source".e-newspaper (image_path, raw_text, edition) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close() 


#! Insert video data here
def insert_video_data(data):
    '''
    :param 'data': List of Tuples(see above function for more details)
        example:
            data = [
                ('http://youtube.com/video1', 'Transcript of the first video', datetime.datetime.now()),
                ('http://youtube.com/video2', 'Transcript of the second video', datetime.datetime.now()),
            ]
    '''

    conn = connect()

    try:
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO "Source".video (video_url, transcript, downloaded_at) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Fetch all data from the given table
def get_all_data_from_table(table_name):
    '''
    :param 'table_name': Any table name of any schema, you will only have read permissions on tables present outside your 'Data-Harvestor' schema
    '''

    conn = connect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            '''
            : '.fetchall()': When you execute a SELECT query, the cursor does not retrieve all rows immediately, but fetches the rows lazily(one by one)
                                , so this method fetches all rows of a query result set as a list of tuples.  
            '''
            records = cursor.fetchall() 

            return records
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
    finally:
        conn.close()


#! <-- Add new Functions here -->




#! <-- End new Functions -->


#! For testing only

'''
print(f"Hostname: {hostname}")
print(f"Port: {port}")
print(f"Username: {username}")
print(f"Database: {database}")
print(f"PWD: {password}")
'''

'''
print(get_all_data_from_table('\"Source\".video'))
'''


'''
import datetime
data = [
        ('http://youtube.com/video1', 'Transcript of the first video', datetime.datetime.now()),
        ('http://youtube.com/video2', 'Transcript of the second video', datetime.datetime.now()),
    ]
insert_video_data(data)
'''


'''
data = [
            ('http://example.com/article1', '<html>Content of article 1</html>', 'English'),
            ('http://example.com/article2', '<html>Content of article 2</html>', 'Hindi'),
        ]
insert_website_data(data)
'''
