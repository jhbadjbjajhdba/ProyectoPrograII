import pygame
from sys import exit

pygame.init() #iniciar las partes de pygame
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Overcooked')
clock= pygame.time.Clock()

test_font=pygame.font.Font('oswald.ttf',50)
score=test_font.render('Jueguito Prueba',False,'White')#texto,smooth, color
score_rect=score.get_rect(center=(400,200))


pasto_original = pygame.image.load("pasto.jpg")
nuevo_pasto = (800, 100) 
pasto = pygame.transform.scale(pasto_original, nuevo_pasto)


cielo_original = pygame.image.load("cielo.jpg")
nuevo_tamano = (800, 300) 
cielo = pygame.transform.scale(cielo_original, nuevo_tamano)

og_azul=pygame.image.load("azul.png")
azul_tamano = (50, 50) 
amongus_azul = pygame.transform.scale(og_azul, azul_tamano)
azul_rectangulo=amongus_azul.get_rect(bottomleft=(700,310))

amongus_original = pygame.image.load("amongus.png")
nuevo_amongus = (50, 50) 
amongus = pygame.transform.scale(amongus_original, nuevo_amongus)
amongus_rectangulo=amongus.get_rect(center=(100,310))

personaje_superficie_x=0
#player_superficie=pygame.image.load('potter.jpg').convert_alpha()
#player_rectangulo=player_superficie.get_rect(midleft=(100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type==pygame.KEYDOWN:
         #   if event.key== pygame.K_SPACE:
          #      azul_rectangulo.y-=10
        #if event.type==pygame.KEDO:
         #   print ('key up')
        
    screen.fill('Black')       
    screen.blit(cielo,(0,0))#es como el place
    screen.blit(pasto,(0,300))
    screen.blit(amongus_azul,azul_rectangulo)
    screen.blit(amongus,amongus_rectangulo)
    screen.blit(score,score_rect)
    amongus_rectangulo.x+=4
    if amongus_rectangulo.x>=810:
        amongus_rectangulo.x=-10
    class Jugador:
        def __init__(self):
            pass
        def mover(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                azul_rectangulo.y-=5
            if keys[pygame.K_DOWN]:
                azul_rectangulo.y+=5
            if keys[pygame.K_LEFT]:
                azul_rectangulo.x-=5
            if keys[pygame.K_RIGHT]:
                azul_rectangulo.x+=5

        self.limitar_pantalla()     
    if azul_rectangulo.x==0:
        azul_rectangulo.x=5
    if azul_rectangulo.x==760:
        azul_rectangulo.x=755
    if azul_rectangulo.y==0:
        azul_rectangulo.y=5
    if azul_rectangulo.y==360:
        azul_rectangulo.y=355

    
        
    #if amongus_rectangulo.colliderect(azul_rectangulo):

      #  print('choque')or print('BOOM')
    #personaje_superficie_x+=1
    
    #screen.blit(player_superficie,player_rectangulo)
    #if personaje_superficie_x>850:
       # personaje_superficie_x=-50
    
    pygame.display.update()#actualiza el display
    clock.tick(60)#frames
