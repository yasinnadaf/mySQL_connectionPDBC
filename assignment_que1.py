import mysql.connector as c
# 1.Write a SQL statement to create a table named countries including columns country_id,
# country_name and region_id and make sure that no countries except Italy, India and China will
# be entered in the table.

def mysql_connection():
    try:
        connection = c.connect(host = 'localhost',
        user = 'root',
        password = 'Yasin@786'
        )
        create_db_query = "CREATE DATABASE Questions1"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)


def create_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database= 'Questions1'
                               )
        create_table_query = """
            CREATE TABLE countries(COUNTRY_ID varchar(2) NOT NULL,
            COUNTRY_NAME varchar(40) NOT NULL,
            CONSTRAINT CHK_country CHECK (COUNTRY_NAME IN ('Italy', 'India', 'China')),
            REGION_ID varchar(10) NOT NULL )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)


def insert_into():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions1'
                               )
        COUNTRY_ID = int(input("Enter country id: "))
        COUNTRY_NAME = input("Enter country name: ")
        REGION_ID = int(input("Enter region id: "))
        insert_query = "insert into countries(COUNTRY_ID, COUNTRY_NAME, REGION_ID) values(%s, %s, %s)"
        connection.cursor()
        data_value = (COUNTRY_ID, COUNTRY_NAME, REGION_ID)
        conn = connection.cursor()
        conn.execute(insert_query, data_value)
        connection.commit()
    except Exception as e:
        print(e)

def display_info():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions1'
                               )
        select_table = "select * from countries"
        with connection.cursor() as cursor:
            cursor.execute(select_table)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # mysql_connection()
    # create_table()
    # insert_into()
    display_info()