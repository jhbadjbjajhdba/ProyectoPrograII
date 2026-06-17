import pygame
from sys import exit
import tkinter as tk

class Alimento():
    def __init__(self,nombre,preparacion,estado):
        self.nombre=nombre
        self.preparacion=preparacion
        self.estado=estado
    def __str__(self):
        return self.nombre
    def get_preparacion(self):
        return self.preparacion
    def get_estado(self):
        return self.estado
        
class Proteina(Alimento):
    def __init__(self,nombre,preparacion,estado):
        super().__init__(nombre,preparacion,estado)
    def get_grupo_alimentario(self):
        return ('proteina')
 
    
class Vegetal(Alimento):
    def __init__(self,nombre,preparacion,estado):
        super().__init__(nombre,preparacion,estado)
    def get_grupo_alimentario(self):
        return ('vegetal')
    
class Estacion():
    def __init__(self,image,size,localizacion):
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.rectangulo=self.image.get_rect(bottomleft=localizacion)
    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)
    
class Mesa(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]
    def get_bandeja(self):
        if len (self.bandeja)==1:
            return self.bandeja[0]
        else:
            pass

        
class Platero(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]
    def get_bandeja(self):
        return self.bandeja

class Basurero(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]

    

class Tabla(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]
    def cocinar(self,producto):            
        lechugapartida=Vegetal('Ensalada',0,True)
        self.bandeja.append(lechugapartida)
        print ('la tabla tiene',self.bandeja[0])

class Horno(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]
    def cocinar(self,producto):            
        carnecocinada=Proteina('Bistec',0,True)
        self.bandeja.append(carnecocinada)
        print ('el horno tiene',self.bandeja[0])
    

class Despensa():
    def __init__(self,image,size,localizacion):
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.localizacion=localizacion
        self.rectangulo=self.image.get_rect(bottomleft=localizacion)
    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)
    def get_localizacion(self):
        return self.localizacion
    
class Despensa_Proteina(Despensa):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.producto=Proteina('Carne',30,False)
    def get_producto(self):
        return self.producto
    
class Despensa_Vegetales(Despensa):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.producto=Vegetal('Lechuga',20,False)
    def get_producto(self):
        return self.producto
    
        
class Jugador():
    def __init__(self,image,size, position, inventario):
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.rectangulo=self.image.get_rect(bottomleft=position)
        self.inventario=inventario

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
     
    def get_inventario(self):
        return self.inventario
    
    def coger(self,producto):
        self.inventario.append(producto)
        
    def dejar(self):
        if len(self.inventario)!=0:
            del self.inventario[0]
          
    
    def mantener_posicion(self):
        if self.rectangulo.x==35:
            self.rectangulo.x=40
        if self.rectangulo.x==715:
            self.rectangulo.x=710
        if self.rectangulo.y==20:
            self.rectangulo.y=25
        if self.rectangulo.y==315:
            self.rectangulo.y=310

    def actualizar(self):
        self.moverse()
        self.mantener_posicion()

    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)

        


