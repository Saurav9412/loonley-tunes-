import pygame as pg,sys
from pygame.locals import*
import time
from tkinter import*

winner=None
draw=False
height=600
width=600
X0='Bugs Bunny'
white=(255,255,255)
line_color=(10,10,10)

#board
TTT=[[None]*3,[None]*3,[None]*3]

#loading images
opening_image=pg.image.load('Opening.jpg')
duffy_image=pg.image.load('duffy.jpg')
bunny_image=pg.image.load('bunny.jpg')
#resizing the images
opening_image=pg.transform.scale(opening_image,(height,width))
duffy_image=pg.transform.scale(duffy_image,(100,100))
bunny_image=pg.transform.scale(bunny_image,(100,100))

#intialising the window
pg.init()
fps=30
clock=pg.time.Clock()
Screen=pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption('Loonley Toons')


def opening_window():
    Screen.blit(opening_image,(0,0))
    pg.display.update()
    time.sleep(1)
    Screen.fill(white)

    #vertical lines
    pg.draw.line(Screen,line_color,(width/3,0),(width/3,height),8)
    pg.draw.line(Screen,line_color,(width/3*2,0),(width/3*2,height),8)
    #horizontal lines
    pg.draw.line(Screen,line_color,(0,height/3),(width,height/3),8)
    pg.draw.line(Screen,line_color,(2,height/3*2),(width,height/3*2),8)

    draw_status()

def draw_status():
    global draw

    if winner is None:
        message=X0 +"'s turn"
    else:
        message=winner.upper()+" Won"
    if draw:
        message="It's a Draw".Capatilize()

    font=pg.font.Font(None, 30)
    text= font.render(message , 1, (255,255,255))

    #copying the message to the board
    Screen.fill((0,0,0),(0, 600, 600, 100))
    text_rect=text.get_rect(center=(width/2,600+50))
    Screen.blit(text,text_rect)
    pg.display.update()

def Win_Checking():
    global TTT,winner,draw

    #checling rows
    for row in range(0,3):
        if ((TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0] )is not None):
            winner=TTT[row][0]
            pg.draw.line(Screen ,(250,0,0) ,(0,(row+1)*height/3-height/6),\
            (width,(row+1)*height/3-height/6),4)
            break
    #checking columns
    for column in range (0,3):
        if((TTT[0][column]==TTT[1][column]==TTT[2][column])and (TTT[0][column]) is not None):
            winner=TTT[0][column]
            pg.draw.line(Screen ,(250,0,0) ,((column+1)*width/3-width/6,0),\
            ((column+1)*width/3-width/6,height),4)
            break
    #checking diagonaly left to right
    if(TTT[0][0]==TTT[1][1]==TTT[2][2] and TTT[0][0] is not None):
        winner=TTT[0][0]
        pg.draw.line(Screen ,(250,70,70) ,(50,50),(550,550),4)


    #checking diagonaly right to left
    if(TTT[0][2]==TTT[1][1]==TTT[2][0] and TTT[0][2] is not None):
        winner=TTT[0][2]
        pg.draw.line(Screen ,(250,70,70) ,(550,50),(50,550),4)


    if(all([all(row) for row in TTT ]) and winner is None):
        draw=True
    draw_status()

def Graphing(row,column):
    global TTT,X0

    if row==1:
        position_X=50
    if row==2:
        position_X=width/3+50
    if row==3:
        position_X=(width/3)*2+50

    if column==1:
        position_Y=50
    if column==2:
        position_Y=height/3+50
    if column==3:
        position_Y=(height/3)*2+50

    TTT[row-1][column-1]=X0

    if X0 == 'Bugs Bunny':
        Screen.blit(bunny_image,(position_Y,position_X))
        X0='Daffy Duck'
    elif X0=='Daffy Duck':
        Screen.blit(duffy_image,(position_Y,position_X))
        X0='Bugs Bunny'
    pg.display.update()

def user_click():
    #taking coordinates of user's click
    X,Y=pg.mouse.get_pos()

    if X<width/3:
        column=1
    elif X<width/3*2:
        column=2
    elif X<width:
        column=3
    else:
        column=None

    if Y<height/3:
        row=1
    elif Y<height/3*2:
        row=2
    elif Y<height:
        row=3
    else:
        row=None

    if(row and column and TTT[row-1][column-1] is None):
        global X0
        Graphing(row,column)
        Win_Checking()

def reset():
    global TTT,X0,winner,draw
    draw=False
    X0='Bugs Bunny'
    time.sleep(3)
    opening_window()
    winner=None
    TTT=[[None]*3,[None]*3,[None]*3]

opening_window()

#running game loop forever
while True:
    for event in pg.event.get():
        if event.type== QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset()

    pg.display.update()
    clock.tick(fps)
