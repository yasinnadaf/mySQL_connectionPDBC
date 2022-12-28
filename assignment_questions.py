import mysql.connector as c

def mysql_connection():
    try:
        connection = c.connect(host = 'localhost',
        user = 'root',
        password = 'Yasin@786'
        )
        create_db_query = "CREATE DATABASE Questions"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)


def create_table_2():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database= 'Questions'
                               )
        create_table_query = """
        CREATE TABLE countries(
            COUNTRY_ID varchar(2) unique NOT NULL,
            COUNTRY_NAME varchar(40) NOT NULL,
            REGION_ID int unique NOT NULL
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

def drop_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
                               )
        drop_table = "drop table countries"
        with connection.cursor() as cursor:
            cursor.execute(drop_table)
    except Exception as e:
        print(e)


# ques 3

def create_table_three():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database= 'Questions'
                               )
        create_table_query = """
        CREATE TABLE countries(
            COUNTRY_ID int NOT NULL auto_increment primary key,
            COUNTRY_NAME varchar(40) NOT NULL DEFAULT 'N\A',
            REGION_ID int NOT NULL
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

def insert_into_3():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
                               )
        COUNTRY_NAME = input("Enter country name: ")
        REGION_ID = int(input("Enter region id: "))
        insert_query = "insert into countries(COUNTRY_NAME, REGION_ID) values(%s, %s)"
        connection.cursor()
        data_value = (COUNTRY_NAME, REGION_ID)
        conn = connection.cursor()
        conn.execute(insert_query, data_value)
        connection.commit()
    except Exception as e:
        print(e)


def insert_into2():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
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

# 5
def rename_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
                               )
        alter_table_query = """
            alter table countries rename to country_new
        """
        show_table_query = "DESCRIBE country_new"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

# 6
def add_column():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
                               )
        alter_table_column = """
                    ALTER TABLE country_new
                    ADD state_province VARCHAR(30) after REGION_ID 
              """
        show_table_query = "DESCRIBE country_new"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_column)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

# 7
def change_column_name():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Questions'
                               )
        alter_change_column_name = """
                            ALTER TABLE country_new
                            CHANGE COLUMN state_province state VARCHAR(30);
                      """
        show_table_query = "DESCRIBE country_new"
        with connection.cursor() as cursor:
            cursor.execute(alter_change_column_name)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

def show_table_query():
    try:
        connection = c.connect(host='localhost',
           user='root',
           password='Yasin@786',
           database='Questions'
           )
        show_table_query = "select * from countries"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    # mysql_connection()
    # create_table_2()
    # insert_into2()
    # show_table_query()
    # drop_table()

    # 3
    # create_table_three()
    # insert_into_3()
    # show_table_query()

    # 5
    # rename_table()

    # 6
    # add_column()
    #
    # # 7
    change_column_name()
