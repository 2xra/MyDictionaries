filetoread = input("What file should I read? (no extensions please!)").__str__()+'.txt'
wordcount = {}
ParseMePlease = open(filetoread,"r")
for word in ParseMePlease:
    present = wordcount.get(word,"false")
    if present == 'false':
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print(wordcount)
