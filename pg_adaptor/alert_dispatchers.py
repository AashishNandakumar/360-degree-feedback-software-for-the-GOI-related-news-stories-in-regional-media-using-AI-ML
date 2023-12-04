import psycopg2
from psycopg2.extras import execute_values
from pg_adaptor import connect

'''
#? To execute this particular file type in the terminal(from the project's root directory):
-> python -m pg_adaptor.alert_dispatchers
'''

#! Insert PIB officials data
def insert_pib_officials_data(data):
    '''
    :param 'data': List of tuples
        example: 
            data = [
                ('John Doe', '{"email": "johndoe@example.com", "phone": "1234567890"}', 'Finance'),
                ('Jane Smith', '{"email": "janesmith@example.com", "phone": "0987654321"}', 'Communications'),
                ('Raj Patel', '{"email": "rajpatel@example.com", "phone": "1122334455"}', 'Infrastructure'),
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
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO "Notification".pib_official (name, contact_detail, department) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Insert notification details
def insert_notifications(data):
    '''
    :param 'data': List of tuples
        example: 
            data = [
                (1, "Policy update available for review.", "Neutral"),
                (2, "Urgent: Budget report needs revision.", "Bad"),
                (3, "Congratulations on the successful campaign!", "Good"),
                # ... more tuples for other notifications
            ]
    '''
    conn = connect()

    try:
        with conn.cursor() as cursor:
            insert_query = """ 
            INSERT INTO "Notification".notification_log (official_id, message, sentiment) VALUES %s;
            """
            execute_values(cursor, insert_query, data)
        conn.commit()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
        conn.rollback()
    finally:
        conn.close()


#! Retreive notifications filtered by 'official_id'
def get_notifications(official_id=None):
    '''
    :param 'offical_id': optional, the ID of PIB official whose notifications to extract
    :return: A list of tuples containing notification data 
    '''
    conn = connect()
    try:
        with conn.cursor() as cursor:
            if official_id:
                cursor.execute("""
                SELECT * FROM "Notification".notification_log WHERE official_id = %s;
                """, (official_id))
            else:
                cursor.execute("""
                SELECT * FROM "Notification".notification_log;
                """)
            return cursor.fetchall()
    except psycopg2.DatabaseError as e:
        print(f"An error occured: {e}")
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
print(get_all_data_from_table("Source", "video"))
'''

'''
data_to_insert = [
    ('John Doe', '{"email": "johndoe@example.com", "phone": "1234567890"}', 'Finance'),
    ('Jane Smith', '{"email": "janesmith@example.com", "phone": "0987654321"}', 'Communications'),
    ('Raj Patel', '{"email": "rajpatel@example.com", "phone": "1122334455"}', 'Infrastructure'),
    # ... more tuples representing other PIB officials
]
insert_pib_officials_data(data_to_insert)
'''

'''
data_to_insert = [
    (1, "Policy update available for review.", "Neutral"),
    (2, "Urgent: Budget report needs revision.", "Bad"),
    (3, "Congratulations on the successful campaign!", "Good"),
    # ... more tuples for other notifications
]
insert_notifications(data_to_insert)
'''

'''
print(get_notifications("2"))
'''