import sqlite3

database = "db.sqlite"

conn = sqlite3.connect(database)

print("database connected successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS USERS(
NAME TEXT,
AGE INTEGER,
CLASS TEXT,
CITY TEXT);
''')
print("table created successfully.")

conn.execute('''
INSERT INTO USERS(NAME, AGE, CLASS, CITY) VALUES
             ("Anna", 15, "10th grade", "Lagos");
''')
conn.commit()
print("records added successfully")

import pandas as pd
tables = pd.read_sql('''
select * from sqlite_master where type = "table";
''', conn)
print(tables)
users = pd.read_sql('''
select * from users;
''', conn)
print (users)