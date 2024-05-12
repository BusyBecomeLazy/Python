# 导入SQLite驱动:
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', ('002',))
# 获得查询结果集:
values = cursor.fetchall()
print(values)  #[('1', 'Michael')]
cursor.close()
conn.close()
