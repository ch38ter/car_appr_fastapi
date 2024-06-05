import sqlite3

conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "PRAGMA table_info(appr);"
cs.execute(sql)
print(cs.fetchall())
conn.commit()
conn.close()
print('OK')
