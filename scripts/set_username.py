import sqlite3
import sys
conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "UPDATE member SET name = ? WHERE id = ?;"
cs.execute(sql, (sys.argv[2], sys.argv[1]))
conn.commit()
sql = "SELECT name FROM member WHERE id = ?;"
cs.execute(sql, (sys.argv[1],))
print(cs.fetchone()[0])
conn.close()
print('OK')
