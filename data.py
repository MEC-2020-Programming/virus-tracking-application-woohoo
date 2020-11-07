

#read file
infile = open('testing.txt','r')
content = infile.read()
data = content.split('\n')
country_number = 0
for i in data:
    data[country_number] = i.split(',')
    k=0
    for ele in data[country_number]:
        data[country_number][k]= ele.strip(' []"')
        k+=1
    country_number+=1
print (data) 
infile.close()
