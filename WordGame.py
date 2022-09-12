from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 
 
import random

chances=0;
LT01=""
LT02=""
LT03=""
LT04=""
LT05=""
LT06=""
LT07=""


list3=['box','can','dog','zip','ice']
#list4= ['fast','file','land','palm','snow']
#list6=['flower','island','search','square','volume']

listN=[1,2,3,4,5]

answer1=""
answer2=""
answer3=""



def raise_frame(frame):
    frame.tkraise()
 
def finish():
    root.destroy()
 
def start1():
    raise_frame(f1)
def start2():
    raise_frame(f2)
def start3():
    raise_frame(f3)
def start4():
    raise_frame(f4)
def start5():
    global listN
    global answer1
    answer1= random.choice(listN);
    
    if(answer1==1):
        l611 = Label(f5, text = "",image=box1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f5, text = "",image=box2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f5, text = "",image=box3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f5, text = "",image=box4, width=200,height=200).place(x = 260, y = 210)
    if(answer1==2):
        l611 = Label(f5, text = "",image=can1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f5, text = "",image=can2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f5, text = "",image=can3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f5, text = "",image=can4, width=200,height=200).place(x = 260, y = 210)
    if(answer1==3):
        l611 = Label(f5, text = "",image=dog1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f5, text = "",image=dog2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f5, text = "",image=dog3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f5, text = "",image=dog4, width=200,height=200).place(x = 260, y = 210)
    if(answer1==4):
        l611 = Label(f5, text = "",image=zip1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f5, text = "",image=zip2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f5, text = "",image=zip3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f5, text = "",image=zip4, width=200,height=200).place(x = 260, y = 210)
    if(answer1==5):
        l611 = Label(f5, text = "",image=ice1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f5, text = "",image=ice2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f5, text = "",image=ice3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f5, text = "",image=ice4, width=200,height=200).place(x = 260, y = 210)

    L01 = Label(f5, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 750,y=100)
    L02 = Label(f5, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 800,y=100)
    L03 = Label(f5, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 850,y=100)
    raise_frame(f5)
   
def start6():
    global listN
    global answer2
    answer2= random.choice(listN);
    
    if(answer2==1):
        l611 = Label(f6, text = "",image=fast1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f6, text = "",image=fast2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f6, text = "",image=fast3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f6, text = "",image=fast4, width=200,height=200).place(x = 260, y = 210)
    if(answer2==2):
        l611 = Label(f6, text = "",image=file1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f6, text = "",image=file2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f6, text = "",image=file3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f6, text = "",image=file4, width=200,height=200).place(x = 260, y = 210)
    if(answer2==3):
        l611 = Label(f6, text = "",image=land1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f6, text = "",image=land2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f6, text = "",image=land3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f6, text = "",image=land4, width=200,height=200).place(x = 260, y = 210)
    if(answer2==4):
        l611 = Label(f6, text = "",image=palm1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f6, text = "",image=palm2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f6, text = "",image=palm3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f6, text = "",image=palm4, width=200,height=200).place(x = 260, y = 210)
    if(answer2==5):
        l611 = Label(f6, text = "",image=snow1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f6, text = "",image=snow2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f6, text = "",image=snow3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f6, text = "",image=snow4, width=200,height=200).place(x = 260, y = 210)


    L01 = Label(f6, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 700,y=100)
    L02 = Label(f6, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 750,y=100)
    L03 = Label(f6, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 800,y=100)
    L04 = Label(f6, text = "_",
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 850,y=100)
    raise_frame(f6)
