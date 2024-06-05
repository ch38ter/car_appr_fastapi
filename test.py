import sqlite3

conn = sqlite3.connect('./db/appr.db')
cs = conn.cursor()
#sql = "SELECT * FROM member"
# sql = "INSERT INTO member (name, wx_openid, create_time, lastlogin_time, authority) VALUES ('Cheng', 'testabcdefg', '20240331', '20240332', '8');"

# cs.execute(sql)
# conn.commit()
# print(cs.fetchone())
# conn.close()

sql = "UPDATE member SET authority = '9' WHERE wx_openid = 'oVWS664B6mt6IpKpZlrgvVssiAgY';"
cs.execute(sql)
conn.commit()
conn.close()
print('OK')
