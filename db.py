import MySQLdb
conn= MySQLdb.connect(
	'localhost',
	'root',
	'123',
	'testing')
#read

a=conn.cursor()
query='select * from details'
a.execute(query)
data=a.fetchall()
print(data)


#write
id =raw_input('enter the id')
name=raw_input('enter the name')
age=raw_input('enter the age')
query="insert into details values('%s','%s','%s')"%(id,name,age)
a.execute(query)
conn.commit()
query='select * from details'
a.execute(query)
data=a.fetchall()
print(data)

#update
name=raw_input("enter the name to update")
id=raw_input("entet the id")
query="update details set name='%s' where id='%s'"%(name,id)
a.execute(query)
conn.commit()
query='select * from details'
a.execute(query)
data=a.fetchall()
print(data)

#delete
age=raw_input('enter the age to delete')
query="delete from details where age='%s'"%(age)
a.execute(query)
conn.commit()
query='select * from details'
a.execute(query)
data=a.fetchall()
print(data)