class Juego():
    def __init__(self):
        pygame.init() #iniciar las partes de pygame
        self.screen=pygame.display.set_mode((810,400))
        pygame.display.set_caption('Overcooked')
        self.clock= pygame.time.Clock()
        self.cargar_imagenes()
        self.crear_jugador()
        self.lista_despensas=[]
        self.lista_mesas=[]
        self.lista_plateros=[]
        self.crear_estaciones()
        
        
    def crear_jugador(self):
        self.uno=Jugador('azul.png',(50,50),(700,310),[])
        self.dos=Jugador('amongus.png',(50,50),(100,310),[])
        self.jugador_seleccionado=self.uno
        
    def cambiar_jugador(self):
        if self.jugador_seleccionado == self.uno:
            self.jugador_seleccionado = self.dos
        else:
            self.jugador_seleccionado = self.uno

    def crear_estaciones(self):
        self.despensauno=Despensa_Proteina('mesa.png',(50,50),(100,50))
        self.lista_despensas.append(self.despensauno)
        self.despensados=Despensa_Vegetales('mesa.png',(50,50),(200,50))
        self.lista_despensas.append(self.despensados)

        self.hornouno=Horno('horno.png',(50,50),(300,50))
        self.tablauno=Tabla('horno.png',(50,50),(400,50))

        self.basurero=Basurero('basurero.png',(50,50),(500,50))
        
        for i in range (10,400,60):
            mesa=Mesa('mesa.png',(50,50),(10,i))
            self.lista_mesas.append(mesa)
            
        for x in range (60,720,75):
            mesa=Mesa('mesa.png',(50,50),(x,390))
            self.lista_mesas.append(mesa)

        for f in range (10,400,60):
            fer=Platero('mesa.png',(50,50),(735,f))
            self.lista_plateros.append(fer)
           
                
    def cargar_imagenes(self):
        
        self.font=pygame.font.Font('oswald.ttf',50)
        self.score=self.font.render('  ',False,'White')#texto,smooth, color
        self.score_rect=self.score.get_rect(center=(400,200))
        
        #pasto_original = pygame.image.load("pasto.jpg")
        #nuevo_pasto = (810, 100) 
        #self.pasto = pygame.transform.scale(pasto_original, nuevo_pasto)

        #cielo_original = pygame.image.load("cielo.jpg")
        #nuevo_tamano_cielo = (810, 300) 
        #self.cielo = pygame.transform.scale(cielo_original, nuevo_tamano_cielo)


    def permitir_eventos(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_r:
                    self.cambiar_jugador()
                    
                if event.key == pygame.K_f:
                    for i in self.lista_despensas:
                        if  self.jugador_seleccionado.rectangulo.colliderect(i.rectangulo) and len(self.jugador_seleccionado.inventario)==0:
                            producto=i.get_producto()
                            self.jugador_seleccionado.coger(producto)
                            print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())
                        
                    for j in self.lista_mesas:
                        if  self.jugador_seleccionado.rectangulo.colliderect(j.rectangulo):
                            if len(j.bandeja)==0 and len(self.jugador_seleccionado.inventario)==1:
                                j.bandeja.append(self.jugador_seleccionado.inventario[0])
                                print ('La mesa tiene: ',j.bandeja[0])
                                return self.jugador_seleccionado.dejar()
                            elif len(j.bandeja)==1 and len(self.jugador_seleccionado.inventario)==0:
                                    producto=j.get_bandeja()
                                    del (j.bandeja[0])
                                    self.jugador_seleccionado.coger(producto)
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())
                            else:
                                pass
                                    
                    for f in self.lista_plateros:
                        if  self.jugador_seleccionado.rectangulo.colliderect(f.rectangulo):
                            if  len(self.jugador_seleccionado.inventario)>=1 and self.jugador_seleccionado.inventario[0].get_estado()==True:
                                for a in self.jugador_seleccionado.inventario:
                                    f.bandeja.append(a)
                                print ('El platero tiene: ')
                                for a in f.bandeja:
                                    print ('platero',a)
                                return self.jugador_seleccionado.dejar()
                            elif len(self.jugador_seleccionado.inventario)==0 and len(f.bandeja)!=0:
                                    producto=f.get_bandeja()
                                    for q in f.bandeja:
                                        self.jugador_seleccionado.coger(q)
                                    for a in self.jugador_seleccionado.inventario:
                                        print (a)
                                    f.bandeja.clear()
                    
                    if len(self.jugador_seleccionado.inventario)==1 and len(self.hornouno.bandeja)==0:
                            if self.jugador_seleccionado.rectangulo.colliderect(self.hornouno.rectangulo):
                                if self.jugador_seleccionado.inventario[0].estado==False and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('proteina'):
                                    elemento=self.jugador_seleccionado.inventario[0]
                                    del (self.jugador_seleccionado.inventario[0])
                                    
                                    return self.hornouno.cocinar(elemento)
                       
                    elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.hornouno.bandeja)==1:
                                if  self.jugador_seleccionado.rectangulo.colliderect(self.hornouno.rectangulo):
                                    producto=self.hornouno.bandeja[0]
                                    self.jugador_seleccionado.coger(producto)
                                    del (self.hornouno.bandeja[0])
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())

                    if len(self.jugador_seleccionado.inventario)==1 and len(self.tablauno.bandeja)==0:
                            if self.jugador_seleccionado.rectangulo.colliderect(self.tablauno.rectangulo):
                                if self.jugador_seleccionado.inventario[0].estado==False and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('vegetal'):
                                    elemento=self.jugador_seleccionado.inventario[0]
                                    del (self.jugador_seleccionado.inventario[0])
                                    return self.tablauno.cocinar(elemento)
                       
                    elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                if  self.jugador_seleccionado.rectangulo.colliderect(self.tablauno.rectangulo):
                                    producto=self.tablauno.bandeja[0]
                                    self.jugador_seleccionado.coger(producto)
                                    del (self.tablauno.bandeja[0])
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())
                                
                    if len(self.jugador_seleccionado.inventario)>=1:
                            if self.jugador_seleccionado.rectangulo.colliderect(self.basurero.rectangulo):
                                    self.jugador_seleccionado.inventario.clear()
                                    print (self.jugador_seleccionado.inventario)

    def dibujar_fondo(self):
        self.screen.fill('White')       

       # self.screen.blit(self.cielo,(0,0))#es como el place
        #self.screen.blit(self.pasto,(0,300))

    def dibujar(self):
        self.dibujar_fondo()
        self.despensauno.dibujar(self.screen)
        self.despensados.dibujar(self.screen)
        self.hornouno.dibujar(self.screen)
        self.basurero.dibujar(self.screen)
        self.tablauno.dibujar(self.screen)
        for i in self.lista_mesas:
            i.dibujar(self.screen)
        for f in self.lista_plateros:
            f.dibujar(self.screen)
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


#===================================================================================================================            
class PantallaPrincipal():
    def __init__(self):
        self.window = None
    def empezar(self):
        self.window.withdraw()
        juego=Juego()
        juego.correr()
        
    def inicializar(self):
        self.window=tk.Tk()
        self.window.geometry('800x400')
        self.window.title('Undercooked')
        self.window.resizable(False,False)
        titulo=tk.Label()
        boton_iniciar=tk.Button(self.window, text='Iniciar', font=('Papyrus',12),command=self.empezar)
        titulo=tk.Label(self.window,text=('UNDERCOOKED: The Video Game'),fg='black',font=(35), compound='bottom')
        titulo.place(x=100,y=10)
        boton_iniciar.place(x=200,y=200)
        self.window.mainloop()
        
    
        
pg=PantallaPrincipal()
pg.inicializar()
