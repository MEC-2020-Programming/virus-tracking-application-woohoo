
#read file
infile = open('testing.txt','r')
content = infile.read()
data = content.split('\n')
country_number = 0
for i in data:
    data[country_number] = i.split(',')
    for k in len(data[country_number]):
        if k=1:
            data[country_number][1]  = data[country_number][1][2:-3]
        else:
            data[country_number][k]  = int(data[country_number][k][2:-2])    
    country_number+=1
print (data) 
infile.close()