import pymysql

con = pymysql.connect(host="localhost",user="root",password="",db="python_test")

a = con.cursor()
sql = 'SELECT * from `signin`;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of rows: ",countrow)
data = a.fetchone()
print(data)



