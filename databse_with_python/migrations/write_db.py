import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO subjects(student_id, name) VALUES (?, ?)
""", (1, "Java"))

conn.commit()

subjects = cursor.fetchall()

for subject in subjects:
    print(subject)

conn.close()