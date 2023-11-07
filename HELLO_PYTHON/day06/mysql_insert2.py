import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
e_id = "5"
e_name = "5"
gen = "5"
addr = "5"
 
curs = conn.cursor()
sql = f"""
        insert into emp
        (e_id, e_name, gen, addr)
        values 
        ('{e_id}', '{e_name}', '{gen}', '{addr}')
"""
         
cnt = curs.execute(sql)
print(cnt)
# print(curs.rowcount)

conn.commit()

curs.close()
conn.close()