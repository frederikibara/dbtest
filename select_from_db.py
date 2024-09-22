import sqlite3

DELIMITER = '----------------------------------------------------------------'

def connect_db():
    return sqlite3.connect('university.db')


def top_students():
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT s.name AS student_name, 
           AVG(g.grade) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    GROUP BY s.student_id
    ORDER BY average_grade DESC
    LIMIT 5;
    '''

    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"Student: {row[0]}, Average Grade: {row[1]:.2f}")

    cursor.close()
    connection.close()


def best_student_in_subject(subject_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT s.name AS student_name, 
           AVG(g.grade) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    WHERE g.subject_id = ?
    GROUP BY s.student_id
    ORDER BY average_grade DESC
    LIMIT 1;
    '''

    cursor.execute(query, (subject_id,))
    result = cursor.fetchone()
    if result:
        print(f"Best student in subject {subject_id}: {result[0]}, Average Grade: {result[1]:.2f}")
    else:
        print(f"No students found for subject {subject_id}.")

    cursor.close()
    connection.close()


def average_grade_in_groups(subject_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT g.group_name, 
           AVG(gr.grade) AS average_grade
    FROM groups g
    JOIN students s ON g.group_id = s.group_id
    JOIN grades gr ON s.student_id = gr.student_id
    WHERE gr.subject_id = ?
    GROUP BY g.group_id;
    '''

    cursor.execute(query, (subject_id,))
    results = cursor.fetchall()
    for row in results:
        print(f"Group: {row[0]}, Average Grade: {row[1]:.2f}")

    cursor.close()
    connection.close()


def overall_average_grade():
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT AVG(grade) AS overall_average_grade
    FROM grades;
    '''

    cursor.execute(query)
    result = cursor.fetchone()
    print(f"Overall average grade: {result[0]:.2f}" if result[0] is not None else "No grades available.")

    cursor.close()
    connection.close()


def courses_by_teacher(teacher_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT sub.subject_name
    FROM subjects sub
    JOIN teachers t ON sub.teacher_id = t.teacher_id
    WHERE t.teacher_id = ?;
    '''

    cursor.execute(query, (teacher_id,))
    results = cursor.fetchall()
    print(f"Courses taught by teacher {teacher_id}: {[row[0] for row in results]}")

    cursor.close()
    connection.close()


def get_courses_for_student(group_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT s.name AS student_name
    FROM students s
    WHERE s.group_id = ?;
    '''

    cursor.execute(query, (group_id,))
    results = cursor.fetchall()
    print(f"Students in group {group_id}: {[row[0] for row in results]}")

    cursor.close()
    connection.close()


def grades_in_group_for_subject(group_id, subject_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT s.name AS student_name, 
           g.grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    WHERE s.group_id = ? AND g.subject_id = ?;
    '''

    cursor.execute(query, (group_id, subject_id))
    results = cursor.fetchall()
    for row in results:
        print(f"Student: {row[0]}, Grade: {row[1]}")

    cursor.close()
    connection.close()


def average_grade_by_teacher(teacher_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
    SELECT AVG(g.grade) AS average_grade
    FROM grades g
    JOIN subjects sub ON g.subject_id = sub.subject_id
    WHERE sub.teacher_id = ?;
    '''

    cursor.execute(query, (teacher_id,))
    result = cursor.fetchone()
    print(f"Average grade given by teacher {teacher_id}: {result[0]:.2f}" if result[0] is not None else "No grades available for this teacher.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    print('\nTOP 5 STUDENTS WITH MAX AVERAGE SCORES')
    print(DELIMITER)
    top_students()
    print('\nBEST STUDENT IN SUBJECT')
    print(DELIMITER)
    best_student_in_subject(1)  
    print('\nAVERAGE GRADES IN GROUPS')
    print(DELIMITER)
    average_grade_in_groups(1) 
    print('\nOVERALL AVERAGE GRADE')
    print(DELIMITER)  
    overall_average_grade()
    print('\nCOURSES BY TEACHER')
    print(DELIMITER)
    courses_by_teacher(1)         
    print('\nGET COURSES FOR STUDENT')
    print(DELIMITER)
    get_courses_for_student(1)  
    print('\nGET COURSES FOR STUDENT WITH TEACHER')
    print(DELIMITER)
    grades_in_group_for_subject(1, 1)
    print('\nAVERAGE GRADE BY TEACHER')
    print(DELIMITER)
    average_grade_by_teacher(1)
    
      