# 1
import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

conn.commit()
conn.close()

# 2
import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

# 3
import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

conn.commit()
conn.close()

# 4
import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
""")

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()

