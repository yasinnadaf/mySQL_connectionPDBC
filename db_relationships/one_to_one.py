import mysql.connector as c


def create_database():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           )
    create_db_query = "CREATE DATABASE School"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)

def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'School'
                           )
    create_table_query ="""
    CREATE TABLE Students_table(
            Id INT auto_increment,
            Name VARCHAR(40) NOT NULL,
            Class VARCHAR(20),
            Age INT, primary key(Id)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='School'
                           )
    Name = input("Enter name: ")
    Class = int(input("Enter class: "))
    Age = int(input("Enter age: "))
    insert_data = 'INSERT INTO Students_table(Name, Class, Age) values(%s ,%s, %s)'
    data_value = (Name, Class, Age)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='School'
                           )
    select_table_query = "select * from Students_table"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
# table2
def create_table_2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'School'
                           )
    create_table_query ="""
    CREATE TABLE  Addresses(
            AddressId INT PRIMARY KEY, 
            Address VARCHAR(100) NOT NULL,
            StudentId INT NOT NULL UNIQUE
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values_table2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='School'
                           )
    AddressId = input("Enter address id: ")
    Address = input("Enter address: ")
    StudentId = int(input("Enter StudentId: "))
    insert_data = 'INSERT INTO  Addresses(AddressId, Address, StudentId) values(%s ,%s, %s)'
    data_value = (AddressId, Address, StudentId)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query_2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='School'
                           )
    select_table_query = "select * from  Addresses"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

if __name__ == '__main__':
    # create_database()
    # create_table()
    # insert_values()
    display_table_query()

    #table2
    # create_table_2()
    # insert_values_table2()
    # display_table_query_2()