def start7():
    global listN
    global answer3
    answer3= random.choice(listN);
    if(answer3==1):
        l611 = Label(f7, text = "",image=flower1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f7, text = "",image=flower2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f7, text = "",image=flower3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f7, text = "",image=flower4, width=200,height=200).place(x = 260, y = 210)
    if(answer3==2):
        l611 = Label(f7, text = "",image=island1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f7, text = "",image=island2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f7, text = "",image=island3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f7, text = "",image=island4, width=200,height=200).place(x = 260, y = 210)
    if(answer3==3):
        l611 = Label(f7, text = "",image=search1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f7, text = "",image=search2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f7, text = "",image=search3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f7, text = "",image=search4, width=200,height=200).place(x = 260, y = 210)
    if(answer3==4):
        l611 = Label(f7, text = "",image=square1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f7, text = "",image=square2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f7, text = "",image=square3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f7, text = "",image=square4, width=200,height=200).place(x = 260, y = 210)
    if(answer3==5):
        l611 = Label(f7, text = "",image=volume1, width=200,height=200).place(x = 50, y = 0)
        l612 = Label(f7, text = "",image=volume2, width=200,height=200).place(x = 260, y = 0)
        l613 = Label(f7, text = "",image=volume3, width=200,height=200).place(x = 50, y = 210)
        l614 = Label(f7, text = "",image=volume4, width=200,height=200).place(x = 260, y = 210)


    L01 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 700,y=100)
    L02 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 750,y=100)
    L03 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 800,y=100)
    L04 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 850,y=100)
    L05 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 900,y=100)
    L06 = Label(f7, text = "_",
                fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 950,y=100)
    raise_frame(f7)
def start8():
    raise_frame(f8)
def start9():
    raise_frame(f9)
def start10():
    raise_frame(f10)
#-------------------------------------------------------------------
#Easy Game Calculations
#-------------------------------------------------------------------
    
def clicked(alphabet):
    global answer1
    global chances
    global LT01
    global LT02
    global LT03
    Data=list3[answer1-1]    
    if alphabet in Data: 
        if alphabet==Data[0]:
            LT01=Data[0]
            L01 = Label(f5, text = Data[0],
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 750,y=100)
        elif alphabet==Data[1]:
            LT02=Data[1]
            L02 = Label(f5, text = Data[1],
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 800,y=100)
        elif alphabet==Data[2]:
            LT03=Data[2]
            L03 = Label(f5, text = Data[2],
                 fg="black",bg="pink", font = "Helvetica 16 bold",height=1,width=3).place(x = 850,y=100)
    else:
        chances = chances + 1;
        if chances==1:
            #l611 = Label(f5, text = "",image=ph29, width=400,height=400).place(x = 800, y = 20)
            messagebox.showinfo("Word Guessing Game", "You have Last 2 chances")
        elif chances==2:
            #l621 = Label(f5, text = "",image=ph30, width=400,height=400).place(x = 800, y = 20)
            messagebox.showinfo("Word Guessing Game", "You have Last 1 chance")
        elif chances==3:
            #l631 = Label(f5, text = "",image=ph31, width=400,height=400).place(x = 800, y = 20)
            messagebox.showinfo("Word Guessing Game","Answer is "+Data)
            chances=0
            LT01="1"
            LT02="2"
            LT03="3"
            raise_frame(f10)
            
    if LT01==Data[0] and LT02==Data[1] and LT03==Data[2] :
        chances=0
        LT01="1"
        LT02="2"
        LT03="3"
        raise_frame(f8)

#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------



    
root = Tk()
f4 = Frame(root)
f5 = Frame(root)
f8 = Frame(root)
f10 = Frame(root)
 

f4.place(x = 0,y = 250,height=450, width=1200)
f5.place(x = 0,y = 250,height=450, width=1200)
f8.place(x = 0,y = 250,height=450, width=1200)
f10.place(x = 0,y = 250,height=450, width=1200)

 


#----------------GameMode Page-------------------------------------------------------------------------



l3 = Label(f4, text = "Game Levels",
                 fg="black",bg="white", font = "Chiller 40 bold",height=1,width=20).place(x = 400,y=0)

b1 = Button(f4, text = "Start",
            fg="white",bg="black", font = "Elephant 20 bold",height=1,width=15,command = start5).place(x = 450, y = 100)

b5 = Button(f4, text = "Quit",
            fg="white",bg="black", font = "Elephant 18 bold",height=1,width=10,command = finish).place(x = 600, y = 300)
