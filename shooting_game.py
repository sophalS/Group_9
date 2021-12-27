# # !(PART-1)====================================== Create interface =================================
from tkinter import*
import winsound
import time
from random import random, randrange,choice
import os
root=Tk()
root.geometry('1000x700')
frame=Frame()
frame.master.title("Space shooting game")
canvas=Canvas(frame)

# !====================================== Set defult background =================================
welcome_img=PhotoImage(file='img/background.png')
menu_background=canvas.create_image(0,0,image=welcome_img,anchor=NW)
# !====================================== Game introduction (1st window) =================================
# def open_game():
#     canvas.create_text(500,100,text='Welcome to space shooting game',fill='yellow', font=('Purisa',40,'bold'))

#     canvas.create_rectangle(150,180,850,500,fill='cyan',outline='white')
#     canvas.create_text(350,220,text='How to play:',fill='blue', font=('Purisa',35,'bold'))

#     canvas.create_text(500,350,text="You can use arrow key to move the game" +'\n'"and 's' key to shoot the anime"+'\n'+"You have only 3 minutes to play"+'\n'+"- You win when you still alive in 3 minute"+'\n'+"- You lose if you death before 3 minute come",fill='blue', font=('Purisa',25))
   
#     canvas.create_oval(400,500,600,700,fill='cyan',outline='yellow',tags='start')
#     canvas.create_text(500,600,text="Start play",font=("",30,'bold'),fill='purple')
        
#     winsound.PlaySound('sound/welcome.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
# !(PART-2)====================================== Main part (play part) =================================
shooter_pos_x=500
shooter_pos_y=500
score=0
p_bul_list=[]
an_bul_list=[]
an_list=[]
# !(part-1/2)=============================create shooter,shooter bullet,move it =================================
# !.......................create shooter.............................
fighter=PhotoImage(file='img/shooter1.png')
my_shooter=canvas.create_image(shooter_pos_x,shooter_pos_y,image=fighter,anchor=NW)

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

# !................... ....move the shooter up........................
def move_shooter_u(event):
    global shooter_pos_y,my_shooter
    if shooter_pos_y >0:
        shooter_pos_y -=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)

# !................... ....move the shooter down......................
def move_shooter_d(event):
    global shooter_pos_y,my_shooter
    if shooter_pos_y<500:
        shooter_pos_y +=25
        canvas.moveto(my_shooter,shooter_pos_x,shooter_pos_y)

# !.........................create shooter bullets....................
p_bul_img=PhotoImage(file='img/p_bullet.png')
def create_p_bullets(event):
    canvas.delete('p_bullet')
    global p_bullet,shooter_pos_x,shooter_pos_y,p_bul_list
    p_bullet=canvas.create_image(shooter_pos_x+20,shooter_pos_y-60,image=p_bul_img,anchor=NW)
    p_bul_list.append(p_bullet)
    while True:
        canvas.move(p_bullet,0,-8)
        root.update()
        time.sleep(0.01) 
# !(part-2/2)====================================== create anime,anime bullet and move them =================================
# !................Create anime...................
def create_anime():
    global simple_an,simple_img
    simple_img=PhotoImage(file='img/simple_anime.png')
    simple_an=canvas.create_image(randrange(5,100),2,image=simple_img)
    an_list.append(simple_an)
def move_an():
    an_pos=create_anime()
    an_bul_pos=canvas.coords(an_pos)
    if an_bul_pos[1]>600:
        canvas.move(simple_an,0,6)
        root.update()
        time.sleep(0.01) 
# move_an()
# !....................check anime bullet meet the shooter or not..................


# !(PART-3)====================================== Finish game (after end game interface) =================================
# !...............Replay the game....................
def play_again():
    root.destroy()
    os.system('python game.py')

#! ..................Exit game.............
def stop_game():
    root.destroy()
def end_game():
    winsound.PlaySound('sound/endG.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
    canvas.create_oval(450,100,710,250,fill='MAGENTA',outline='yellow',tags='start')
    canvas.create_text(580,180,text=score,font=("",30,'bold'),fill='white')
    canvas.create_text(600,280,text='Your scores!',font=("",30,'bold'),fill='white')
    replay=Button(text='Play again',font=('',30),command=play_again,bg='pink',fg='black')
    stop=Button(text='Exit game',font=('',30),command=stop_game,bg='cyan',fg='black')
    replay.pack(padx=20,pady=20)
    stop.pack(padx=20,pady=20)
    replay.place(x=250,y=450)
    stop.place(x=650,y=450)

# !====================================== Check condition to display all above parts =================================

# !..................all event parts...............
# canvas.tag_bind('start','<Button-1>',click_on_start)
root.bind('<Up>',move_shooter_u)
root.bind('<Down>',move_shooter_d)
root.bind('<Left>',move_shooter_l)
root.bind('<Right>',move_shooter_r)
root.bind('<s>',create_p_bullets)

frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()