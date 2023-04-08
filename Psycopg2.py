import psycopg2
import psycopg2.extras # to make the datas into dictionary format use this library at cursor


hostname = 'localhost'
database = 'postgres'
user_name = 'postgres'
pwd = 'postgres'
port_id = 1111
conn = None
cur = None


try:
    conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = user_name,
    password = pwd,
    port = port_id)

    #create a table

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #here it returns the datas as dictionary format (optional)
    cur.execute('DROP TABLE IF exists madhavan.developers')

    create_script = ''' CREATE TABLE IF NOT EXISTS madhavan.DEVELOPERS (
        ID int not null primary key,
        NAME varchar (40) not null,
        SALARY float,
        CLIENT varchar(40))'''

    cur.execute(create_script)
    
    
    # insert a data's into table 
    insert_script = 'INSERT INTO madhavan.DEVELOPERS (ID,NAME,SALARY,CLIENT) VALUES (%s,%s,%s,%s)'
    insert_values = [(1001,'Madhavan',4.2,'AbbVie'),(1002,'Aakash',4.2,'AbbVie'),(1003,'Mathu',5.5,'HCL'),(1004,'Maddy',5.5,'HCL')]
    for record in insert_values:             #for loop t insert multiple values
        cur.execute(insert_script,record)


     #Update a table in Database
    update_script = "UPDATE madhavan.DEVELOPERS set SALARY = SALARY + 1 WHERE CLIENT =  'HCL'"
    cur.execute(update_script)
    

    #Delete Script
    delete_script = 'DELETE FROM madhavan.developers where client = %s'
    delete_record = ('AbbVie',)
    cur.execute(delete_script,delete_record)


    #to print valuesin visual code
    cur.execute('SELECT * FROM madhavan.DEVELOPERS') 
    #print(cur.fetchall())
    for value in cur.fetchall():
        print(value['name'],value['salary'])     #here use small letter characters because in db default type is small alphabets


    conn.commit() #commit it tells to the database to take data and save
except Exception as Error:
    print(Error)

finally:
    if conn is not None:
        conn.close()
    if cur is not None:
        cur.close()