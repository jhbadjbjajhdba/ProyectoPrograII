import tkinter as tk
import nivel_uno
import nivel_dos
import nivel_tres

class PantallaPrincipal():
    def __init__(self):
        self.window = None
        
    def empezar_uno(self):
        self.window.withdraw()
        juego=nivel_uno.Juego()
        juego.correr()
        self.window.deiconify()
        
    def empezar_dos(self):
        self.window.withdraw()
        juego=nivel_dos.Juego()
        juego.correr()
        self.window.deiconify()

    def empezar_tres(self):
        self.window.withdraw()
        juego=nivel_tres.Juego()
        juego.correr()
        self.window.deiconify()
        
        
    def volver(self):
        self.miniwindow.withdraw()
        self.window.deiconify()
        
    def mostrar_tutorial(self):
        self.window.withdraw()
        self.miniwindow=tk.Tk()
        self.miniwindow.geometry('800x400')
        self.miniwindow.title('Undercooked: Tutorial')
        self.miniwindow.resizable(False,False)
        infor=tk.Label(self.miniwindow,text=('Controles:\n-F: Botón de acción\n-R: Cambio de personaje\n-Flechas: Movilización '),fg='black',font=(35), compound='bottom')
        infor=tk.Label(self.miniwindow,text=('Controles:\n-F: Botón de acción\n-R: Cambio de personaje\n-Flechas: Movilización '),fg='black',font=(35), compound='bottom')
        infor.place(x=10,y=10)
        boton_volver=tk.Button(self.miniwindow, text='Volver', font=('Papyrus',12),command=self.volver)
        boton_volver.place(x=200,y=200)
        
    def inicializar(self):
        
        self.window=tk.Tk()
        self.window.geometry('800x400')
        self.window.title('Undercooked')
        self.window.resizable(False,False)
        titulo=tk.Label()
        info=tk.Button(self.window, text='Tutorial', font=('Arial',12),command=self.mostrar_tutorial)
        info.place(x=200,y=300)
        boton_iniciar=tk.Button(self.window, text='Mapa 1', font=('Arial',12),command=self.empezar_uno)
        boton_iniciar_dos=tk.Button(self.window, text='Mapa 2', font=('Arial',12),command=self.empezar_dos)
        boton_iniciar_tres=tk.Button(self.window, text='Mapa 3', font=('Arial',12),command=self.empezar_tres)
        titulo=tk.Label(self.window,text=('UNDERCOOKED: The Video Game'),fg='black',font=(35), compound='bottom')
        titulo.place(x=100,y=10)
        boton_iniciar.place(x=100,y=200)
        boton_iniciar_dos.place(x=200,y=200)
        boton_iniciar_tres.place(x=300,y=200)
        self.window.mainloop()
        
    
        
pg=PantallaPrincipal()
pg.inicializar()
