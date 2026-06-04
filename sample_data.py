import sqlite3

conn = sqlite3.connect("employees.db")

cursor = conn.cursor()

employees = [
    ("Sudheer", "IT", 60000),
    ("Ravi", "HR", 45000),
    ("Anjali", "Finance", 70000),
    ("Priya", "IT", 80000)
]

cursor.executemany(
    """
    INSERT INTO employees
    (name, department, salary)
    VALUES(?,?,?)
    """,
    employees
)

conn.commit()
conn.close()

print("Data Inserted")
