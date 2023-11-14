import pymysql

class DaoStudent:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select * from student"
        self.curs.execute(sql)
         
        students = self.curs.fetchall()
        return students

    def selectOne(self, s_id):
        sql = f"""
                select * from student 
                where
                    s_id = '{s_id}'
        """
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
    
    
    def insert(self, s_id, s_name, mobile, grade):
        sql = f"""
                insert into student
                (s_id, s_name, mobile, grade)
                values 
                ('{s_id}', '{s_name}', '{mobile}', '{grade}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def update(self, s_id, s_name, mobile, grade):
        sql = f"""
                update student
                set
                    s_name = '{s_name}', 
                    mobile = '{mobile}',
                    grade = '{grade}'
                where s_id = '{s_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    
    def delete(self, s_id):
        sql = f"""
                delete from student
                where s_id = '{s_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
         


    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DaoStudent()
    list = ds.selectList()
    print(list)