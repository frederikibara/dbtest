import sqlite3
from faker import Faker
import random


def connect_db(db_name):
    return sqlite3.connect(db_name)

def insert_into_database(connection):
    fake = Faker()
    cursor = connection.cursor()

    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        cursor.execute('INSERT INTO groups (group_name, faculty) VALUES (?, ?)', (group_name, fake.word()))

    teachers = []
    for _ in range(3):  
        teacher_name = fake.name()
        subject = fake.word()
        cursor.execute('INSERT INTO teachers (name, subject) VALUES (?, ?)', (teacher_name, subject))
        teachers.append((teacher_name, subject))

    subjects = []
    for _ in range(5): 
        subject_name = fake.word()
        teacher_id = random.choice(range(1, 4))  
        cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject_name, teacher_id))
        subjects.append(subject_name)

    students = []
    for _ in range(random.randint(30, 50)):  
        student_name = fake.name()
        age = random.randint(18, 25)
        group_id = random.choice(range(1, 4))  
        cursor.execute('INSERT INTO students (name, age, group_id) VALUES (?, ?, ?)', (student_name, age, group_id))
        students.append((student_name, group_id))

    for student_id in range(1, len(students) + 1):  
        for _ in range(random.randint(10, 20)):  
            subject_id = random.choice(range(1, 6))  
            grade = random.randint(2, 5)  
            date_received = fake.date_between(start_date='-1y', end_date='today')  
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', 
                           (student_id, subject_id, grade, date_received))

    connection.commit()

if __name__ == "__main__":

    connection = connect_db('university.db')
    insert_into_database(connection)
    connection.close()

    print("Generated data has been entered into databas")