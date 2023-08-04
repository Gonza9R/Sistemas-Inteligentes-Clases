from math import dist
from random import random
import numpy
import pandas as pd
import random


#Actividad 9. Problemas que se resuelven con Clustering


#Gonzalo Hernandez Hernandez A01423362
#Jose Fernando Ramirez Roldan A01422285


data = pd.read_excel(io='peliculas.xlsx',sheet_name="Sheet1",header=None)

def selec_categoria(data):# Selección de categorias para asignar los clusters
    print("Selecciona una categoria para ordenarla")
    for i in range(12):#impresión del menu de opciones para el clusters
        print(i+1, data[i+1][0])
    z=int(input())# Entrada de opción 
    return(z) #regresa la opción elegida
def centroides_inicial(data,z):#Asignación de centroides inicial
    num_centroides=5 #Asiignas cuantos centroides deseas tener
    centroides=[] #Lista para guardar centroiides
    i=0#Contador de centroides
    while i<num_centroides: #Se utiliza un while para repetir el proceso de asignación hasta obtener 5 centroides con distintos valores
        n=random.choice(data[z][1:])# Se utiliza el random choice para selecionar valores alazar de la categoria seleccionada
        if centroides.count(n)==0:# Se comprueba que el valor no se encuentre en la lista 
            centroides.append(n)#Si no se encuentra se agrega a la lista
            i+=1#Se cuentan los centroides asignados
    return(centroides)# Se regresa los centroides
def distancia(data,matriz_D,centroides,z): # Se calcula las distancias de los datos con los centroides y se guarda en la matriz_D
    for i in range(len(centroides)):
        for j in range(len(data)-1):
            matriz_D[j,i]=abs(data[z][j+1]-centroides[i])
            print(j,data[z][j+1],centroides[i])
        print(matriz_D[:,i]) 
    return matriz_D
def printea(matriz_D):#Matriz para printear los datos y poder visualizarlos
    d=numpy.shape(matriz_D)
    for i in range(d[0]):
        print(i,matriz_D[i])
def categoria(matriz):# Se asigna a un centroide el valor según el cual tenga una diferencia menor
    d=numpy.shape(matriz) #Permite saber el tamaño de la matriz
    matriz_G=numpy.zeros((d[0],d[1]))#Se crea una matriz de 0 para asignar los centroides
    for i in range(d[0]):
        min_value=matriz[i,0]
        ubi_minvalue=0
        for j in range(d[1]):
            if matriz[i,j]<=min_value:
                ubi_minvalue=j
                min_value=matriz[i,j]
        matriz_G[i][ubi_minvalue]=1
        print(i,matriz_G[i])
    return matriz_G
def calcu_centroides(matriz_G,centroides,data,z):#Utilizando el resultado de la funcion categorias se calcula el nuevo valoor de centroides sumando todos los datos cercanos al clustering y dividiendolo entre el total de datos
    d=numpy.shape(matriz_G)
    for i in range(d[1]):
        sum=0
        cont=0
        for j in range(d[0]):
            if matriz_G[j,i]==1:
                sum+=data[z][j+1]
                cont+=1
        print(centroides[i])
        centroides[i]=sum/cont
        print(centroides[i])
    return centroides
def comparador(matante_G, matriz_G,contador):#Sirve para comparar que los valores de la matriz y poder decir si cambiaron o no
    d=numpy.shape(matriz_G)
    n=0
    for i in range(d[0]):#For para comparar las verdades dato por dato
        for j in range(d[1]):
            if matante_G[i,j]==matriz_G[i,j]:
                n+=1
    if n==(d[0]*d[1]):#en el caso de que sea verdad se suma 1 
        contador+=1
    else:
        contador=0# En el caso de que no se reinicia el contador 
    return contador# Permite terminar las iteraciones cuando matriz_g no cambia en 2 iteracion
def result_final(centroides,data,z,matriz_G):
    d=numpy.shape(matriz_G)
    for i in range(d[1]):
        print("Centroide =  ",centroides[i] )
        for j in range(d[0]):
            if matriz_G[j][i]==1:
                print(data[0][j+1],"  ",data[z][j+1])


z=selec_categoria(data)
centroides=centroides_inicial(data,z)
matriz_D=numpy.zeros(((len(data)-1),len(centroides))) #matriz de distancias
printea(matriz_D)
matriz_G=numpy.zeros(((len(data)-1),len(centroides))) #matriz  de grupo
contador=0
while contador<3:# Permite terminar las iteraciones cuando matriz_g no cambia en 2 iteracion
    matante_G=matriz_G
    #print(numpy.shape(matriz_D))
    matriz_D=distancia(data,matriz_D,centroides,z)
    #d=numpy.shape(matriz_D)
    printea(matriz_D)
    matriz_G=categoria(matriz_D)
    centroides=calcu_centroides(matriz_G,centroides,data,z)
    contador=comparador(matante_G,matriz_G,contador)
printea(matriz_G)
print(centroides)
result_final(centroides,data,z,matriz_G)
#al finala agregue result final para mostrarlos