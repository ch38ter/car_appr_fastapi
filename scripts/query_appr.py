import sqlite3
import pprint
conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "SELECT * FROM appr;"
cs.execute(sql)
res = cs.fetchall()
conn.close()
pprint.pp(res)

print('OK')