f4.config(bg='white')
#----------------EasyGame Page-------------------------------------------------------------------------
# cat,dog,fox,yak,pig
lname = Label(f5, text = "Name of item/animal in 3 Letters",
                 fg="black",bg="white", font = "Helvetica 16 bold",height=1,width=30).place(x = 600,y=10)

box1=ImageTk.PhotoImage(Image.open("imgs/3/box1.jpeg"))
box2=ImageTk.PhotoImage(Image.open("imgs/3/box2.jpeg"))
box3=ImageTk.PhotoImage(Image.open("imgs/3/box3.jpeg"))
box4=ImageTk.PhotoImage(Image.open("imgs/3/box4.jpeg"))

can1=ImageTk.PhotoImage(Image.open("imgs/3/can1.jpeg"))
can2=ImageTk.PhotoImage(Image.open("imgs/3/can2.jpeg"))
can3=ImageTk.PhotoImage(Image.open("imgs/3/can3.jpeg"))
can4=ImageTk.PhotoImage(Image.open("imgs/3/can4.jpeg"))

dog1=ImageTk.PhotoImage(Image.open("imgs/3/dog1.jpeg"))
dog2=ImageTk.PhotoImage(Image.open("imgs/3/dog2.jpeg"))
dog3=ImageTk.PhotoImage(Image.open("imgs/3/dog3.jpeg"))
dog4=ImageTk.PhotoImage(Image.open("imgs/3/dog4.jpeg"))

ice1=ImageTk.PhotoImage(Image.open("imgs/3/ice1.jpeg"))
ice2=ImageTk.PhotoImage(Image.open("imgs/3/ice2.jpeg"))
ice3=ImageTk.PhotoImage(Image.open("imgs/3/ice3.jpeg"))
ice4=ImageTk.PhotoImage(Image.open("imgs/3/ice4.jpeg"))

zip1=ImageTk.PhotoImage(Image.open("imgs/3/zip1.jpeg"))
zip2=ImageTk.PhotoImage(Image.open("imgs/3/zip2.jpeg"))
zip3=ImageTk.PhotoImage(Image.open("imgs/3/zip3.jpeg"))
zip4=ImageTk.PhotoImage(Image.open("imgs/3/zip4.jpeg"))


b40 = Button(f5, text = "Change",fg="white",bg="black",font = "Helvetica 16 bold",width=7,command=start4).place(x = 760, y = 370)
b30 = Button(f5, text = "Quit",fg="white",bg="black",font = "Helvetica 16 bold",width=7,command=finish).place(x = 910, y = 370)

a = Button(f5, text = "A",font = "Helvetica 16 bold",width=3,command=lambda: clicked("a")).place(x = 500, y = 270)
b = Button(f5, text = "B",font = "Helvetica 16 bold",width=3,command=lambda: clicked("b")).place(x = 550, y = 270)
c = Button(f5, text = "C",font = "Helvetica 16 bold",width=3,command=lambda: clicked("c")).place(x = 600, y = 270)
d = Button(f5, text = "D",font = "Helvetica 16 bold",width=3,command=lambda: clicked("d")).place(x = 650, y = 270)
e = Button(f5, text = "E",font = "Helvetica 16 bold",width=3,command=lambda: clicked("e")).place(x = 700, y = 270)
f = Button(f5, text = "F",font = "Helvetica 16 bold",width=3,command=lambda: clicked("f")).place(x = 750, y = 270)
g = Button(f5, text = "G",font = "Helvetica 16 bold",width=3,command=lambda: clicked("g")).place(x = 800, y = 270)
h = Button(f5, text = "H",font = "Helvetica 16 bold",width=3,command=lambda: clicked("h")).place(x = 850, y = 270)
i = Button(f5, text = "I",font = "Helvetica 16 bold",width=3,command=lambda: clicked("i")).place(x = 900, y = 270)
j = Button(f5, text = "J",font = "Helvetica 16 bold",width=3,command=lambda: clicked("j")).place(x = 950, y = 270)
k = Button(f5, text = "K",font = "Helvetica 16 bold",width=3,command=lambda: clicked("k")).place(x = 1000, y = 270)
l = Button(f5, text = "L",font = "Helvetica 16 bold",width=3,command=lambda: clicked("l")).place(x = 1050, y = 270)
m = Button(f5, text = "M",font = "Helvetica 16 bold",width=3,command=lambda: clicked("m")).place(x = 1100, y = 270)

