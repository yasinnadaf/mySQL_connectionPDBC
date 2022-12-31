import mysql.connector as c


def create_database():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           )
    create_db_query = "CREATE DATABASE online_shopy"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)

def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'online_shopy'
                           )
    create_table_query ="""
    CREATE TABLE Customers(
             user_id INT NOT NULL primary key,
             name VARCHAR(50) NOT NULL,
             phone VARCHAR(12),
             address VARCHAR(100)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    user_id = int(input("Enter user_id: "))
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    insert_data = 'INSERT INTO Customers(user_id, name, phone, address) values(%s ,%s, %s, %s)'
    data_value = (user_id, name, phone, address)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    select_table_query = "select * from Customers"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

##########################################

def create_table_item():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'online_shopy'
                           )
    create_table_query ="""
    CREATE TABLE Items(
             item_id INT NOT NULL PRIMARY KEY,
             category_id INT,
             item_name VARCHAR(100) NOT NULL,
             Price int
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values_item():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    item_id = int(input("Enter item_id: "))
    category_id = int(input("Enter category_id: "))
    item_name = input("Enter items name: ")
    price = int(input("Enter price: "))
    insert_data = 'INSERT INTO Items(item_id, category_id, item_name, price) values(%s, %s ,%s, %s)'
    data_value = (item_id, category_id, item_name, price)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query_item():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    select_table_query = "select * from Items"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
#############################################

def create_table_order_history():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'online_shopy'
                           )
    create_table_query ="""
    CREATE TABLE OrderHistory(
            order_history_id INT PRIMARY KEY,
            user_id INT NOT NULL, 
            item_id INT NOT NULL, 
             order_date DATE
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values_in_history_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    order_history_id = int(input("Enter order history id: "))
    user_id = int(input("Enter user id: "))
    item_id = int(input("Enter item id: "))
    order_date = input("Enter order date: ")
    insert_data = 'INSERT INTO OrderHistory(order_history_id, user_id, item_id, order_date) values(%s, %s ,%s, %s)'
    data_value = (order_history_id, user_id, item_id, order_date)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query_history():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='online_shopy'
                           )
    select_table_query = "select * from OrderHistory"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

if __name__ == '__main__':
    # create_database()
    # create_table()
    # insert_values()
    # display_table_query()

    # create_table_item()
    # insert_values_item()
    # display_table_query_item()
    #
    # create_table_order_history()
    # insert_values_in_history_table()
    display_table_query_history()