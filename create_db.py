import sqlite3

def connect_db(db_name):
    return sqlite3.connect(db_name)


def create_groups_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        group_name TEXT NOT NULL,
        faculty TEXT NOT NULL)''')

def create_teachers_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT NOT NULL)''')

def create_students_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(group_id))''')
    
def create_subjects_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id))''')

def create_grades_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id))''')

if __name__ == "__main__":
    connection = connect_db('university.db')
    cursor = connection.cursor()

    create_groups_table(cursor)
    create_teachers_table(cursor)
    create_students_table(cursor)
    create_subjects_table(cursor)
    create_grades_table(cursor)

    connection.commit()
    cursor.close()
    connection.close()

    print("DONE! Database & all tables has been created!")
