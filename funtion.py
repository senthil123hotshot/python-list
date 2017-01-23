def add():
	fo=open("string.txt","r+")
	s=fo.read()
	fo.write('heloo')
	print(s)
	fo.close()
add()
