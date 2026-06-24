import pygame
from sys import exit
import tkinter as tk
import random
#___________________________________________________________________________________
class Receta():
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    def mostrar_receta(self):
        print("Receta generada:")
        for ingrediente, cantidad in self.ingredientes.items():
            print(ingrediente, "x", cantidad)
        
#________________________________________________________________________________________________       
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

#__________________________________________________________________________________________________________
    
class Alimento():
    def __init__(self,nombre,preparacion,image,size,localizacion):
        self.nombre=nombre
        self.preparacion=preparacion
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.localizacion=localizacion
        self.rectangulo=self.image.get_rect(bottomleft=localizacion)
        
    def __str__(self):
        return self.nombre
    def get_preparacion(self):
        return self.preparacion
    def get_estado(self):
        return self.estado
    def get_nombre(self):
        return self.nombre
    def dibujar(self, screen):
        screen.blit(self.image, self.rectangulo)
        
class Proteina(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('proteina')
    def get_estado(self):
        return False   
 
class Vegetal(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('vegetal')
    def get_estado(self):
        return False

class Papas_Cortadas(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('vegetal')
    def get_estado(self):
        return ('Semilisto')

class Papas_Fritas(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('vegetal')
    def get_estado(self):
        return True

class Pescado(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('proteina')
    def get_estado(self):
        return ('Semilisto')
    
class Pescado_Empanizado(Alimento):
    def __init__(self,nombre,preparacion,image,size,localizacion ):
        super().__init__(nombre,preparacion,image,size,localizacion )
    def get_grupo_alimentario(self):
        return ('proteina')
    def get_estado(self):
        return True


#_________________________________________________________________________________________
    
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

class Tabla_vegetales(Estacion):
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
            print("preparando ingrediente...")
    def actualizar(self):
        if self.temporizador.terminar():
            papas_tiras = Papas_Cortadas('Papas cortadas', 5000,'papa_cortada.png',(30,30),(350,50))
            self.bandeja.append(papas_tiras)
            self.producto_a_cocinar = None
            print("La tabla tiene:", self.bandeja[0])
            
    def get_tiempo_restante(self):
        return self.temporizador.mostrar_tiempo()

    def esta_cocinando(self):
        return self.temporizador.esta_activo()

    
class Tabla_pescado(Estacion):
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
            print("preparando ingrediente...")
    def actualizar(self):
        if self.temporizador.terminar():
            pescado_machacado = Pescado('Pescado', 5000,'pezcado_cortado.png',(30,30),(410,50))
            self.bandeja.append(pescado_machacado)
            self.producto_a_cocinar = None
            print("La tabla tiene:", self.bandeja[0])
            
    def get_tiempo_restante(self):
        return self.temporizador.mostrar_tiempo()

    def esta_cocinando(self):
        return self.temporizador.esta_activo()

class Freidora_Pescado(Estacion):
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
            print("Friendo")
    def actualizar(self):
    
        if self.temporizador.terminar():
            pescado= Pescado_Empanizado('Pescado Empanizado', 0,'frito.png',(30,30),(280,50))
            self.bandeja.append(pescado)
            self.producto_a_cocinar = None
            print("La freidora de pescado tiene:", self.bandeja[0])
            
    def get_tiempo_restante(self):
        return self.temporizador.mostrar_tiempo()

    def esta_cocinando(self):
        return self.temporizador.esta_activo()
    
class Freidora_Papas(Estacion):
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
            print("Friendo")
    def actualizar(self):
    
        if self.temporizador.terminar():
            fritas= Papas_Fritas('Papas Fritas', 0,'papas_fritas.png',(30,30),(200,50) )
            self.bandeja.append(fritas)
            self.producto_a_cocinar = None
            print("La freidora de papas tiene:", self.bandeja[0])
            
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
    
class Despensa_Pez(Despensa):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.producto=Proteina('Pez',5000,'pezcado.png',(30,30),(100,50) )
    def get_producto(self):
        return self.producto
    
class Despensa_Papa(Despensa):
    def __init__(self,image,size,localizacion):
        super().__init__(image,size,localizacion)
        self.producto=Vegetal('Papas',5000,'papa.png',(30,30),(10,240) )
    def get_producto(self):
        return self.producto
    

#____________________________________________________________________________________________________________        
class Jugador():
    def __init__(self,image,size, position, inventario):
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.rectangulo=self.image.get_rect(bottomleft=position)
        self.inventario=inventario
    
    def dibujar_inventario(self, screen):
        if len(self.inventario) > 0:
            alimento = self.inventario[0]
            alimento.rectangulo.midtop = self.rectangulo.midbottom
            alimento.rectangulo.y -= 35
            alimento.dibujar(screen)
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

class Jugador_alpha(Jugador):
    def __init__(self,image,size, position, inventario):
        super().__init__(image,size, position, inventario)
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

                
class Jugador_betha(Jugador):
    def __init__(self,image,size, position, inventario):
        super().__init__(image,size, position, inventario)
        original=pygame.image.load(image)
        self.image= pygame.transform.scale(original, size)
        self.rectangulo=self.image.get_rect(bottomleft=position)
        self.inventario=inventario
    def moverse(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rectangulo.y-=5
        if keys[pygame.K_s]:
            self.rectangulo.y+=5
        if keys[pygame.K_a]:
            self.rectangulo.x-=5
        if keys[pygame.K_d]:
            self.rectangulo.x+=5


        


class Juego():
    def __init__(self):
        pygame.init() #iniciar las partes de pygame
        self.screen=pygame.display.set_mode((1050,400))
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
        self.uno_alpha=Jugador_alpha('uno_uno.png',(60,60),(700,310),[])
        self.dos_alpha=Jugador_alpha('uno_uno.png',(60,60),(100,310),[])
        self.uno_betha=Jugador_betha('dos_uno.png',(60,60),(500,310),[])
        self.dos_betha=Jugador_betha('dos_uno.png',(60,60),(670,45),[])
        self.jugador_seleccionado=self.uno_alpha
        self.jugador_escogido=self.uno_betha
    
        
    def cambiar_jugador_alpha(self):
        if self.jugador_seleccionado == self.uno_alpha:
            self.jugador_seleccionado = self.dos_alpha
        else:
            self.jugador_seleccionado = self.uno_alpha

    def cambiar_jugador_betha(self):
        if self.jugador_escogido == self.uno_betha:
            self.jugador_escogido = self.dos_betha
        else:
            self.jugador_escogido = self.uno_betha
            
    def contar_inventario(self,jugador):
        conteo = {}
        for producto in jugador.inventario:
            nombre = producto.get_nombre()
            if nombre not in conteo:
                conteo[nombre] = 1
            else:
                conteo[nombre] += 1
        return conteo
    
    def entregar_pedido(self,jugador):
        inventario_contado = self.contar_inventario(jugador)

        if inventario_contado == self.receta_actual.ingredientes:
            print("Pedido correcto")
            for i in inventario_contado:
                self.puntaje+=10
            print("Puntaje:", self.puntaje)
            jugador.inventario.clear()
            self.generar_receta()
            self.temporizador_receta = Temporizador(25000)
            self.temporizador_receta.iniciar()
            
        else:
            self.puntaje-=10
            jugador.inventario.clear()
    def generar_receta(self):
        ingredientes_posibles = ["Pescado Empanizado", "Papas Fritas"]
        receta = {}
        for ingrediente in ingredientes_posibles:
            cantidad = random.randint(0, 1)
            if cantidad > 0:
                receta[ingrediente] = cantidad
        if len(receta) == 0:
            ingrediente = random.choice(ingredientes_posibles)
            receta[ingrediente] = 1

        self.receta_actual = Receta(receta)
        self.lista_recetas.append(self.receta_actual)
        self.receta_actual.mostrar_receta()
        
    
    def crear_estaciones(self):
        self.despensauno=Despensa_Pez('pezcado_despensa.png',(50,50),(100,50))
        self.lista_despensas.append(self.despensauno)
        self.despensados=Despensa_Papa('papas_despensa.png',(50,50),(10,240))
        self.lista_despensas.append(self.despensados)

        self.hornouno=Freidora_Pescado('freidora_pez.png',(50,50),(280,50))
        self.hornodos=Freidora_Papas('freidora_papa.png',(50,50),(200,50))
        
        self.tablauno=Tabla_vegetales('tabla_papa.png',(50,50),(350,50))
        self.tablados=Tabla_pescado('tabla_pescado.png',(50,50),(420,50))

        self.basurero=Basurero('basurero.png',(50,50),(500,50))

        self.entrega=Entrega('banda_3.png',(50,80),(600,60))
        
        for i in range (60,200,80):
            mesa=Mesa('mesa_trasera_tres.jpeg',(50,50),(10,i))
            self.lista_mesas.append(mesa)
        for i in range (300,400,80):
            mesa=Mesa('mesa_trasera_tres.jpeg',(50,50),(10,i))
            self.lista_mesas.append(mesa)
            
        for x in range (70,720,90):
            mesa=Mesa('mesa_trasera_tres.jpeg',(50,50),(x,400))
            self.lista_mesas.append(mesa)

        for f in range (60,400,90):
            fer=Platero('platero_tres.jpeg',(50,50),(735,f))
            self.lista_plateros.append(fer)
               
    def cargar_imagenes(self):
        self.font=pygame.font.Font('oswald.ttf',50)
        self.score=self.font.render('  ',False,'White')#texto,smooth, color
        cielo_original = pygame.image.load("cielo_tres.png")
        nuevo_tamano_cielo = (800, 400)
        self.cielo = pygame.transform.scale(cielo_original, nuevo_tamano_cielo)
        self.score_rect=self.score.get_rect(center=(400,200))

    def permitir_eventos(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.permitir=False
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_u:
                    self.cambiar_jugador_alpha()

                
            
                if event.key == pygame.K_r:
                    self.cambiar_jugador_betha()
                    
                    
                if event.key == pygame.K_j:
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
                                    
                    if self.jugador_seleccionado.rectangulo.colliderect(self.hornouno.rectangulo):            
                            if len(self.jugador_seleccionado.inventario)==1 and len(self.hornouno.bandeja)==0:
                                if self.jugador_seleccionado.inventario[0].get_estado()==('Semilisto') and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('proteina'):
                                    elemento=self.jugador_seleccionado.inventario[0]
                                    del (self.jugador_seleccionado.inventario[0])
                                    return self.hornouno.cocinar(elemento)
                       
                            elif len(self.jugador_seleccionado.inventario)==0:
                                if len(self.hornouno.bandeja)==1:
                                    
                                        producto=self.hornouno.bandeja[0]
                                        self.jugador_seleccionado.coger(producto)
                                        del (self.hornouno.bandeja[0])
                                        print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())

                    elif self.jugador_seleccionado.rectangulo.colliderect(self.hornodos.rectangulo):            
                            if len(self.jugador_seleccionado.inventario)==1 and len(self.hornodos.bandeja)==0:
                            
                                if self.jugador_seleccionado.inventario[0].get_estado()==('Semilisto') and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('vegetal'):
                                    elemento=self.jugador_seleccionado.inventario[0]
                                    del (self.jugador_seleccionado.inventario[0])
                                    return self.hornodos.cocinar(elemento)
                       
                            elif len(self.jugador_seleccionado.inventario)==0:
                                if len(self.hornodos.bandeja)==1:
                                    
                                        producto=self.hornodos.bandeja[0]
                                        self.jugador_seleccionado.coger(producto)
                                        del (self.hornodos.bandeja[0])
                                        print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())







                    if self.jugador_seleccionado.rectangulo.colliderect(self.tablauno.rectangulo):
                        if len(self.jugador_seleccionado.inventario)==1 and len(self.tablauno.bandeja)==0:
                            if self.jugador_seleccionado.inventario[0].get_estado()==False and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('vegetal'):
                                elemento=self.jugador_seleccionado.inventario[0]
                                del (self.jugador_seleccionado.inventario[0])
                                return self.tablauno.cocinar(elemento)
                       
                        elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                producto=self.tablauno.bandeja[0]
                                self.jugador_seleccionado.coger(producto)
                                del (self.tablauno.bandeja[0])
                                print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())




                    if self.jugador_seleccionado.rectangulo.colliderect(self.tablados.rectangulo):
                        if len(self.jugador_seleccionado.inventario)==1 and len(self.tablados.bandeja)==0:
                            if self.jugador_seleccionado.inventario[0].get_estado()==False and self.jugador_seleccionado.inventario[0].get_grupo_alimentario()==('proteina'):
                                elemento=self.jugador_seleccionado.inventario[0]
                                del (self.jugador_seleccionado.inventario[0])
                                return self.tablados.cocinar(elemento)
                       
                        elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.tablados.bandeja)==1:
                                    producto=self.tablados.bandeja[0]
                                    self.jugador_seleccionado.coger(producto)
                                    del (self.tablados.bandeja[0])
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())






                                
                    if len(self.jugador_seleccionado.inventario)>=1:
                            if self.jugador_seleccionado.rectangulo.colliderect(self.basurero.rectangulo):
                                    self.jugador_seleccionado.inventario.clear()
                                    print (self.jugador_seleccionado.inventario)

                    if len(self.jugador_seleccionado.inventario) >= 1:
                        if self.jugador_seleccionado.rectangulo.colliderect(self.entrega.rectangulo):
                            self.entregar_pedido(self.jugador_seleccionado)
                            return
                                   
                                
                    elif len(self.jugador_seleccionado.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                if  self.jugador_seleccionado.rectangulo.colliderect(self.tablauno.rectangulo):
                                    producto=self.tablauno.bandeja[0]
                                    self.jugador_seleccionado.coger(producto)
                                    del (self.tablauno.bandeja[0])
                                    print (self.jugador_seleccionado.inventario[0],self.jugador_seleccionado.inventario[0].get_estado())
#======================================================================================================================================================
                if event.key == pygame.K_f:
                    for i in self.lista_despensas:
                        if  self.jugador_escogido.rectangulo.colliderect(i.rectangulo) and len(self.jugador_escogido.inventario)==0:
                            producto=i.get_producto()
                            self.jugador_escogido.coger(producto)
                            print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())
                        
                    for j in self.lista_mesas:
                        if  self.jugador_escogido.rectangulo.colliderect(j.rectangulo):
                            if len(j.bandeja)==0 and len(self.jugador_escogido.inventario)==1:
                                j.bandeja.append(self.jugador_escogido.inventario[0])
                                print ('La mesa tiene: ',j.bandeja[0])
                                return self.jugador_escogido.dejar()
                            elif len(j.bandeja)==1 and len(self.jugador_escogido.inventario)==0:
                                    producto=j.get_bandeja()
                                    del (j.bandeja[0])
                                    self.jugador_escogido.coger(producto)
                                    print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())
                            else:
                                pass
                                    
                    for f in self.lista_plateros:
                        if  self.jugador_escogido.rectangulo.colliderect(f.rectangulo):
                            if  len(self.jugador_escogido.inventario)>=1:
                                todos_true=True
                                for a in self.jugador_escogido.inventario:
                                    if a.get_estado()==False:
                                        todos_true=False
                                if todos_true:
                                    for a in self.jugador_escogido.inventario:
                                        f.bandeja.append(a)
                                print ('El platero tiene: ')
                                for a in f.bandeja:
                                    print ('platero',a)
                                self.jugador_escogido.inventario.clear()
                                return
                            
                            elif len(self.jugador_escogido.inventario)==0 and len(f.bandeja)!=0:
                                    for q in f.bandeja:
                                        self.jugador_escogido.coger(q)
                                    f.bandeja.clear()
                                    for a in self.jugador_escogido.inventario:
                                        print (a)
                                    
                    if self.jugador_escogido.rectangulo.colliderect(self.hornouno.rectangulo):            
                            if len(self.jugador_escogido.inventario)==1 and len(self.hornouno.bandeja)==0:
                                if self.jugador_escogido.inventario[0].get_estado()==('Semilisto') and self.jugador_escogido.inventario[0].get_grupo_alimentario()==('proteina'):
                                    elemento=self.jugador_escogido.inventario[0]
                                    del (self.jugador_escogido.inventario[0])
                                    return self.hornouno.cocinar(elemento)
                       
                            elif len(self.jugador_escogido.inventario)==0:
                                if len(self.hornouno.bandeja)==1:
                                    
                                        producto=self.hornouno.bandeja[0]
                                        self.jugador_escogido.coger(producto)
                                        del (self.hornouno.bandeja[0])
                                        print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())

                    elif self.jugador_escogido.rectangulo.colliderect(self.hornodos.rectangulo):            
                            if len(self.jugador_escogido.inventario)==1 and len(self.hornodos.bandeja)==0:
                            
                                if self.jugador_escogido.inventario[0].get_estado()==('Semilisto') and self.jugador_escogido.inventario[0].get_grupo_alimentario()==('vegetal'):
                                    elemento=self.jugador_escogido.inventario[0]
                                    del (self.jugador_escogido.inventario[0])
                                    return self.hornodos.cocinar(elemento)
                       
                            elif len(self.jugador_escogido.inventario)==0:
                                if len(self.hornodos.bandeja)==1:
                                    
                                        producto=self.hornodos.bandeja[0]
                                        self.jugador_escogido.coger(producto)
                                        del (self.hornodos.bandeja[0])
                                        print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())







                    if self.jugador_escogido.rectangulo.colliderect(self.tablauno.rectangulo):
                        if len(self.jugador_escogido.inventario)==1 and len(self.tablauno.bandeja)==0:
                            if self.jugador_escogido.inventario[0].get_estado()==False and self.jugador_escogido.inventario[0].get_grupo_alimentario()==('vegetal'):
                                elemento=self.jugador_escogido.inventario[0]
                                del (self.jugador_escogido.inventario[0])
                                return self.tablauno.cocinar(elemento)
                       
                        elif len(self.jugador_escogido.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                producto=self.tablauno.bandeja[0]
                                self.jugador_escogido.coger(producto)
                                del (self.tablauno.bandeja[0])
                                print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())




                    if self.jugador_escogido.rectangulo.colliderect(self.tablados.rectangulo):
                        if len(self.jugador_escogido.inventario)==1 and len(self.tablados.bandeja)==0:
                            if self.jugador_escogido.inventario[0].get_estado()==False and self.jugador_escogido.inventario[0].get_grupo_alimentario()==('proteina'):
                                elemento=self.jugador_escogido.inventario[0]
                                del (self.jugador_escogido.inventario[0])
                                return self.tablados.cocinar(elemento)
                       
                        elif len(self.jugador_escogido.inventario)==0:
                            if len(self.tablados.bandeja)==1:
                                    producto=self.tablados.bandeja[0]
                                    self.jugador_escogido.coger(producto)
                                    del (self.tablados.bandeja[0])
                                    print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())






                                
                    if len(self.jugador_escogido.inventario)>=1:
                            if self.jugador_escogido.rectangulo.colliderect(self.basurero.rectangulo):
                                    self.jugador_escogido.inventario.clear()
                                    print (self.jugador_escogido.inventario)

                    if len(self.jugador_escogido.inventario) >= 1:
                        if self.jugador_escogido.rectangulo.colliderect(self.entrega.rectangulo):
                            self.entregar_pedido(self.jugador_escogido)
                            return
                                   
                                
                    elif len(self.jugador_escogido.inventario)==0:
                            if len(self.tablauno.bandeja)==1:
                                if  self.jugador_escogido.rectangulo.colliderect(self.tablauno.rectangulo):
                                    producto=self.tablauno.bandeja[0]
                                    self.jugador_escogido.coger(producto)
                                    del (self.tablauno.bandeja[0])
                                    print (self.jugador_escogido.inventario[0],self.jugador_escogido.inventario[0].get_estado())
    def dibujar_fondo(self):
        self.screen.fill('Grey')       
        self.screen.blit(self.cielo,(0,0))#es como el place
    def dibujar(self):
        self.dibujar_fondo()
        self.despensauno.dibujar(self.screen)
        self.despensados.dibujar(self.screen)
        self.hornouno.dibujar(self.screen)
        self.hornodos.dibujar(self.screen)
        self.basurero.dibujar(self.screen)
        self.tablauno.dibujar(self.screen)
        self.tablados.dibujar(self.screen)
        self.entrega.dibujar(self.screen)
        
        for i in self.lista_mesas:
            i.dibujar(self.screen)


        for a in self.lista_mesas:
            for q in a.bandeja:
                q.rectangulo.center=a.rectangulo.center
                q.dibujar(self.screen)
                
        
        for f in self.lista_plateros:
            f.dibujar(self.screen)

        for a in self.lista_plateros:
            for q in a.bandeja:
                q.rectangulo.center=a.rectangulo.center
                q.dibujar(self.screen)
                


        for a in self.hornouno.bandeja:
            a.rectangulo.center = self.hornouno.rectangulo.center
            a.dibujar(self.screen)

        for a in self.hornodos.bandeja:
            a.rectangulo.center = self.hornodos.rectangulo.center
            a.dibujar(self.screen)

        for a in self.tablauno.bandeja:
            a.rectangulo.center = self.tablauno.rectangulo.center
            a.dibujar(self.screen)

        for a in self.tablados.bandeja:
            a.rectangulo.center = self.tablados.rectangulo.center
            a.dibujar(self.screen)

        

        
        
        tiempo = self.temporizador.mostrar_tiempo()
        texto_tiempo = self.fuente.render(f"Tiempo: {tiempo}", False, "Red")
        self.screen.blit(texto_tiempo, (810, 20))
        
        if self.hornouno.esta_cocinando():
                self.hornotres=Freidora_Pescado('freidora_dos.jpeg',(50,50),(280,50))
                self.hornotres.dibujar(self.screen)
                tiempo_horno = self.hornouno.get_tiempo_restante()
                texto_horno = self.fuente.render(f"Horno: {tiempo_horno}", False, "Black")
                self.screen.blit(texto_horno, (self.hornouno.rectangulo.x, self.hornouno.rectangulo.y +50))
                
        if self.hornodos.esta_cocinando():
                self.hornocuatro=Freidora_Pescado('freidora_dos.jpeg',(50,50),(200,50))
                self.hornocuatro.dibujar(self.screen)
                tiempo_horno = self.hornodos.get_tiempo_restante()
                texto_horno = self.fuente.render(f"Horno: {tiempo_horno}", False, "Black")
                self.screen.blit(texto_horno, (self.hornodos.rectangulo.x, self.hornodos.rectangulo.y +50))

                
        if self.tablauno.esta_cocinando():
            tiempo_tabla = self.tablauno.get_tiempo_restante()
            texto_tabla = self.fuente.render(f"Tabla: {tiempo_tabla}", False, "Black")
            self.screen.blit(texto_tabla, (350, 60))

        if self.tablados.esta_cocinando():
            tiempo_tabla = self.tablados.get_tiempo_restante()
            texto_tabla = self.fuente.render(f"Tabla: {tiempo_tabla}", False, "Black")
            self.screen.blit(texto_tabla, (410, 60))


            
        self.uno_alpha.dibujar(self.screen)
        self.dos_alpha.dibujar(self.screen)

        self.uno_betha.dibujar(self.screen)
        self.dos_betha.dibujar(self.screen)
        
        self.uno_alpha.dibujar_inventario(self.screen)
        self.dos_alpha.dibujar_inventario(self.screen)

        self.uno_betha.dibujar_inventario(self.screen)
        self.dos_betha.dibujar_inventario(self.screen)
        
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
        self.jugador_escogido.actualizar()
        self.hornodos.actualizar()
        self.hornouno.actualizar()
        self.tablauno.actualizar()
        self.tablados.actualizar()
        if self.temporizador_receta.terminar():
            self.puntaje -= 10
            self.generar_receta()
            self.temporizador_receta.iniciar()
        
        if self.temporizador.terminar():
            self.permitir = False

    def mostrar_pantalla_final(self):
        ventana = tk.Toplevel()
        ventana.geometry("300x200")
        ventana.title("Fin del nivel")

        texto = tk.Label(ventana,text=f"Nivel terminado\nPuntaje: {self.puntaje}",font=("Arial", 20))
        texto.pack(pady=40)

        boton = tk.Button(ventana,text="Cerrar",font=("Arial", 12),command=ventana.destroy)
        boton.pack()
       
        ventana.wait_window()
        
            

    def correr(self):
        
        while self.permitir:
            self.permitir_eventos()
            self.actualizar()
            self.dibujar()
            pygame.display.update()#actualiza el display
            self.clock.tick(60)#frames
        pygame.display.quit()
        self.mostrar_pantalla_final()
    
        
    
    
        
    
