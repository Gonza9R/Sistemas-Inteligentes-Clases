import turtle
import time
import numpy as np
import random

#Actividad 3 Agentes Inteligentes
#Equipo: Gonzalo Hernández Hernández
#José Fernando Ramírez Roldán

#Utilizamos la libreria Turtle para poder realizar la actividad graficamente

board = turtle.Turtle() #objeto turtle para poder crear algun objeto grafico



#Funcion para crear un cuadrado, darle color, posicion y un tamaño
def draw_box(t,x,y,size,fill_color):
    t.penup() #penup, levanta (limpia), por si se esta ocupando con algun otro objeto
    t.goto(x,y) # mueve el objeto (pluma) a una posicion dada, que dibujara nuestra figura 
    t.pendown() # empieza a dibujar
    t.fillcolor(fill_color) #le da un color a la figura
    t.begin_fill() #se llama a esta funcion para llenar el color de la figura
    for i in range(0,4):
        board.forward(size) # mueve hacia delante el objeto que dibuja nuestra figura, tomando de referencia el tamaño que le damos
        board.right(90) # cada que llega al tamño que le dimos, gira la pluma 90 grados, para poder formar el cuadrado
    t.end_fill()


delay = 0.5 # variable que nos ayuda a que el ambiente grafico, tome un tiempo entre cada frame


# Objeto Turtle.Screen que nos ayuda a crear la pantalla del ambiente
#Darle un color, ancho y altura
wn = turtle.Screen()
wn.title("Agent Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

#Objeto tipo turtle, con el que creamos el agente (box verde), le damos un color, figura, posicion y tamño
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(-5, -5)
head.shapesize(1.5)

 
start_x = -230 # punto de partida en X de la primera caja a dibujar
start_y = -110 # punto de partida en Y de la primera caja a dibujar
box_size = 30 # tamaño de cada cuadrado del mapa
board.speed(100) #velocidad del dibujado
wn.tracer(0)#Acelerar el dibujado

color_white = "white"
color_black = "black"
tablero=np.ones([13,17]) #creacion de matriz llena de 1's
n=11 #filas de la matriz
m=1 #columna de la matriz pero que se ira agragando conforme se van llenando
maty=0 #posicion de donde se poscionara el agente en la matriz en Y
matx=0 #posicion de donde se poscionara el agente en la matriz en X
print(tablero)
for i in range(0,4): #  primer parte del mapa de 3x12
    for j in range(0,12):
        if i!=3:
            if j<5 or j>8:#condicion para poder dejar un espacio entra las cajas, esto debido a las condiciones del mapa del ejercicio
                draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white) #se dibuja la caja blanca, se toma de referencia de donde se empezo a dibujar
                tablero[n][m]=0 #se llena la matriz en 0, porque como es un espacio en blanco, significa que es un espacio donde se puede mover el agente
            m=m+1
        else:
             draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white)
             tablero[n][m]=0
             m=m+1 #se aumenta las columnas
    if m>=12:
        m=1
    n=n-1
 
 #seguna parte del mapa, de 3x15 donde ya hay partes en negro. Se define una condicion para que en determinada parte del dibujada las cajas sean negras, esto de acuerdo al mapa del ejercicio
for i in range(4,7):
    for j in range(0,15):    
        if i>4:
            if (j>2 and j<5) or (j>=7 and j<9):    
                draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_black)
                tablero[n][m]=1
                m=m+1
            else:
                draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white)
                tablero[n][m]=0
                m=m+1
        else:
            draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white)
            tablero[n][m]=0
            m=m+1
    if m>=15:
        m=1
    n=n-1

#Tercera parte del mapa de 4x12, donde la mayoria del mapa son cajas blancas, solo una fila contiene cajas negras
for i in range(7,11):
    for j in range(0,12):
        if i>7:
            draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white)
            tablero[n][m]=0
            m=m+1
        else:
            if j>2 and j<9:
                draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_black)
                tablero[n][m]=1
                m=m+1
            else:
                draw_box(board,start_x + j*box_size, start_y + i*box_size, box_size,color_white)
                tablero[n][m]=0
                m=m+1
    if m>=12:
        m=1
    n=n-1

print(tablero)


def movup(maty,matx):
    y = head.ycor() #metodo para obtener la coordenada en Y del agente
    head.sety(y+30)#metodo para mover al agente en Y, hacia arriba
    maty=maty-1 #se mueve la posicion del agente en la matriz hacia arriba
    tablero[maty+1][matx]=0 #se libera la posicion donde se encontraba el agente
    tablero[maty][matx]=8 # se actualiza la nueva posicion que ocupa el agente, en el tablero
    wn.update() #se actualiza el mapa
    return maty #se retorno la nueva posicion en y del agente, en la matriz
    
    
#funcion para mover al agente hacia abajo, en el mapa grafico y en la matriz. Misma logica que Movup 
def movdown(maty,matx):
    y = head.ycor()
    head.sety(y-30)
    maty=maty+1
    tablero[maty-1][matx]=0
    tablero[maty][matx]=8
    wn.update()
    return maty

#funcion para mover al agente hacia la izquierda, en el mapa grafico y en la matriz. Misma logica que Movup 
def moveleft(matx,maty):
    x = head.xcor()
    head.setx(x-30)
    tablero[maty][matx]=0
    matx=matx-1
    tablero[maty][matx]=8
    wn.update()
    return matx

