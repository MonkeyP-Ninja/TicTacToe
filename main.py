import pygame
from sys import exit
from Player import Player
import math
from collections import Counter
from button import Button

pygame.init()

width, height = 1280, 900
cwidth, cheight= 1280,720
font = pygame.font.SysFont("Arial", 20)
game = False
button = Button(
    "Click here",
    (500, 800),
    font=30,
    bg="navy",
    feedback="You clicked me")

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic TAC Toe')
clock = pygame.time.Clock()
surface=pygame.Surface((1280, 720))
menu=pygame.Surface((cwidth,height-cheight))

surface.fill('Black')
menu.fill('Green')


mx, my = 0, 0
player1 = Player()
player2 = Player('Green',1)


def __init__(self):
    game=False


def draw_game():
    for i in range(3):
        pygame.draw.line(surface, 'White', (cwidth / 3 * (i + 1), 0), (cwidth / 3 * (i + 1), cheight), 6)
        pygame.draw.line(surface, 'White', (0, cheight / 3 * (i + 1)), (cwidth, cheight / 3 * (i + 1)), 6)


def search_field(width, height, mx, my):
    points=[]
    delta_List=[]

    for i in range(3):
        for u in range(3):
            x=width/3 *(u+1)-width/6
            y=height/3*(i+1)-height/6


            points.append((x,y))

    for p in range(9):
        delta=math.sqrt(math.pow((points[p][0]-mx),2)+math.pow((points[p][1]-my),2))
        delta_List.append(delta)

    index=delta_List.index(min(delta_List))

    return points[index]


draw_game()


def draw(cx,cy,r):
    draw= True
    if len(player1.list)==0:
        player1.draw_shape(surface,cx,cy,r)

    if  len(player1.list)>len(player2.list):
        for i in player1.list:
            if i[0]==cx and i[1] == cy:
                draw= False

        if draw:
            player2.draw_shape(surface,cx,cy,r)
        else:
            print('choose other field')

    else:
        for i in player2.list:

            if i[0]==cx and i[1] == cy:
                draw= False

        if draw:
            player1.draw_shape(surface,cx,cy,r)
        else:
            print('choose other field')


def if_won():
    x_list=[]
    y_list=[]
    x_list2 = []
    y_list2 = []
    for i in player1.list:
        x_list.append(i[0])
        y_list.append(i[1])


    if len(player2.list)!=0:
        for i in player2.list:
            x_list2.append(i[0])
            y_list2.append(i[1])
            count_x2 = Counter(x_list2).most_common(1)
            count_y2 = Counter(y_list2).most_common(1)
            if count_x2[0][1] == 3 or count_y2[0][1] == 3:
                print('Won')
                player1.score = player1.score + 1

    count_x=Counter(x_list).most_common(1)
    count_y=Counter(y_list).most_common(1)

    if count_x[0][1]==3 or count_y[0][1]==3:
        print('Won')
        player2.score=player2.score+1


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT :
            pygame.quit()

            exit()

        if button.click(event):
            game=True

        if game:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3)[0]:
                        if pygame.mouse.get_pos()[0] <= width and pygame.mouse.get_pos()[1] <= cheight:
                            mx, my = pygame.mouse.get_pos()
                            cx, cy = search_field(cwidth, cheight, mx, my)
                            draw(cx, cy, 100)
                            if_won()




    screen.blit(surface,(0,0))
    screen.blit(menu, (0,cheight))
    button.show(screen)
    pygame.display.update()
    clock.tick(60)






