import pygame.draw


class Player:

    def __init__(self,color='Blue',player_number=0):
        self.color = color
        self.list = []
        self.score = 0
        self.player_number = player_number


    def draw_shape(self,surface,x,y,r):



        pygame.draw.circle(surface,self.color,(x,y),r)
        self.list.append((x, y))












