import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("""
    UPDATE students SET name = ? WHERE id = ?
""", ("Gabriel P", 1))

conn.commit()

conn.close()