

winnerwinner = open("WorldSeriesWinners.txt","r")
year = 1903
yeardict = {}
teamdict = {}
for element in winnerwinner:
    
    #minor exception handler
    if year == 1904:
        year += 1
    elif year == 1994:
        year += 1
    
    yeardict[year]=element.strip("\n")
    if teamdict.get(element.strip("\n"),'F') == 'F':
        teamdict[element.strip("\n")]=1
    else:
        teamdict[element.strip("\n")] += 1
    year += 1

request = int(input('What year(1903-2008) do you want to know?'))

if request == 1904:
    print('we don\'t talk about that year')
elif request == 1994:
    print("we also don't talk about that year")
elif yeardict.get(request,"F") == "F":
    print("run me again and pick a good year")
else:
    print("The ",yeardict[request]," won in the year ", request.__str__(), ". The ", yeardict[request], " have won the World Series ", teamdict[yeardict[request]].__str__(), " times.", sep= "")
