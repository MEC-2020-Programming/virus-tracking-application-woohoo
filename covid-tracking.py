from tkinter import *
import tkinter.messagebox
 
class MainWindow:
    def __init__(self):
        self.frame = Tk()
 
        self.label_name = Label(self.frame,text = "country name")
        self.input_name = Entry()
        self.label_name.grid(row = 0,column = 0)
 
        self.button_search = Button(self.frame,text = "Search",width = 10)
        self.button_search.bind("<ButtonRelease-1>",self.buttonListener1)
 
        self.input_name.grid(row = 0,column = 1)
        self.button_search.grid(row = 3,column = 0)
 
        self.frame.mainloop()

    def buttonListener1(self,event):
        name = self.input_name.get()
        result = search(name)
        tkinter.messagebox.showinfo("Report","Data in "+result[0]+" is:\n"+"Total Case: "+result[1]+"\n"+"New Case: "+result[2]+"\n"+"Total Deaths: "+result[3]+"\n"+"Total Recovered: "+result[4]+"\n"+"Avtive Cases: "+result[5]+"\n")
 



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

def search(name):
    i = 0
    for ele in data:
        if ele[0]==name:
            break
        i+=1
    return data[i]

frame = MainWindow()