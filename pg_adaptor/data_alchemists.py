import psycopg2  #? Adaptor to interact with postgres server
from psycopg2.extras import execute_values #? An helper function designed to insert several rows in a single operation
from pg_adaptor import connect


'''
#? To execute this particular file type in the terminal(from the project's root directory):
-> python -m pg_adaptor.data_alchemists
'''

#! Insert processed + analyzed website data
def insert_processed_website_data(data):
    '''
    :param 'data': List of tuples(Tuples indicating each row of a table)
        example: 
            data = [
                (1, "Processed content for website 1", "Positive"),
                (2, "Processed content for website 2", "Neutral"),
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
            INSERT INTO "Processed_and_analyzed".processed_website (processed_website_id, processed_content, sentiment) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Insert processed + analyzed e-newspaper data
def insert_processed_e_newspaper_data(data):
    '''
    :param 'data': List of tuples
        example: 
            data = [
                (1, "/path/to/processed/clipping1.jpg", "Negative"),
                (2, "/path/to/processed/clipping2.jpg", "Positive"),
            ]
    '''
    conn = connect()
    try:
        with conn.cursor() as cursor:
            insert_query = """ 
            INSERT INTO "Processed_and_analyzed".processed_e_newspaper (processed_e_newspaper_id, clipping_path, sentiment) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Insert processed + analyzed video data
def insert_processed_video_data(data):
    '''
    :param 'data': List of tuples
        example:
            processed_youtube_video_data = [
            (1, "Bad", "00:01:30-00:02:15"),
            (2, "Good", "00:00:10-00:01:00"),
            (3, "Neutral", "00:00:15-00:03:00"),

        ]

    '''
    conn = connect()
    try:
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO "Processed_and_analyzed".processed_video (processed_video_id, sentiment, highlight_timestamps) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Fetch all data from the given table
def get_all_data_from_table(schema_name, table_name):
    '''
    :param 'table_name': Any table name of any schema, you will only have read permissions on tables present outside your 'Data-Harvestor' schema
    '''

    conn = connect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM \"{schema_name}\".{table_name}")
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
print(get_all_data_from_table('Source', 'video'))
'''

'''
processed_youtube_video_data = [
    (13, "Bad", "00:01:30-00:02:15"),
    (14, "Good", "00:00:10-00:01:00"),
]
insert_processed_video_data(processed_youtube_video_data)
'''
 
