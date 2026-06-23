import pygame
from sys import exit
import tkinter as tk
import random
class Receta():
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    def mostrar_receta(self):
        print("Receta generada:")
        for ingrediente, cantidad in self.ingredientes.items():
            print(ingrediente, "x", cantidad)
        
        
class Temporizador():
    def __init__(self,duracion):
        self.tiempo_inicio=0
        self.duracion=duracion
        self.activo = False
    def get_tiempo_actual(self):
        tiempo_actual =pygame.time.get_ticks()
        return tiempo_actual
    def iniciar(self):
        self.tiempo_inicio=pygame.time.get_ticks()
        self.activo = True
    def terminar(self):
        if self.activo:
            tiempo_actual =pygame.time.get_ticks()
            if tiempo_actual-self.tiempo_inicio>=self.duracion:
                self.activo = False
                return True
        return False
        
    def mostrar_tiempo(self):
        if self.activo==True:
            tiempo_actual=pygame.time.get_ticks()
            tiempo_pasado= tiempo_actual-self.tiempo_inicio
            restante=self.duracion-tiempo_pasado
            if restante<0:
                restante=0
            return restante//1000
    def esta_activo(self):
        return self.activo

    
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
    def get_nombre(self):
        return self.nombre
        
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
class Entrega(Estacion):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
    
    
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
        self.temporizador=Temporizador(0)
        self.producto_a_cocinar=None
        
    def cocinar(self,producto):
        if len(self.bandeja) == 0 and self.producto_a_cocinar == None:
            self.producto_a_cocinar = producto
            self.temporizador = Temporizador(producto.get_preparacion())
            self.temporizador.iniciar()
            print("Preparando lechuga...")
    def actualizar(self):
        if self.temporizador.terminar():
            lechugapartida= Vegetal("Ensalada", 0, True)
            self.bandeja.append(lechugapartida)
            self.producto_a_cocinar = None
            print("La tabla tiene:", self.bandeja[0])
            
    def get_tiempo_restante(self):
        return self.temporizador.mostrar_tiempo()

    def esta_cocinando(self):
        return self.temporizador.esta_activo()

class Horno(Estacion):
    
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.bandeja=[]
        self.temporizador=Temporizador(0)
        self.producto_a_cocinar=None
        
    def cocinar(self,producto):
        if len(self.bandeja) == 0 and self.producto_a_cocinar == None:
            self.producto_a_cocinar = producto
            self.temporizador = Temporizador(producto.get_preparacion())
            self.temporizador.iniciar()
            print("Cocinando carne...")
    def actualizar(self):
        if self.temporizador.terminar():
            carnecocinada = Proteina("Bistec", 0, True)
            self.bandeja.append(carnecocinada)
            self.producto_a_cocinar = None
            print("El horno tiene:", self.bandeja[0])
            
    def get_tiempo_restante(self):
        return self.temporizador.mostrar_tiempo()

    def esta_cocinando(self):
        return self.temporizador.esta_activo()
    


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
        self.producto=Proteina('Carne',5000,False)
    def get_producto(self):
        return self.producto
    
class Despensa_Vegetales(Despensa):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.producto=Vegetal('Lechuga',5000,False)
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
            self.inventario.clear()
          
    
    def mantener_posicion(self):
        if self.rectangulo.x==35:
            self.rectangulo.x=40
        if self.rectangulo.x==715:
            self.rectangulo.x=710
        if self.rectangulo.y==20:
            self.rectangulo.y=25
        if self.rectangulo.y==320:
            self.rectangulo.y=315

    def actualizar(self):
        self.moverse()
        self.mantener_posicion()

    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)

        


