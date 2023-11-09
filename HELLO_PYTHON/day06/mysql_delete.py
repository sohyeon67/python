import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
e_id = "5"

 
curs = conn.cursor()
sql = f"""
        delete from emp
        where e_id = '{e_id}'
"""
         
cnt = curs.execute(sql)
print(cnt)
# print(curs.rowcount)

conn.commit()

curs.close()
conn.close()