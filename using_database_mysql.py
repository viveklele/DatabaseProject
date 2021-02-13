import time
start_time = time.time()
import mysql.connector
import re
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vivek',
    database = 'mydatabase'
    )
cur = mydb.cursor(buffered=True)
cur.execute('DROP TABLE mydata')
cur.execute('CREATE TABLE mydata(name CHAR(10), id INT, Prop_USDDOLLER INT(20))')
cur.execute('''INSERT INTO mydata VALUES
            ('as', 12, 6900),
            ('wq', 23, 11111 ),
            ('a', 34, 23423),
            ('wqe', 234, 3431 ),
            ('werd', 2575, 13413),
            ('bv', 764, 8794),
            ('GH', 895, 9758),
            ('et', 7699, 1290),
            ('HH', 4564, 6654),
            ('TE', 423, 8897)''')
            
#cur.execute('SELECT Prop_USDDOLLER FROM mydata ORDER BY Prop_USDDOLLER DESC LIMIT 5')
name, id, Prop_USDDOLLER = input('Enter company data in format=>Company_Name,cof,NetWorth_USD_DOLLER : ').split(',')
sql_stmt = f"select * from mydata where name='{name}'"
print(sql_stmt)
cur.execute(sql_stmt)
print(cur)
for i in cur:
    print(i)
    if i[0] == Company_Name:
        print('data is available')
        break
    else:
        data_viriable = [(Company_Name),(cof),(NetWorth_USD_DOLLER)]
        cur.execute('insert into company values(%s,%s, %s)',data_viriable)
        mydb.commit()
        print('your data is sucessfully added')
mydb.commit()
print("----%s seconds -----" % (time.time()-start_time))


    