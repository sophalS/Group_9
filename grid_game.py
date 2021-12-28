
# !=======================================constant===============================

MARIO_CELL = 3
DIAMOND_CELL=1
BLUE_DIAMOND_CELL=2
CION_CELL=4
NOTHING=0
GRID_LIN=9
score=0

# !=======================================Variable===============================

grid=[
    [1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,],
    [1,0,0,4,0,0,0,1,4,4,4,1,2,0,0,0,0,0,0,0,],
    [1,0,4,4,4,0,0,1,4,4,4,1,0,0,0,0,0,0,0,0,],
    [1,0,0,4,0,0,2,4,4,4,4,1,0,0,0,0,0,0,0,0,],
    [1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,],
    [0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,1,0,0,1,0,0,0,0,0,0,4,4,4,4,4,0,],
    [3,0,0,0,1,0,0,1,0,0,2,0,0,0,4,1,4,1,4,0,],
    [4,1,1,1,1,0,0,4,0,0,0,0,0,0,0,4,4,4,0,0,],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,4,1,0,0,0,],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
]
# !======================================Draw grid===============================

def draw_grid():
    global move,move_up,move_down,move_left,move_right
    cell_x=0
    cell_y=10
    isWin=True
    if isWin and score<29:
        for row in grid:
            cell_y+=46
            y2=cell_y+46
            cell_x=0
            for col in range(len(row)):
                cell_x+=46
                x2=cell_x+46
                if row[col]==NOTHING:
                    canvas.create_rectangle(cell_x,cell_y,x2,y2,fill='',outline='')
                elif row[col]==DIAMOND_CELL:
                    canvas.create_rectangle(cell_x,cell_y,x2,y2,fill='purple',outline='')
                    diamond=canvas.create_image(cell_x,cell_y,image=diamond_img,anchor='nw')
                elif row[col]==BLUE_DIAMOND_CELL:
                    canvas.create_rectangle(cell_x,cell_y,x2,y2,fill='',outline='')
                    star=canvas.create_image(cell_x,cell_y,image=star_img,anchor='nw')
                elif row[col]==MARIO_CELL:
                    canvas.create_rectangle(cell_x,cell_y,x2,y2,fill='pink',outline='cyan')
                    mari=canvas.create_image(cell_x,cell_y,image=mario_img,anchor='nw')
                elif row[col]==CION_CELL:
                    canvas.create_rectangle(cell_x,cell_y,x2,y2,fill='yellow',outline='')
                    cion=canvas.create_image(cell_x,cell_y,image=cion_img,anchor='nw')
    elif score==29:
        win()
# !======================================Move mario===============================

    def move(direction):
        # !======================================= Defult sound===============================
        canvas.delete("all")
        winsound.PlaySound('sound/fireball.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
        global score
        isTrue=True
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if direction=='right':
                    if (grid[row][col]==MARIO_CELL and col<len(grid[row])-1 ) and (grid[row][col+1] != DIAMOND_CELL) :
                        if grid[row][col+1]==CION_CELL:
                            winsound.PlaySound('sound/coin.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                            score+=1
                        
                        grid[row][col]=0
                        grid[row][col+1]=MARIO_CELL
                        break
                elif direction=='left':
                    if grid[row][col]==MARIO_CELL and col>0 and (grid[row][col-1] != DIAMOND_CELL):
                        if grid[row][col-1]==CION_CELL:
                            winsound.PlaySound('sound/coin.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                            score+=1
                    
                        grid[row][col]=0
                        grid[row][col-1]=MARIO_CELL
                        break
                elif direction=='up':
                    if grid[row][col]==MARIO_CELL and row>0 and (grid[row-1][col] != DIAMOND_CELL) :
                        if grid[row-1][col]==CION_CELL:
                            winsound.PlaySound('sound/coin.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                            score+=1
                        if grid[row][col] != DIAMOND_CELL or  grid[row][col] != BLUE_DIAMOND_CELL:
                            grid[row][col]=0
                            grid[row-1][col]=MARIO_CELL
                            break
                elif direction=='down':
                    if grid[row][col]==MARIO_CELL and row<10 and isTrue and (grid[row+1][col] != DIAMOND_CELL) :
                        if grid[row+1][col]==CION_CELL and isTrue:
                            winsound.PlaySound('sound/coin.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)
                            score+=1
                        grid[row][col]=0
                        grid[row+1][col]=MARIO_CELL
                        isTrue=False
    # !=======================================Game background==========================
        canvas.create_image(0,0,image=background,anchor='nw')
        canvas.create_text(530,600,text='Your score: '+str(score),fill='yellow',font=('',30,'bold'))
        draw_grid()

    def move_right(e):
        move('right')
    def move_left(e):
        move('left')
    def move_up(e):
        move('up')
    def move_down(e):
        move('down')
def win():
    global button_exit,button_replay
    canvas.create_text(500,400,text="YOU WIN !",font=("",25,"bold"),fill="white")
    canvas.create_text(500,450,text="CONGRATULATION !",font=("",25,"bold"),fill="white")
    canvas.create_window(100,500,window=button_exit)
    canvas.create_window(900,500,window=button_replay)
def replay():
    root.destroy()
    os.system('python grid_game.py')
def exit():
    root.destroy()
def check_button():
    canvas.create_window(100,500,window=button_exit)
    canvas.create_window(900,500,window=button_replay)
# !================================== Create window==============================    
from tkinter import*
import winsound
import os
root=Tk()       
root.geometry('1000x700')
frame=Frame()
frame.master.title('project game')
canvas=Canvas(frame)

# !=======================================All images===============================
background=PhotoImage(file='img/Background_g.png')
diamond_img=PhotoImage(file='img/diamond.png')
star_img=PhotoImage(file='img/blue_mix_purple.png')
cion_img=PhotoImage(file='img/cion.png')
mario_img=PhotoImage(file='img/mario.png')

# !=======================================Game background==========================
canvas.create_image(0,0,image=background,anchor='nw')

# !======================================= Create button ==========================
button_exit=Button(text="Exit",padx=10,pady=5,font=("",25,"bold"),bg="cyan",command=exit)
button_replay=Button(text="Replay",padx=10,pady=5,font=("",25,"bold"),bg="cyan",command=replay)

button_check=Button(text="Check button",padx=10,pady=5,font=("",25,"bold"),bg="cyan",command=check_button)
canvas.create_window(200,610,window=button_check)

draw_grid()
# !=======================================All events===============================
root.bind('<Up>',move_up)
root.bind('<Down>',move_down)
root.bind('<Left>',move_left)
root.bind('<Right>',move_right)

frame.pack(expand=True,fill='both')
canvas.pack(expand=True,fill='both')
root.mainloop()