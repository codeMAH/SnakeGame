import random
import sys,time,os
import pygame
pygame.init()

#colours
white= (255, 255, 255)
red= (255, 0, 0)
black= (0,0,0)
green= (34,139,34)
#dimension
screen_width= 900
screen_height= 600

#window creation
gameWindow= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game v[@sif]")
pygame.display.update()

#time setting
clock= pygame.time.Clock()
#display setting
font= pygame.font.SysFont(None, 50)
def scr_disp(text, colour, x,y):
    disp_text= font.render(text, True, colour)
    gameWindow.blit(disp_text, [x,y])
w= pygame.font.SysFont(None,35, italic=2)
def watermark(text, colour, x,y):
    mark=w.render(text, True, colour)
    gameWindow.blit(mark, [x,y])

def plot_s(gameWindow, colour, sli, sn_size):
    for x,y in sli:
        pygame.draw.rect(gameWindow, colour, [x,y,sn_size,sn_size])


#welcome screen
def welcome():

    exit_game=False
    while not exit_game:
        gameWindow.fill(black)
        scr_disp("Welcome to the Game", red, 250, 250)
        watermark("Press enter key to play", white, 300, 320)
        time.sleep(0.1)
        scr_disp(">-----game by @sif-----<", green, 250, 500)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

#game loop starts
def gameloop():
#game specific variables
    exit_game= False
    game_over= False
    sn_x= 45
    sn_y= 55
    sn_size= 10
    vx= 0
    vy= 0
    fps= 30
    fx= random.randint(20, screen_width/2)
    fy= random.randint(20, screen_height/2)
    scr=0
    inv= 5
    sli= []
    sln=1

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            scr_disp("GAME OVER! Press enter to continue", red, screen_height/5, screen_width/4)
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game= True
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        gameloop()
        #key functions
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game= True

                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT:
                        vx= inv
                        vy=0
                    if event.key== pygame.K_LEFT:
                        vx= -inv
                        vy=0
                    if event.key== pygame.K_UP:
                        vy= -inv
                        vx=0
                    if event.key== pygame.K_DOWN:
                        vy= inv
                        vx=0
            sn_x= sn_x+vx
            sn_y= sn_y+vy
            #score increment & display
            if abs(sn_x-fx)<6 and abs(sn_y-fy)<6:
                scr+= 1  ##not required
                print("SCORE: ",scr)  ##not required
                fx= random.randint(20, screen_width/2)
                fy = random.randint(20, screen_height / 2)
                sln+=2
            gameWindow.fill(white)
            scr_disp("Score: " + str(scr * 10), red, 5, 5)
            #creating food
            pygame.draw.rect(gameWindow, red, [fx, fy, sn_size, sn_size])
            #snake animate
            head= []
            head.append(sn_x)
            head.append(sn_y)
            sli.append(head)
            if len(sli)>sln:
                del sli[0]

            #collision
            if head in sli[:-1]:
                game_over=True
            if sn_x<0 or sn_x>screen_width or sn_y<0 or sn_y>screen_height:
                game_over= True
                #print("Game Over")

            plot_s(gameWindow, black, sli, sn_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()