#funcion para mover al agente hacia la derecha, en el mapa grafico y en la matriz. Misma logica que Movup 
def moveright(matx,maty):
    x = head.xcor()
    head.setx(x+30)
    tablero[maty][matx]=0
    matx=matx+1
    tablero[maty][matx]=8
    wn.update()
    return matx

prueba=0
cont=0

#While para que el usuario ingrese las coordenadas iniciales del agente
while prueba==0:
    wn.update()
    w=input("Ingresa la posición x del robot favor de elegir un numero entre -215 y 205 ")
    f=input("Ingresa la posición y del robot favor de elegir un numero entre -125 y 175 ")
    w=int(w)
    f=int(f)
    maty=int((f-205)/(-30))#Posición correpondiente en matriz
    matx=int((w+245)/(30))#formula para darle la posicion en la matriz bidemensional en x
   
    if w>=-215 and w<=205 and f>=-125 and f<=175: #condicion, para que el usuario no ingrese coordenadas fuera del rango
        if tablero[maty][matx]==0: # si se encuentra libre el espacio termina el ciclo while
            prueba=1
        elif tablero[maty][matx]==1: #condicion de si la coordenanda dada, se encuentra un obstaculo
            print("Las cordenadas se encuentran en un obstaculo o fuera del mundo")
            print("Vuelva ingresar nuevas cordenadas")
       
    else:
        print("Ingreso algun valor fuera del rango ")
        print("Vuelva ingresar nuevas cordenadas")    
   


corx=(30*matx)-245 #variable que asigna la coordenada en X en el ambiente grafico
cory=205+(maty*(-30))#variable que asigna la coordenada en Y en el ambiente grafico
tablero[maty][matx]=8 #Se ocupa el espacio en la matriz con el numero 8, este es el agente
head.goto(corx,cory) # se mueve el agente a la coordenada dada por el usuario
print(tablero)
print(corx,cory) 

#ciclo para iniciar el movimiento del agente
while True:
    wn.update()
    
    
    if cont<=55: #condicion de paro. Si se llega a los 55 movimientos del agente, el programa se detiene
        print(maty,matx)
        #si se encuentra la diagonal izquierda inferior ocupada, la izquierda ocupada y arriba desocupado, el agente se va hacia arriba
        if tablero[maty+1][matx-1]==1 and tablero[maty][matx-1]==1 and tablero[maty-1][matx]==0:
            print("Arriba")
            maty=movup(maty,matx)
            #si la diagonal izquierda inferior esta ocupada y abajo este ocupado, el agente se va a la izquierda
        elif tablero[maty+1][matx-1]==1 and tablero[maty+1][matx]==1:
            matx=moveleft(matx,maty)
            print("Izquierda")
            #si  arriba esta ocupado, si diagonal superior izquierda esta ocupada y la derecha libre, el agente se va a la derecha
        elif tablero[maty-1][matx]==1 and tablero[maty-1][matx-1]==1 and tablero[maty][matx+1]==0:
            print("derecha")
            matx=moveright(matx,maty)
            #si la casilla diagonal izquierda inferio esta ocupada, el agente se va a la izquierda
        elif tablero[maty+1][matx-1]==1:
            print("Izquierda")
            matx=moveleft(matx,maty)
            #si la casilla de abajo esta ocupada, el agente se va a la izquierda
        elif tablero[maty+1][matx]==1:
            print("Izquierda")
            matx=moveleft(matx,maty)
             #si la casilla de la izquierda esta ocupada, el agente se va a la izquierda
        elif tablero[maty][matx+1]==1:
            print("abajo")
            maty=movdown(maty,matx)
             #si la casilla diagononal inferior derecha esta ocupada, el agente se va abajo
        elif tablero[maty+1][matx+1]==1:
            print("abajo")
            maty=movdown(maty,matx)
            #si la casilla diagononal superior izquierda esta ocupada y la casilla de arriba esta ocupada, el agente se va a la derecha
        elif tablero[maty-1][matx-1]==1 and tablero[maty-1][matx]==1:
            matx=moveright(matx,maty)
            print("derecha")
            #si la casilla diagononal superior derecha esta ocupada, el agente se va a la derecha
        elif tablero[maty-1][matx+1]==1:
            print("derecha")
            matx=moveright(matx,maty)
            #si la casilla diagononal superior izquierda esta ocupada, el agente se va arriba
        elif tablero[maty-1][matx-1]==1:
            print("Arriba")
            maty=movup(maty,matx)
            #si la casilla diagononal superior izquierda esta libre, si la casilla de arriba esta libre, la casilla diagonal superior derecha esta libre, si la casilla izquierda esta libre, si la casilla diagonal inferior izquierda esta libre, si la casilla de abajo esta libre y la casilla inferior diagonal izquierda esta libre, el agente se mueve Arriba  
        elif tablero[maty-1][matx-1]==0 and tablero[maty-1][matx]==0 and tablero[maty-1][matx+1]==0 and tablero[maty][matx-1]==0 and tablero[maty][matx+1]==0 and tablero[maty+1][matx-1]==0 and tablero[maty+1][matx]==0 and tablero[maty+1][matx+1]==0:
            print("Arriba")
            maty=movup(maty,matx)
        cont=cont+1
        print(cont,"contador pasos")
        time.sleep(delay)
        print(tablero)
