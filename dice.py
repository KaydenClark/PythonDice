from tkinter import *
from random import randint

root = Tk()

def d4():
    print("D4", randint(1,4))
def d6():
    print("D6", randint(1,6))
def d8():
    print("D8", randint(1,8))
def d10():
    print("D10", randint(1, 10))
def d12():
    print("D12", randint(1,12))
def d20():
    roll = randint(1,20)
    print("D20", roll)
def d100():
    print("D100",  randint(1,100))
def percentageDie():
    print(randint(0,9)*10,"+",randint(0,9))

app = Frame(root)
app.pack
label =Label(app,text = "Dice Things")
label.pack()
root.title("Pocket Dice")

d4 = Button(root, text= "D4", bg= "black", fg= "white", command= d4)
d4.pack(fill=X)

d6 = Button(root, text= "D6", bg= "blue", fg= "white", command= d6)
d6.pack(fill=X)

d8 = Button(root, text= "D8", bg= "yellow", fg= "black", command= d8)
d8.pack(fill=X)

d10 = Button(root, text= "D10", bg= "purple", fg= "white", command= d8)
d10.pack(fill=X)

d12 = Button(root, text= "D12", bg= "green", fg= "white", command= d12)
d12.pack(fill=X)

d20 = Button(root, text= "D20", bg= "red", fg= "white", command= d20)
d20.pack(fill=X)

d100 = Button(root, text= "D100", bg= "orange", fg= "black", command= d100)
d100.pack(fill=X)

percentageDie = Button(root, text= "Percentage Die", command= percentageDie)
percentageDie.pack(fill=X)

root.geometry("500x220")
root.mainloop()