n = Button(f5, text = "N",font = "Helvetica 16 bold",width=3,command=lambda: clicked("n")).place(x = 500, y = 314)
o = Button(f5, text = "O",font = "Helvetica 16 bold",width=3,command=lambda: clicked("o")).place(x = 550, y = 314)
p = Button(f5, text = "P",font = "Helvetica 16 bold",width=3,command=lambda: clicked("p")).place(x = 600, y = 314)
q = Button(f5, text = "Q",font = "Helvetica 16 bold",width=3,command=lambda: clicked("q")).place(x = 650, y = 314)
r = Button(f5, text = "R",font = "Helvetica 16 bold",width=3,command=lambda: clicked("r")).place(x = 700, y = 314)
s = Button(f5, text = "S",font = "Helvetica 16 bold",width=3,command=lambda: clicked("s")).place(x = 750, y = 314)
t = Button(f5, text = "T",font = "Helvetica 16 bold",width=3,command=lambda: clicked("t")).place(x = 800, y = 314)
u = Button(f5, text = "U",font = "Helvetica 16 bold",width=3,command=lambda: clicked("u")).place(x = 850, y = 314)
v = Button(f5, text = "V",font = "Helvetica 16 bold",width=3,command=lambda: clicked("v")).place(x = 900, y = 314)
w = Button(f5, text = "W",font = "Helvetica 16 bold",width=3,command=lambda: clicked("w")).place(x = 950, y = 314)
x = Button(f5, text = "X",font = "Helvetica 16 bold",width=3,command=lambda: clicked("x")).place(x = 1000, y = 314)
y = Button(f5, text = "Y",font = "Helvetica 16 bold",width=3,command=lambda: clicked("y")).place(x = 1050, y = 314)
z = Button(f5, text = "Z",font = "Helvetica 16 bold",width=3,command=lambda: clicked("z")).place(x = 1100, y = 314)
f5.config(bg='white')    


#----------------Result Win Page-----------------------------------------------------------------------

p13=ImageTk.PhotoImage(Image.open("w3.jpg"))
l8 = Label(f8, text = "",image=p13, width=250,height=250).place(x = 400, y = 50)

l4 = Label(f8, text = "YOU WON THE GAME",bg="white",
                 font = "Helvetica 30 bold",height=1,width=30).place(x = 220,y=300)

b21 = Button(f8, text = "Play again",
            fg="white",bg="black", font = "Chiller 16 bold",height=1,width=10,command=start4).place(x = 320, y = 370)

b23 = Button(f8, text = "Quit",
            fg="white",bg="black", font = "Chiller 16 bold",height=1,width=10,command=finish).place(x = 680, y = 370)
f8.config(bg='white') 
#----------------Result Lose Page-----------------------------------------------------------------------

p113=ImageTk.PhotoImage(Image.open("los1.jpeg"))
l8 = Label(f10,bg = "white", text = "",image=p113, width=300,height=230).place(x = 400, y = 50)

l4 = Label(f10, text = "YOU LOSE THE GAME",bg="white",
                 font = "Helvetica 30 bold",height=1,width=30).place(x = 220,y=300)

b21 = Button(f10, text = "Play again",
            fg="white",bg="black", font = "Chiller 16 bold",height=1,width=10,command=start4).place(x = 320, y = 370)

b23 = Button(f10, text = "Quit",
            fg="white",bg="black", font = "Chiller 16 bold",height=1,width=10,command=finish).place(x = 680, y = 370)
f10.config(bg='white') 

#----------------About Page------------------------------------------------------------------------


#----------------------------------------------------------------------------------


raise_frame(f4)
root.geometry("1200x700+50+20")
root.configure(bg='white')
root.title("WORD GUESSING GAME")
root.mainloop()





