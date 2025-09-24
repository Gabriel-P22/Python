import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
""")


conn.commit()

conn.close()