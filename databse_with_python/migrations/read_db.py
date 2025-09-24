import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM subjects
""")

conn.commit()

conn.close()