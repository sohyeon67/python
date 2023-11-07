import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
e_id = "5"
e_name = "6"
gen = "6"
addr = "6"
 
curs = conn.cursor()
sql = f"""
        update emp
        set
            e_name = '{e_name}', 
            gen = '{gen}',
            addr = '{addr}'
        where e_id = '{e_id}'
"""
         
cnt = curs.execute(sql)
print(cnt)
# print(curs.rowcount)

conn.commit()

curs.close()
conn.close()