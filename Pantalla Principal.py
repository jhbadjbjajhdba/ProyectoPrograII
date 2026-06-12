import pygame
from sys import exit

class Jugador():
    def __init__(self,image,size, position):
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.rectangulo=self.image.get_rect(bottomleft=position)
        

    def moverse(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rectangulo.y-=5
        if keys[pygame.K_DOWN]:
            self.rectangulo.y+=5
        if keys[pygame.K_LEFT]:
            self.rectangulo.x-=5
        if keys[pygame.K_RIGHT]:
            self.rectangulo.x+=5
            
    def mantener_posicion(self):
        if self.rectangulo.x==0:
            self.rectangulo.x=5
        if self.rectangulo.x==760:
            self.rectangulo.x=755
        if self.rectangulo.y==0:
            self.rectangulo.y=5
        if self.rectangulo.y==360:
            self.rectangulo.y=355

    def actualizar(self):
        self.moverse()
        self.mantener_posicion()

    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)

        


class Juego():
    def __init__(self):
        pygame.init() #iniciar las partes de pygame
        self.screen=pygame.display.set_mode((800,400))
        pygame.display.set_caption('Overcooked')
        self.clock= pygame.time.Clock()
        self.cargar_imagenes()
        self.crear_jugador()
        
    def crear_jugador(self):
        self.uno=Jugador('azul.png',(50,50),(700,310))
        self.dos=Jugador('amongus.png',(50,50),(100,310))
        self.jugador_seleccionado=self.uno
        
    def cambiar_jugador(self):
        if self.jugador_seleccionado == self.uno:
            self.jugador_seleccionado = self.dos
        else:
            self.jugador_seleccionado = self.uno
            
            
           
                
    def cargar_imagenes(self):
        
        self.font=pygame.font.Font('oswald.ttf',50)
        self.score=self.font.render('Jueguito Prueba',False,'White')#texto,smooth, color
        self.score_rect=self.score.get_rect(center=(400,200))


        pasto_original = pygame.image.load("pasto.jpg")
        nuevo_pasto = (800, 100) 
        self.pasto = pygame.transform.scale(pasto_original, nuevo_pasto)


        cielo_original = pygame.image.load("cielo.jpg")
        nuevo_tamano_cielo = (800, 300) 
        self.cielo = pygame.transform.scale(cielo_original, nuevo_tamano_cielo)

#og_azul=pygame.image.load("azul.png")
#azul_tamano = (50, 50) 
#amongus_azul = pygame.transform.scale(og_azul, azul_tamano)
#self.rectangulo=amongus_azul.get_rect(bottomleft=(700,310))

#amongus_original = pygame.image.load("amongus.png")
#nuevo_amongus = (50, 50) 
#amongus = pygame.transform.scale(amongus_original, nuevo_amongus)
#amongus_rectangulo=amongus.get_rect(center=(100,310))

#personaje_superficie_x=0

    def permitir_eventos(self):
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.cambiar_jugador()
        #if event.type==pygame.KEYDOWN:
         #   if event.key== pygame.K_SPACE:
          #      self.rectangulo.y-=10
        #if event.type==pygame.KEDO:
         #   print ('key up')
    def dibujar_fondo(self):
        
        
        self.screen.fill('Black')       
        self.screen.blit(self.cielo,(0,0))#es como el place
        self.screen.blit(self.pasto,(0,300))

    def dibujar(self):
        self.dibujar_fondo()
        self.uno.dibujar(self.screen)
        self.dos.dibujar(self.screen)
        self.screen.blit(self.score, self.score_rect)

    def actualizar(self):
        self.jugador_seleccionado.actualizar()

    def correr(self):
        while True:
            self.permitir_eventos()
            self.actualizar()
            self.dibujar()
           
            pygame.display.update()#actualiza el display
            self.clock.tick(60)#frames

juego=Juego()
juego.correr()
        
        
        
  
