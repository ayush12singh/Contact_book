import mysql.connector


class contact:

    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', 
                                            port='3306',
                                            user='root',
                                            password='**********',
                                            database='contact_book')
        print(self.conn)
        self.query = 'CREATE TABLE IF NOT EXISTS contact (user_id  INTEGER PRIMARY KEY,user_name VARCHAR(100),phone_id VARCHAR(100),user_occ VARCHAR(100),mail_id VARCHAR(100))'
        self.cur = self.conn.cursor()
        self.cur.execute(self.query)
        self.conn.commit()

    def inser_in(self, userid, username, phone, occupation, email):
        self.query = "INSERT INTO contact(user_id,user_name,phone_id,user_occ, mail_id) values('{}','{}','{}','{}','{}')".format(
            userid, username, phone, occupation, email)
        self.cur = self.conn.cursor()
        self.cur.execute(self.query)
        self.conn.commit()

    def fetch(self):
        self.query = 'SELECT * FROM contact'
        self.cur = self.conn.cursor()
        self.cur.execute(self.query)
        return self.cur

    def delete(self, userid):
        self.query = 'delete from users where user_id={}'.format(userid)
        self.cur = self.conn.cursor()
        self.cur.execute(self.query)
        self.conn.commit()

    def clearall(self):
        self.query = 'DELETE FROM contact WHERE user_id>0'
        self.cur = self.conn.cursor()
        self.cur.execute(self.query)
        self.conn.commit()

    def updatesql(self, u, n, p, o, e):
        self.q = "UPDATE contact SET user_name='{}' ,phone_id='{}',user_occ='{}',mail_id='{}'where user_id={}".format(n, p, e, o, u)
        self.cur = self.conn.cursor()
        self.cur.execute(self.q)
        self.conn.commit()
