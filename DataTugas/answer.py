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
newest = []
#problem 1: append strings that contain numbers to a list
for word in data:
	for letter in word:
		if letter in number:
			box.append(word)
			break
#problem 2: reverse the list and put the number back to the data in reverse order
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
#problem 3: uppercase the first letter in each sentence
for i in range(len(new)):
	word = data[i]
	wordprev = data[i-1]
	if (wordprev[len(wordprev)-1] == '.') :
		word = word[0].upper() + word[1:]
	newest.append(word)
#not nacessary, write a new file that contains modified data
txt = ' '.join(newest)
f = open("ModifiedDataSet.txt","w+")
f.write(txt)
f.close