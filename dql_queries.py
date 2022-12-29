import mysql.connector as c


def create_database():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           )
    create_db_query = "CREATE DATABASE data_query_lang"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)

def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'data_query_lang'
                           )
    create_table_query ="""
    CREATE TABLE Students_info(
            id int auto_increment,
            name varchar(50) not null,
            age int not null,
            percentage int not null,
            address varchar(60) not null,
            primary key(id)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)


def select_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='data_query_lang'
                           )
    select_table_query = "select * from Students_info"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

def selected_column_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='data_query_lang'
                           )
    select_columns_query = "select name, age from Students_info"
    with connection.cursor() as cursor:
        cursor.execute(select_columns_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

def insert_values():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='data_query_lang'
                           )
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    percentage = float(input("Enter percentage: "))
    address = input("Enter address: ")
    insert_data = 'INSERT INTO Students_info(name, age,  percentage, address) values(%s ,%s, %s, %s)'
    data_value = (name, age,  percentage, address)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()


if __name__ == '__main__':
    # create_database()
    # create_table()
    # insert_values()
    # select_query()
    selected_column_query()