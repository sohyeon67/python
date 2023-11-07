import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
curs = conn.cursor()
sql = """
        insert into emp
        (e_id, e_name, gen, addr)
        values 
        (%s, %s, %s, %s)
"""
         
curs.execute(sql, ('4', '4', '4', '4'))
conn.commit()

curs.close()
conn.close()