class Juego():
    def __init__(self):
        pygame.init() #iniciar las partes de pygame
        self.screen=pygame.display.set_mode((900,400))
        pygame.display.set_caption('Overcooked')
        self.clock= pygame.time.Clock()
        self.fuente=pygame.font.SysFont('oswald',22)
        self.cargar_imagenes()
        self.crear_jugador()
        self.lista_despensas=[]
        self.lista_mesas=[]
        self.lista_plateros=[]
        self.lista_ingredientes_listos=[]
        self.crear_estaciones()
        self.lista_recetas=[]
        self.puntaje=0
        self.generar_receta()
        self.temporizador=Temporizador(100000)
        self.temporizador.iniciar()
        self.temporizador_receta = Temporizador(25000)
        self.temporizador_receta.iniciar()
        self.permitir=True
        
    def crear_jugador(self):
        self.uno=Jugador('uno.png',(60,60),(700,310),[])
        self.dos=Jugador('dos.png',(60,60),(100,310),[])
        self.jugador_seleccionado=self.uno
    
        
    def cambiar_jugador(self):
        if self.jugador_seleccionado == self.uno:
            self.jugador_seleccionado = self.dos
        else:
            self.jugador_seleccionado = self.uno
            
    def contar_inventario(self):
        conteo = {}
        for producto in self.jugador_seleccionado.inventario:
            nombre = producto.get_nombre()
            if nombre not in conteo:
                conteo[nombre] = 1
            else:
                conteo[nombre] += 1
        return conteo
    
    def entregar_pedido(self):
        inventario_contado = self.contar_inventario()

        if inventario_contado == self.receta_actual.ingredientes:
            print("Pedido correcto")
            self.puntaje += 10
            print("Puntaje:", self.puntaje)
            self.jugador_seleccionado.inventario.clear()
            self.generar_receta()
            self.temporizador_receta = Temporizador(25000)
            self.temporizador_receta.iniciar()
        else:
            self.puntaje-=10
            self.jugador_seleccionado.inventario.clear()
            
    def generar_receta(self):
        ingredientes_posibles = ["Bistec", "Ensalada"]
        receta = {}
        for ingrediente in ingredientes_posibles:
            cantidad = random.randint(0, 2)
            if cantidad > 0:
                receta[ingrediente] = cantidad
        if len(receta) == 0:
            ingrediente = random.choice(ingredientes_posibles)
            receta[ingrediente] = 1

        self.receta_actual = Receta(receta)
        self.lista_recetas.append(self.receta_actual)
        self.receta_actual.mostrar_receta()
        
    
    def crear_estaciones(self):
        self.despensauno=Despensa_Proteina('carne_despensa.png',(50,50),(100,50))
        self.lista_despensas.append(self.despensauno)
        self.despensados=Despensa_Vegetales('lechuga_despensa.png',(50,50),(200,50))
        self.lista_despensas.append(self.despensados)

        self.hornouno=Horno('horno.jpeg',(50,50),(300,50))
        self.tablauno=Tabla('cortadora.png',(50,50),(400,50))

        self.basurero=Basurero('basurero.png',(50,50),(500,50))

        self.entrega=Entrega('banda.png',(50,50),(600,50))
        
        for i in range (60,400,60):
            mesa=Mesa('mesa_trasera.jpeg',(50,50),(10,i))
            self.lista_mesas.append(mesa)
            
        for x in range (70,720,75):
            mesa=Mesa('mesa_trasera.jpeg',(50,50),(x,400))
            self.lista_mesas.append(mesa)

        for f in range (60,400,60):
            fer=Platero('platero.jpeg',(50,50),(735,f))
            self.lista_plateros.append(fer)
               
    def cargar_imagenes(self):
        self.font=pygame.font.Font('oswald.ttf',50)
        self.score=self.font.render('  ',False,'White')#texto,smooth, color
        cielo_original = pygame.image.load("cielo.png")
        nuevo_tamano_cielo = (800, 400)
        self.cielo = pygame.transform.scale(cielo_original, nuevo_tamano_cielo)
        self.score_rect=self.score.get_rect(center=(400,200))

    def permitir_eventos(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.permitir=False
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
                            if  len(self.jugador_seleccionado.inventario)>=1:
                                todos_true=True
                                for a in self.jugador_seleccionado.inventario:
                                    if a.get_estado()==False:
                                        todos_true=False
                                if todos_true:
                                    for a in self.jugador_seleccionado.inventario:
                                        f.bandeja.append(a)
                                print ('El platero tiene: ')
                                for a in f.bandeja:
                                    print ('platero',a)
                                self.jugador_seleccionado.inventario.clear()
                                return
                            
                            elif len(self.jugador_seleccionado.inventario)==0 and len(f.bandeja)!=0:
                                    for q in f.bandeja:
                                        self.jugador_seleccionado.coger(q)
                                    f.bandeja.clear()
                                    for a in self.jugador_seleccionado.inventario:
                                        print (a)
                                    
                                    
                    
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

                    if len(self.jugador_seleccionado.inventario) >= 1:
                        if self.jugador_seleccionado.rectangulo.colliderect(self.entrega.rectangulo):
                            self.entregar_pedido()
                            return
                                   
                                
                    elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                if  self.jugador_seleccionado.rectangulo.colliderect(self.tablauno.rectangulo):
                                    producto=self.tablauno.bandeja[0]
                                    self.jugador_seleccionado.coger(producto)
                                    del (self.tablauno.bandeja[0])
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())

    def dibujar_fondo(self):
        self.screen.fill('Grey')       
        self.screen.blit(self.cielo,(0,0))#es como el place
    def dibujar(self):
        self.dibujar_fondo()
        self.despensauno.dibujar(self.screen)
        self.despensados.dibujar(self.screen)
        self.hornouno.dibujar(self.screen)
        self.basurero.dibujar(self.screen)
        self.tablauno.dibujar(self.screen)
        self.entrega.dibujar(self.screen)
        for i in self.lista_mesas:
            i.dibujar(self.screen)
        for f in self.lista_plateros:
            f.dibujar(self.screen)
        
        tiempo = self.temporizador.mostrar_tiempo()
        texto_tiempo = self.fuente.render(f"Tiempo: {tiempo}", False, "Black")
        self.screen.blit(texto_tiempo, (810, 20))
        if self.hornouno.esta_cocinando():
            self.hornodos=Horno('horno_2.jpeg',(50,50),(300,50))
            self.hornodos.dibujar(self.screen)
            tiempo_horno = self.hornouno.get_tiempo_restante()
            texto_horno = self.fuente.render(f"Horno: {tiempo_horno}", False, "Black")
            self.screen.blit(texto_horno, (300, 60))
        if self.tablauno.esta_cocinando():
            tiempo_tabla = self.tablauno.get_tiempo_restante()
            texto_tabla = self.fuente.render(f"Tabla: {tiempo_tabla}", False, "Black")
            self.screen.blit(texto_tabla, (400, 60))
        self.uno.dibujar(self.screen)
        self.dos.dibujar(self.screen)
        
        y = 80
        titulo = self.fuente.render("Receta:", False, "Black")
        self.screen.blit(titulo, (810, y))

        y += 25

        for ingrediente, cantidad in self.receta_actual.ingredientes.items():
            texto = self.fuente.render(f"{ingrediente} x{cantidad}", False, "Black")
            self.screen.blit(texto, (810, y))
            y += 25
        puntos = self.puntaje
        texto_puntos = self.fuente.render(f"Puntos: {puntos}", False, "Black")
        self.screen.blit(texto_puntos, (810, 300))
        tiempo_receta = self.temporizador_receta.mostrar_tiempo()
        texto_tiempo_receta = self.fuente.render(f'Cambio: {tiempo_receta}',True , "Black")
        self.screen.blit(texto_tiempo_receta, (805, y))
        self.screen.blit(self.score, self.score_rect)
        

    def actualizar(self):
        self.jugador_seleccionado.actualizar()
        self.hornouno.actualizar()
        self.tablauno.actualizar()
        if self.temporizador_receta.terminar():
            self.generar_receta()
            self.temporizador_receta.iniciar()
        
        if self.temporizador.terminar():
            self.permitir = False
            

    def correr(self):
        
        while self.permitir:
            self.permitir_eventos()
            self.actualizar()
            self.dibujar()
            pygame.display.update()#actualiza el display
            self.clock.tick(60)#frames
        pygame.display.quit()
            
    
        
    
    


          
