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
    canvas.create_text(500,100,text='Welcome to space shooting game',fill='yellow', font=('Purisa',40,'bold'))

    canvas.create_rectangle(150,180,850,500,fill='cyan',outline='white')
    canvas.create_text(350,220,text='How to play:',fill='blue', font=('Purisa',35,'bold'))

    canvas.create_text(500,350,text="You can use arrow key to move the game" +'\n'"and 's' key to shoot the anime"+'\n'+"You have only 3 minutes to play"+'\n'+"- You win when you still alive in 3 minute"+'\n'+"- You lose if you death before 3 minute come",fill='blue', font=('Purisa',25))
   
    canvas.create_oval(400,500,600,700,fill='cyan',outline='yellow')
    canvas.create_text(500,600,text="Start play",font=("",30,'bold'),fill='purple')
        
    winsound.PlaySound('sound/welcome.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)


# !(PART-2)====================================== Main part (play part) =================================
shooter_pos_x=500
shooter_pos_y=500
score=0
click=0
times=0
# !------------- main function----------------
def start_game():
    global simple,medium,special,an_bul_check,my_shooter
    canvas.delete('all')
    canvas.create_image(0,0,image=welcome_img,anchor=NW)
    my_shooter=canvas.create_image(shooter_pos_x,shooter_pos_y,image=fighter,anchor=NW)

                    # !=================create anime and move==================
    def create_anime():
        # !............... simple anime ...................
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

        # !...............  medium anime ...................
        medium_an_1=PhotoImage(file='img/medium.png')
        medium1=canvas.create_image(randrange(200,900),0,image=medium_an_1)

        medium_an_2=PhotoImage(file='img/medium.png')
        medium2=canvas.create_image(randrange(200,900),0,image=medium_an_2)

        # !................... move anime.......................
        while True:
            canvas.move(simple1,0,5)
            canvas.move(simple2,0,6)
            canvas.move(simple3,0,9)
            canvas.move(simple4,0,8)
            canvas.move(simple5,0,7)
            canvas.move(medium1,0,3)
            canvas.move(medium2,0,4)
    
            root.update()
            time.sleep(0.01)
    create_anime()
# !..............create bullets............
winsound.PlaySound('sound/play.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
fighter=PhotoImage(file='img/shooter1.png')

#! ................... move shooter to the left......................
def move_shooter_l(event):
    global shooter_pos_x,shooter_pos_y,my_shooter
    if shooter_pos_x>10:
        shooter_pos_x -=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)
#! ................... move shooter to the right......................
def move_shooter_r(event):
    global shooter_pos_x,shooter_pos_y,my_shooter
    if shooter_pos_x<920:
        shooter_pos_x +=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)

# !................... move the shooter up......................
def move_shooter_u(event):
    global shooter_pos_y,my_shooter
    if shooter_pos_y >0:
        shooter_pos_y -=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)

# !................... move the shooter down......................
def move_shooter_d(event):
    global shooter_pos_y,my_shooter
    if shooter_pos_y<500:
        shooter_pos_y +=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)

# !.............create shooter bullets................
p_bul_img=PhotoImage(file='img/p_bullet.png')
def create_p_bullets():
    global p_bullet,shooter_pos_x,shooter_pos_y
    canvas.after(2000,lambda:create_p_bullets())
    p_bullet=canvas.create_image(shooter_pos_x+20,shooter_pos_y-60,image=p_bul_img,anchor=NW)
    while True:
        canvas.move(p_bullet,0,-8)
        root.update()
        time.sleep(0.01)

#! ...........................create special anime and it's bullet.........................
an_bul=PhotoImage(file='img/an_bullet.png')
def create_an_bullets():
    global an_bullet,an_bul_check,special
    special_an=PhotoImage(file='img/special_anime.png')
    special=canvas.create_image(randrange(100,800),2,image=special_an)

    should_an_bul_pos=canvas.coords(special)

    an_bul=PhotoImage(file='img/an_bullet.png')
    an_bullet=canvas.create_image(should_an_bul_pos[0],should_an_bul_pos[1],image=an_bul)
    canvas.after(4000,lambda:create_an_bullets())
    while True:
        canvas.move(special,0,5)
        canvas.move(an_bullet,0,8)
        root.update()
        time.sleep(0.01)
# !....................check anime bullet meet the shooter or not..................
def an_bul_meet_shooter():
    should_an_bul_pos=canvas.coords(special)
    if should_an_bul_pos[0]==shooter_pos_x and should_an_bul_pos[1]==shooter_pos_y:
        canvas.delete(fighter)
        end_game()
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
if click==0:
    open_game()
elif click==1:
    start_game()
elif click==times:
    end_game()
    
root.bind('<u>',move_shooter_u)
root.bind('<d>',move_shooter_d)
root.bind('<l>',move_shooter_l)
root.bind('<r>',move_shooter_r)


frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()