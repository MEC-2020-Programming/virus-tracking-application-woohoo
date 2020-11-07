## Read datas
infile = open("testing.txt","r")
content = infile.read()
data = content.split("\n")
countryNum = 0
for i in data:
    data[countryNum] = i.split(",")
    k = 0
    for element in data[countryNum]:
        data[countryNum][k] = element.strip(' []"')
        k += 1
    countryNum += 1


countryName = []

i = 0
while i <= 53:
    countryName.append(data[i][0])
    i += 1

del(countryName[-1])



## Reminders:
totalDeath = 0
totalCases = 0
position = 0

for i in countryName:
    ind = countryName.index(i)
    totalCases += int(data[position][1])
    totalDeath += int(data[position][3])
    position += 1

aveDeathRate = totalDeath / totalCases

position = 0
for i in countryName:
    ind = countryName.index(i)
    if ((int(data[position][3]))/(int(data[position][1]))) > aveDeathRate:
        print("This country, " + i + " have a high risk.")
 print("Process done.")

