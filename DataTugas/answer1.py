data1 = "DataSet.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

data = readData(data1)
number = ["1","2","3","4","5","6","7","8","9","0"]
box = []
new = []
for word in data:
	for letter in word:
		if letter in number:
			box.append(word)
			break
box.reverse()
i = 0
for word in data:
	for letter in word:
		if letter in number:
			new.append(box[i])
			i += 1
			break
		else:
			new.append(word)
			break

txt = ' '.join(new)
f = open("ModifiedDataSet.txt","w+")
f.write(txt)
f.close