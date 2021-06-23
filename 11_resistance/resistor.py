from tkinter import *

root = Tk()
root.geometry("600x400")
val1 = StringVar(value = "Black")
val2 = StringVar(value = "Black")
val3 = StringVar(value = "Black")
val4 = StringVar(value = "Black")
val5 = StringVar(value = "Silver")
list1 = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"]
list2 = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "Nil"]
list3 = ["Silver", "Gold"]
d = {"Silver": 10, "Gold" : 5, "Black": 0, "Brown" : 1, "Red" : 2, "Orange" : 3, "Yellow" : 4, "Green" : 5, "Blue" : 6, "Violet" : 7, "Grey" : 8, "White" : 9, "Nil" : 20}
#################################################################################################
topframe = Frame(root)
topframe.pack(side=TOP, pady = (15, 0), padx = (15, 15))
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM, pady = (15, 15), padx = (15, 15))

column1 = Frame(topframe)
column1.pack(side=LEFT)
column2 = Frame(topframe)
column2.pack(side=LEFT)
column3 = Frame(topframe)
column3.pack(side=LEFT)
column4 = Frame(topframe)
column4.pack(side=LEFT)
column5 = Frame(topframe)
column5.pack(side=LEFT)

info = Frame(bottomframe)
info.pack(side = LEFT)
interface = Frame(bottomframe)
interface.pack(side = RIGHT)
########################################################################################################
def translate(textlist):
    numlist = list()
    for i in textlist:
        numlist.append(d[i])
    return numlist

def calc(numlist):
    out = "The resistance is: "+str(numlist[0])+str(numlist[1])
    if numlist[3]!=20:
        out = out+str(numlist[2])+"x10^"+str(numlist[3])+" ohms with a tolerance of +/-"
    else:
        out = out+"x10^"+str(numlist[2])+" ohms with a tolerance of +/-"
    out = out+str(numlist[4])+"%"
    return out

def main():
    colors = [str(val1.get()), str(val2.get()), str(val3.get()), str(val4.get()), str(val5.get())]
    colorcodes = translate(colors)
    out = calc(colorcodes)
    output.config(text = out)
############################################################################################################
for i in list1:
    Radiobutton(column1, text = i, variable = val1, value = i).pack(anchor = W)
for i in list1:
    Radiobutton(column2, text = i, variable = val2, value = i).pack(anchor = W)
for i in list1:
    Radiobutton(column3, text = i, variable = val3, value = i).pack(anchor = W)
for i in list2:
    Radiobutton(column4, text = i, variable = val4, value = i).pack(anchor = W)
for i in list3:
    Radiobutton(column5, text = i, variable = val5, value = i).pack(anchor = W)

button1 = Button(interface, text = "Calculate", command=main)
button1.pack(side = TOP)

output = Label(interface)
output.pack(side = BOTTOM)
output.config(text = "Select colors and press button")
#############################################################################################################

root.title("Resistance")
root.mainloop()

