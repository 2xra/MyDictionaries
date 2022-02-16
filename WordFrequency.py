filetoread = input("What file should I read? (no extensions please!)").__str__()+'.txt'
wordcount = {}
ParseMePlease = open(filetoread,"r")
with open(filetoread) as f:
    content = f.readlines()
    ListOWords = []
    for item in content:
        ListOWords += item.split()
        


for word in ListOWords:
    present = wordcount.get(word.lower(),"false")
    if present == 'false':
        wordcount[word.lower()] = 1
    else:
        wordcount[word.lower()] += 1

print(wordcount)
