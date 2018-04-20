import pygame, random, sys
from pygame.locals import *
import numpy as np
pygame.font.init()

A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m
                
def Nbr(n, k): return A.T[n-1, k-1]

def markov_discrete_pebble(k):
        n=nran(1, 4)
        if Nbr(n, k)!=0: k=Nbr(n, k)
        return k

FPS=30
windowwidth=1000 # in pixels
windowheight=700 # in pixels
boardwidth=3 # number of columns
boardheight=3 # number of heights
boxsize=80
gapsize=10
BASICFONTSIZE=20

xmargin=int((windowwidth-(boardwidth*(boxsize + gapsize)))/2)
ymargin=int((windowheight-(boardheight*(boxsize + gapsize)))/2)

#the colors
white=(255, 255, 255)
faded_green=(51, 255, 51)
red=(255, 0, 0)
deep_green=(0, 51, 25)
blue=(0, 0, 255)
black=(0, 0, 0)

DISPLAYSURF=pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption('Markov-Pebble')
##BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)


background=white
board_color=red
border=black
circle_color=blue
textcolor=faded_green

L={7:[0, 0], 8:[0, 1], 9:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 1:[2,0], 2:[2,1], 3:[2, 2]}
clock=pygame.time.Clock()

def getBoard(): return [[0]*3, [0]*3, [0]*3]

def getLeftTopOf(boxx, boxy):
    left=boxx*(boxsize + gapsize) + xmargin
    top=boxy*(boxsize + gapsize) + ymargin
    return (left, top)

def drawBox(boxx, boxy):
    left, top=getLeftTopOf(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, board_color, (left, top, boxsize, boxsize))

def drawBoard(board):
    DISPLAYSURF.fill(background)
    
    for boxx in range(len(board)):
        for boxy in range(len(board[0])):
            drawBox(boxx, boxy)

    left, top=getLeftTopOf(0, 0)
    width=boardwidth*boxsize
    height=boardheight*boxsize
    pygame.draw.rect(DISPLAYSURF, border, (left - 5, top - 5, width + 30, height + 30), 5)

drawBoard(getBoard())
left, top=getLeftTopOf(0, 0)
pygame.draw.circle(DISPLAYSURF, circle_color, (left + boxsize/2, top + boxsize/2), 30)
k=7
throws=0

myfont=pygame.font.SysFont('Comic Sans MS', 30)
textsurface=myfont.render('Throws = '+str(throws), False, black)
DISPLAYSURF.blit(textsurface, (280, 150))
while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'Random Permutation.png')
                        pygame.quit()
                        sys.exit()
        clock.tick(2)
        drawBoard(getBoard())
        textsurface=myfont.render('Throws = '+str(throws), False, black)
        DISPLAYSURF.blit(textsurface, (440, 150))
        
        k=markov_discrete_pebble(k) # calls the main algorithm
        n=L[k]
        left, top=getLeftTopOf(n[0], n[1])
        pygame.draw.circle(DISPLAYSURF, circle_color, (left + boxsize/2, top + boxsize/2), 30)
        throws+=1
        pygame.display.update()

