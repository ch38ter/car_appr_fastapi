import sqlite3

conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "ALTER TABLE appr ADD COLUMN status VARCHAR DEFAULT '0';"
cs.execute(sql)
conn.commit()
conn.close()
print('OK')
