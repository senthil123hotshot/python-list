
a=[]

m=[[0 for j in range(2)] for i in range(2)]

for i in range(0,2):
	for j in range(0,2):
		m[i][j]=int(raw_input())
n=[[0 for j in range(2)] for i in range(2)]

for i in range(0,2):
	for j in range(0,2):
		n[i][j]=int(raw_input())

c=[[0 for j in range(2)] for i in range(2)]
c[0][0]=0
for i in range(0,2):
	for j in range(0,2):
		c[i][j]=c[i][j]+m[i][j]+n[i][j]
print (c)
a.append(raw_input())
for i in range(0,3):
	print(a[i])
a.sort()
print (a)
a.insert(0,"jhgjksf")
a.pop()
print (a)
a.reverse()
print(a)
a.remove(a[0])
print(a)
#a.extend(5)
print(a)

