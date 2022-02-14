filetoread = input("What file should I read? (no extensions please!)").__str__()+'.txt'
wordcount = {}
ParseMePlease = open(filetoread,"r")
with open(filetoread) as f:
    content = f.readlines()
    ListOWords = content[0].split()


for word in ListOWords:
    present = wordcount.get(word,"false")
    if present == 'false':
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print(data)
