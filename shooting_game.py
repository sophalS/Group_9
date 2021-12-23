
from tkinter import*
import winsound
import time
WIDTH=1400
HEIGHT=700
x=0
y=4
root=Tk()
canvas=Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()
frame=Frame()
frame.master.title("Space shooting game")
welcome_img=PhotoImage(file='img/background.png')
menu_background=canvas.create_image(0,0,image=welcome_img,anchor=NW)

# !introduction
def open_game():
    canvas.create_text(680,100,text='Welcome to space shooting game',fill='yellow', font=('Purisa',50,'bold'))

    canvas.create_rectangle(100,180,800,500,fill='cyan',outline='white')
    canvas.create_text(300,220,text='How to play:',fill='blue', font=('Purisa',35,'bold'))

    canvas.create_text(450,350,text="You can use arrow key to move the game" +'\n'"and 's' key to shoot the anime"+'\n'+"You have only 3 minutes to play"+'\n'+"- You win when you still alive in 3 minute"+'\n'+"- You lose if you death before 3 minute come",fill='blue', font=('Purisa',25))
    canvas.create_oval(930,270,1150,480,fill='cyan',outline='yellow',tags='play')
    canvas.create_text(1040,370,text="Start play",font=("",30,'bold'),fill='purple')
        
    winsound.PlaySound('sound/welcome.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)


# !main part
x=1
y=10
score=0
times=0

# set condition to avoid cutting sound without end game and effect to other function
if times ==0:
        winsound.PlaySound('sound/play.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
def start_game():
    canvas.delete('all')
    canvas.create_image(0,0,image=welcome_img,anchor=NW)
    global my_images1,my_images2,my_images3,my_images4,my_images5,my_images6,my_images7,my_images8,my_images9x,y
    simple_anime_1=PhotoImage(file='img/simple_anime.png')
    my_images1=canvas.create_image(200,0,image=simple_anime_1)

    simple_anime_2=PhotoImage(file='img/simple_anime.png')
    my_images2=canvas.create_image(500,1,image=simple_anime_2)

    simple_anime_3=PhotoImage(file='img/simple_anime.png')
    my_images3=canvas.create_image(800,3,image=simple_anime_3)

    simple_anime_4=PhotoImage(file='img/simple_anime.png')
    my_images4=canvas.create_image(1100,5,image=simple_anime_4)

    simple_anime_5=PhotoImage(file='img/special_anime.png')
    my_images5=canvas.create_image(900,2,image=simple_anime_5)

    simple_anime_6=PhotoImage(file='img/medium.png')
    my_images6=canvas.create_image(700,0,image=simple_anime_6)


    #     # !shooter
    img=PhotoImage(file='img/shooter.png')
    my_image=canvas.create_image(600,600,image=img)

    img_width=img.width()
    img_height=img.height()
    canvas.after(1800,lambda:start_game())
    while True:
        canvas.move(my_images1,x,y)
        canvas.move(my_images2,x,y)
        canvas.move(my_images3,x,y)
        canvas.move(my_images4,x,y)
        canvas.move(my_images5,x,y)
        canvas.move(my_images6,x,y)
        root.update()
        time.sleep(0.01)
#! finally part
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


# !Check part
if time==0:
    open_game()
elif time==2:
    start_game()
else:
    end_game()



frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()