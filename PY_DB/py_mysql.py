import pymysql, datetime

# Create Connection
conn = pymysql.connect(host='localhost', port=3306, user='brucy', passwd='brucy_getGoodJob', db='db_playground')

# Create Cursor
cursor = conn.cursor()

# Execute SQL and get effected rows
effect_row = cursor.execute('select * from students')
# print(effect_row) # 20

# get one row of data
# print('The cursor.fetchone() will only return one row of data a time')
# print(cursor.fetchone())
# print(cursor.fetchone()) # the cursor will jump to next one

print('------------------------------------------------------')
print('The cursor.fetchall() will return all remaining matched data, but not formatted')
print(cursor.fetchall())

# print('------------------------------------------------------')
# print('Update:')
# effect_row2 = cursor.execute('update students set name = "GeekyBrucy" where id=1')
# print(effect_row2)

# print('------------------------------------------------------')
# print('executemany:')
# data = [
#   ('GeekyBrucy', 'GeekyBruy@home.org', datetime.date(1993, 6, 25)),
#   ('Cindy Li', 'Cindy.Li@home.org', datetime.date(1993, 5, 26)),
#   ('Bella Liu', 'Bella.Liu@home.org', datetime.date(1993, 4, 9)),
#   ('Bacon Zhou', 'Bacon.Zhou@home.org', datetime.date(2010, 12, 15)),
# ]
# effect_row2 = cursor.executemany('insert into students (name, email, birthday) values (%s, %s, %s)', data)

conn.commit() # must do, otherwise the data won't be updated

cursor.close()
conn.close()