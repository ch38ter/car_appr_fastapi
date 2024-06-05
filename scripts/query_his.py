import sqlite3
import pprint
import sys


conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "SELECT wx_openid FROM member WHERE id = ?;"
cs.execute(sql, (sys.argv[1],))
res = cs.fetchone()
wx_openid = res[0]
sql = "SELECT * FROM appr WHERE member_id = ? AND strftime('%Y', summit_time) = ?;"
cs.execute(sql, (wx_openid, sys.argv[2],))
res = cs.fetchall()
conn.close()
pprint.pp(res)

print('OK')
