import pygame
import sys
import math
fa =0
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"the rotating heart of math by rafi mahr")
total_points = 200
r = width /2-16


def get_vecter(i,r_angle):

    angle = 2 * math.pi * i / total_points + r_angle
    x = r * math.cos(angle+math.pi) + width // 2 
    y = r * math.sin(angle+math.pi) + height // 2
    v = pygame.math.Vector2(x,y)
    v*r
    return v


rotation_speed = 0.001

clock = pygame.time.Clock()
fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    color = (0,0,123)
    screen.fill((0, 0, 0))
    fa += rotation_speed
    circle = pygame.draw.circle(screen,(255,255,255),(width/2,height/2),width//2-16,1)

    for i in range(total_points):
        angle = get_vecter(i,0)
    for i in range(total_points):
        a = get_vecter(i,0)
        b = get_vecter(i*fa,rotation_speed)
        
        pygame.draw.aalines(screen,color,False,(a,b),1)
        
    
    
    
    pygame.display.flip()
    

clock.tick(fps)

pygame.quit()
sys.exit()

