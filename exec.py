import sqlite3  

def ex(file_name):
    with open(file_name, 'r') as file:
        sql = file.read()
    
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for row in results:
        print(row)

connection = sqlite3.connect('university.db')
cursor = connection.cursor()

ex('sql/query_1.sql')
ex('sql/query_2.sql')
ex('sql/query_3.sql')

cursor.close()
connection.close()
