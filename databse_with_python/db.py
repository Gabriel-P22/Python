import sqlite3

create_student_table_sql = """
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """

create_registration_table_sql = """
            CREATE TABLE IF NOT EXISTS registrations(
                id INTEGER PRIMARY KEY,
                subject TEXT,
                student_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """

def connect():
    return sqlite3.connect("school.db")

def create_table(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

def create_user(name: str, age: int):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, age) VALUES (?, ?) 
    """, (name, age))
    conn.commit()
    conn.close()

def find_all_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students
    """)
    students = cursor.fetchall()
    for student in students:
        print(student)
    conn.commit()
    conn.close()

def create_registration(user_id: int, name: str):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO registrations(student_id, name) VALUES (?, ?) 
        """, (user_id, name))
    conn.commit()
    conn.close()

def find_all_registrations():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT registrations.id, students.name, registration.subject registration
            FROM registrations
            JOIN students on registrations.student_id = students.id
        """)
    registrations = cursor.fetchall()
    for registration in registrations:
        print(registration)
    conn.commit()
    conn.close()