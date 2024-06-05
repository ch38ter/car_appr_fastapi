import sqlite3
import sys
conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = sys.argv[1]
cs.execute(sql)
conn.commit()
print(cs.fetchall())
conn.close()
print('OK')
