import sqlite3
import sys
conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "DELETE FROM appr WHERE id = ?"
cs.execute(sql, (sys.argv[1],))
conn.commit()
conn.close()
print('OK')
