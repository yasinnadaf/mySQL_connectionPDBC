import mysql.connector as c


def create_database():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           )
    create_db_query = "CREATE DATABASE employee_data"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)

# 8
def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='employee_data'
                           )
    create_table_query = """
       CREATE TABLE employees(
           employee_id int auto_increment,
           first_name varchar(50),
           last_name varchar(50),
           phone_number int,
           email varchar(30),
           hire_date DATE,
           job_id int,
           salary int,
           commission DECIMAL,
           manager_id int,
           department_id int,
           UNIQUE(employee_id)
       )
        """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

# 9
def change_column():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='employee_data'
                           )

    alter_table_column_name = """
                                UPDATE employees SET email='not available',
                                commission=0.10
                          """
    show_table_query = "DESCRIBE employees"
    with connection.cursor() as cursor:
        cursor.execute(alter_table_column_name)
        cursor.execute(show_table_query)
        res = cursor.fetchall()
        print(res)

# 10
def insert_value_to_change():
    pass

def show_tables():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='employee_data'
                           )
    show_table_query = "DESCRIBE  employees"
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)


if __name__ == '__main__':
    # create_database()
    # create_table()
    # show_tables()
    change_column()