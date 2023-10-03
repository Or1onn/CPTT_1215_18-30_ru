import sqlite3

connection = sqlite3.connect("db.sl3", 5)

cur = connection.cursor()

# Create DB
# cur.execute("CREATE TABLE first_table (name TEXT);")


# Insert value into db
# INSERT INTO first_table (name) VALUES ('Ahmed')

# Select specific data
# cur.execute("SELECT rowid, name FROM first_table;")

# Update value in db
# cur.execute("UPDATE first_table SET name='Fehruz' WHERE rowid=''2")

# Delete from db
# cur.execute("DELETE FROM first_table WHERE rowid=4")

# DROP
# cur.execute("DROP TABLE first_table")

output = cur.fetchall()
connection.close()
print(output)
