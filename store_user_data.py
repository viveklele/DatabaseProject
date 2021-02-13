import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='vivek',
    database = 'mydatabase'
    )
cur = mydb.cursor(buffered = True)
cur.execute('DROP TABLE COMPANY')
cur.execute('''create table company
           (Company_Name varchar(20),
            cofounder varchar(20),
            NetWorth_USD_DOLLER INT(20))''')  
cur.execute('''insert into company values('tesla','elon_musk',6090),
           ('spacex','elon_musk', 1234),
           ('microsoft','Bill_Gates', 11110),
           ('alphabate','larry page', 6870),
           ('as', 'df', 6900),
           ('wq', 'dfd', 11111),
           ('a', 'ads', 23423),
           ('wqe', 'ew', 3431),
           ('werd', 'hfr', 13413),
           ('bv', 'iu', 8794),
           ('GH', 'jmg', 9758),
           ('et', 'ery', 1290),
           ('HH', 'uyn', 6654),
           ('TE', 'o', 8897)''')
while True:
    def EnteringData():
        try:            
            Company_Name, cof, NetWorth_USD_DOLLER = input('Enter company data in format=>Company_Name,cof,NetWorth_USD_DOLLER : ').split(',')
            cur.execute(f"select Company_Name from company where Company_Name='{Company_Name}'")
            for i in cur:    
                if i[0] == Company_Name:
                    print('data is available')
                    break                    
            else:
                data_viriable = [(Company_Name),(cof),(NetWorth_USD_DOLLER)]
                cur.execute('insert into company values(%s,%s, %s)',data_viriable)
                mydb.commit()
                print('your data is sucessfully added')
        except mysql.connector.Error as err:
            print("Enter integer value for coloum 'NetWorth_USD_DOLLER'\n")
        except ValueError:
            print("Enter input in given format")
    print("Enter '1' for adding data" )
    print("Enter '2' for display data")
    print("Enter '3' for top 5 records")
    print("Enter '4' for exit")   
    user_choise = input('Enter your choise: ')
    if user_choise == '1': 
        EnteringData()
    elif user_choise == '2':
        show_table = cur.execute('select * from company')       
        for i in cur:     
            print(i)
    elif user_choise == '3':
        cur.execute('SELECT NetWorth_USD_DOLLER FROM company ORDER BY NetWorth_USD_DOLLER DESC LIMIT 5')
        for i in cur:
            print(i[0])
    elif user_choise == '4':
        exit()
    else:
        print('invalid choice')
mydb.commit()