import sqlite3

def create_connecction(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_country(connection, country):
    # 'INSERT INTO countries (title) VALUES (?)'
    try:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO countries (title) VALUES (?)', (country,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_city(connection, city):
    sql = ('INSERT INTO cities (title, area, country_id)'
           'VALUES (?, ?, ?)')
    try:
        cursor = connection.cursor()
        cursor.execute(sql, city)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_students(connection, student):
    sql = ('INSERT INTO students (name, city_id)'
           'VALUES (?, ?)')
    try:
        cursor = connection.cursor()
        cursor.execute(sql, student)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

sql_create_table = ('CREATE TABLE countries ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'title VARCHAR(200) NOT NULL)')
sql_to_create_city = (
    'CREATE TABLE cities ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'title VARCHAR(200) NOT NULL,'
    'area FLOAT(8,2) NOT NULL DEFAULT 0.0,'
    'country_id INTEGER NOT NULL REFERENCES countries (id))'
)
sql_students = (
    'CREATE TABLE students ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name VARCHAR(200) NOT NULL,'
    'city_id INTEGER NOT NULL REFERENCES cities (id))'
)


def choose_city(connection):
    while True:
        print_cities(connection)
        city = int(input('\nВведите id города или 0 чтоб выйти -- '))
        if city == 0:
            print('exiting')
            break
        try:
            sql = (f'SELECT * FROM cities '
                   f'INNER JOIN students, countries ON students.city_id = cities.id '
                   f'AND countries.id = cities.country_id '
                   f'WHERE students.city_id = {city} '
                   # 'INNER JOIN countries ON cities.country_id = countries.id'
                   )
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)

def print_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM cities')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# def show_cities(connection):
#     try:
#         cursor = connection.cursor()
#         cursor.execute('SELECT title FROM cities')
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as e:
#         print(e)


test = create_connecction('hw3.db')


# create_table(test, sql_to_create_city)
# create_table(test, sql_students)
# insert_city(test, ('Tashkent', 33200, 3))
# insert_students(test, ('Arseniy', 1))
# insert_students(test, ('max', 1))
# insert_students(test, ('kiril', 2))
# insert_students(test, ('mom', 3))
# insert_students(test, ('danil', 4))
# insert_students(test, ('alex', 5))
# insert_students(test, ('max2', 6))
# insert_students(test, ('semetey', 7))
# insert_students(test, ('erkay', 1))
# insert_students(test, ('erika', 2))
# insert_students(test, ('nikita', 3))
# insert_students(test, ('vanya', 4))
# insert_students(test, ('emir', 5))
# insert_students(test, ('Aijana', 6))
# insert_students(test, ('adina', 7))
# insert_students(test, ('Adiya', 1))
# print_cities(test)
# choose_city(test)
choose_city(test)
test.close()