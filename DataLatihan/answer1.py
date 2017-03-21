data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

x = readData(data1)
a = []
for i in x:
	if i == 'I': a.append('*')
	elif ((i == 'and') or (i == 'the') or (i == 'you')): a.append('*'*3)
	else: a.append(i)
b = ' '.join(a)
print(b)