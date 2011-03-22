from string import punctuation

items = ['wedding', 'property', 'society', 'pride', 'marriage', 'engagement']

vocab = set()
x = input("Enter the window")
n = int(x)
f = open("1342.txt")
for line in f:
    for word in line.split():
        vocab.add(word.strip(punctuation).lower())

for item in items:
    f.seek(0,0)

    a = dict((v,0) for v in vocab)
    for line in f:
        l = []
        for word in line.split():
        	l.append(word.strip(punctuation).lower())
        #print(l)
        try:
        	windex = l.index(item)
        	#print(windex)
        except:
        	#print("caught exception")
        	continue
        for prev in l[windex-n:windex]:
        	#print(prev)
        	a[prev] = a.get(prev,0) + 1
        for after in l[windex+1:windex+n+1]:
        	print(after)
        	a[after] = a.get(after,0) + 1
    print(item,':',a)
f.close()
