# # !(PART-1)====================================== Create interface =================================
from tkinter import*
import winsound
import time
from random import random, randrange,choice
WIDTH=1000
HEIGHT=700
x=0
y=4
root=Tk()
canvas=Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()
frame=Frame()
frame.master.title("Space shooting game")

# !====================================== Set defult background =================================
welcome_img=PhotoImage(file='img/background.png')
menu_background=canvas.create_image(0,0,image=welcome_img,anchor=NW)

# !====================================== Game introduction (1st window) =================================
def open_game():
    canvas.create_text(680,100,text='Welcome to space shooting game',fill='yellow', font=('Purisa',50,'bold'))

    canvas.create_rectangle(100,180,800,500,fill='cyan',outline='white')
    canvas.create_text(300,220,text='How to play:',fill='blue', font=('Purisa',35,'bold'))

    canvas.create_text(450,350,text="You can use arrow key to move the game" +'\n'"and 's' key to shoot the anime"+'\n'+"You have only 3 minutes to play"+'\n'+"- You win when you still alive in 3 minute"+'\n'+"- You lose if you death before 3 minute come",fill='blue', font=('Purisa',25))
    canvas.create_oval(930,270,1150,480,fill='cyan',outline='yellow',tags='play')
    canvas.create_text(1040,370,text="Start play",font=("",30,'bold'),fill='purple')
        
    winsound.PlaySound('sound/welcome.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)


# !(PART-2)====================================== Main part (play part) =================================
pos_x=500
pos_y=500

# ------------- main function----------------
def start_game():
    global simple,medium,special,simple_an_coord,shooter_coord,pos_x,pos_y,move_shooter_u,move_shooter_d,move_shooter_l,move_shooter_r
    canvas.delete('all')
    canvas.create_image(0,0,image=welcome_img,anchor=NW)

    # =================create anime and move==========================
    def create_anime():
        # ............... simple anime ...................
        simple_an_1=PhotoImage(file='img/simple_anime.png')
        simple1=canvas.create_image(randrange(5,100),0,image=simple_an_1)

        simple_an_2=PhotoImage(file='img/simple_anime.png')
        simple2=canvas.create_image(randrange(300,800),0,image=simple_an_2)

        simple_an_3=PhotoImage(file='img/simple_anime.png')
        simple3=canvas.create_image(randrange(100,600),0,image=simple_an_3)

        simple_an_4=PhotoImage(file='img/simple_anime.png')
        simple4=canvas.create_image(randrange(40,300),0,image=simple_an_4)

        simple_an_5=PhotoImage(file='img/simple_anime.png')
        simple5=canvas.create_image(randrange(1,700),0,image=simple_an_5)

         # ...............  medium anime ...................
        medium_an_1=PhotoImage(file='img/medium.png')
        medium1=canvas.create_image(randrange(200,900),0,image=medium_an_1)

        medium_an_2=PhotoImage(file='img/medium.png')
        medium2=canvas.create_image(randrange(200,900),0,image=medium_an_2)

         # ............... special anime ...................
        special_an=PhotoImage(file='img/special_anime.png')
        special=canvas.create_image(randrange(300,700),2,image=special_an)
        canvas.after(4000,lambda:start_game())

        # ................... move anime.......................
        while True:
            canvas.move(simple1,0,5)
            canvas.move(simple2,0,6)
            canvas.move(simple3,0,9)
            canvas.move(simple4,0,8)
            canvas.move(simple5,0,7)
            canvas.move(medium1,0,3)
            canvas.move(medium2,0,4)
            canvas.move(special,0,5)
            root.update()
            time.sleep(0.01)
    create_anime()
winsound.PlaySound('sound/play.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
fighter=PhotoImage(file='img/shooter1.png')
my_shooter=canvas.create_image(pos_x,pos_y,image=fighter,anchor=NW)

# ................... move shooter to the left......................
def move_shooter_l(event):
    global pos_x,my_shooter
    if pos_x>10:
        pos_x -=25
        canvas.moveto(my_shooter,pos_x,pos_y)

# ................... move shooter to the right......................
def move_shooter_r(event):
    global pos_x,my_shooter
    if pos_x<920:
        pos_x +=25
        canvas.moveto(my_shooter,pos_x,pos_y)

# ................... move the shooter up......................
def move_shooter_u(event):
    global pos_y,my_shooter
    if pos_y >0:
        pos_y -=25
        canvas.moveto(my_shooter,pos_x,pos_y)

# ................... move the shooter down......................
def move_shooter_d(event):
    global pos_y,my_shooter
    if pos_y<500:
        pos_y +=25
        canvas.moveto(my_shooter,pos_x,pos_y)
# !(PART-3)====================================== Finish game (after end game interface) =================================
def end_game():
    global score
    canvas.create_oval(540,100,800,250,fill='MAGENTA',outline='yellow',tags='start')
    canvas.create_text(675,180,text=score,font=("",30,'bold'),fill='white')
    canvas.create_text(670,280,text='Your scores!',font=("",30,'bold'),fill='white')
    def play_again():
        canvas.create_rectangle(200,500,500,600,fill='purple',outline='yellow',tags='play')
        canvas.create_text(350,550,text='Play again',font=("",30,'bold'),fill='white')
    play_again()

    def exit_game():
        canvas.create_rectangle(850,500,1150,600,fill='purple',outline='yellow',tags='leave')
        canvas.create_text(1000,550,text='Exit game',font=("",30,'bold'),fill='white')
    exit_game()
    winsound.PlaySound('sound/endG.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)

# !====================================== Check condition to display all above parts =================================
root.bind('<u>',move_shooter_u)
root.bind('<d>',move_shooter_d)
root.bind('<l>',move_shooter_l)
root.bind('<r>',move_shooter_r)


frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()