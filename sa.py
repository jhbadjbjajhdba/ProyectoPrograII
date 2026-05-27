import pygame
from sys import exit


pygame.init() #iniciar las partes de pygame


screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Overcooked')
clock= pygame.time.Clock()

test_fot=pygame.font.Font('oswald.ttf',50)

test_surface=pygame.Surface((100,200))

test_surface.fill('Blue')

test_surface_2=pygame.image.load('ladrllos.jpg').convert_alpha()

text_surface=test_fot.render('Overcooked',False,'White')#texto,smooth, color

personaje_superficie=pygame.image.load('luigi.png').convert_alpha()
personaje_superficie_x=0
player_superficie=pygame.image.load('potter.jpg').convert_alpha()
player_rectangulo=player_superficie.get_rect(midleft=(100,300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('Black')       
    screen.blit(test_surface,(200,100))
    screen.blit(test_surface_2,(200,100))#es como el place
    screen.blit(text_surface,(300,100))
    personaje_superficie_x+=1
    
    screen.blit(player_superficie,player_rectangulo)
    if personaje_superficie_x>850:
        personaje_superficie_x=-50
    
    pygame.display.update()#actualiza el display
    clock.tick(60)#frames
