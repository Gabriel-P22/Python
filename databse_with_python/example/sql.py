import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Gabriel", 24))

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()