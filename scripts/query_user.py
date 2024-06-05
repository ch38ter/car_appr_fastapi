import sqlite3

conn = sqlite3.connect('../db/appr.db')
cs = conn.cursor()
sql = "SELECT * FROM member;"
cs.execute(sql)
res = cs.fetchall()
conn.close()
print('{:-<6}'.format('id'),end='')
print('{:-<8}'.format('姓名'),end='')
print('{:-<30}'.format('union_id'),end='')
print('{:-<30}'.format('app_id'),end='')
print('{:-<30}'.format('open_id'),end='')
print('{:-<16}'.format('职位'),end='')
print('{:-<24}'.format('注册时间'),end='')
print('{:-<22}'.format('上次登录时间'),end='')
print('权限')
for row in res:
    
    print('{: <6}'.format(row[0]),end='')
    print('{:　<5}'.format(row[1]),end='')
    print('{: <30}'.format(row[2]),end='')
    print('{: <30}'.format(row[3]),end='')
    print('{: <30}'.format(row[4]),end='')
    print('{:　<9}'.format(row[5]),end='')
    print('{: <28}'.format(row[6]),end='')
    print('{: <28}'.format(row[7]),end='')
    print('{: <3}'.format(row[8]))

print('OK')