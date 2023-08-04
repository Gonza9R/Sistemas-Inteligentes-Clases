import networkx as nx #pip install networkx
import math
import matplotlib.pyplot as plt

#Actividad 4.1 Busqueda con Informacion
#Gonzalo Hernández Hernández 
#José Fernando Ramírez Roldán 

#funcion para checar si un nodo se encuentra en la lista
def checkListNodes(target,nodeList):
    if len(nodeList)!=0:
        for i,x in enumerate(nodeList):
            if x[0]==target:
                return i,True
    return 0, False        

#Se crea una clase Position para poder manejar de una manera estructurada las coordenadas de cada ciudad
#Los atributos de esa clase es la latitud y la longitud de cada ciudad.
#Esta clase incluye el constructor y métodos para obtener los atributos de la clase
class Position():
    def __init__(self,latitude, length):
        self.latitude=latitude
        self.length=length
    def getLatitude(self):
        return self.latitude
    def getLength(self):
        return self.length
    
 #Funcion para convertir en radianes   
def convertToRadians(value):
    return (math.pi/180)*value

#Funcion para elevar un valor al cuadrado
def toSquared(value):
    return math.pow(value,2)


#Se ocupó fórmula de Haversine para realizar el calculo de la distancia de un punto de la tierra o otro punto de la tierra
#Se utilizó esta fórmula debido a que con la latitud y longitud se puede calcular la distancia, pero se tiene que considerar
#la curvatura terrestre por lo que esta fórmula considera esto con un modelo matemático
# https://www.genbeta.com/desarrollo/como-calcular-la-distancia-entre-dos-puntos-geograficos-en-c-formula-de-haversine
def distanceInKm(posOrigen,posDestino):
    RADIO_TIERRA=6.371 #radio de la tierra en KM
    
    #calculamos la diferencia entre la latitud de la posición destino y la posición origen. De igual manera la longitud
    latitude_difference= convertToRadians(posDestino.getLatitude()-posOrigen.getLatitude())
    length_difference= convertToRadians(posDestino.getLength()-posOrigen.getLength())
    
    #Se empieza a implementar la fórmula de Haversine
    a=toSquared(math.sin(latitude_difference/2))+(math.cos(convertToRadians(posOrigen.getLatitude()))*
    math.cos(convertToRadians(posOrigen.getLatitude()))*math.cos(convertToRadians(posDestino.getLatitude()))*
    toSquared(math.sin(length_difference/2)))
    
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    return (RADIO_TIERRA*c)*1000 # *1000 para que salga en km

#algoritmo de busqueda por Profundidad, le tenemos que ingresar nodo raiz y el nodo a buscar         
def greedyAlgorithm(G,rootNode,targetNode,heuristics):
    lista=[]#se crea una estructura de datos stack (pila)
    ruta=[]#se crea una lista que ira guardando el recorrido del algoritmo
    costo=0 #variable que ira guardando el costo de la ruta
    
    root=[rootNode,heuristics[rootNode],0] #se agrega en un arreglo tridimensional la informacion del nodo raíz, la heurística de ese nodo y el costo que es 0
    
    lista.append(root)#se empieza agregando la raiz para 
    #ruta.append(rootNode)
    
    while (len(lista))!=0:#condicion de para cuando la pila este vacia
        lista.sort(key=lambda x:x[1]) #ordenamos la lista con base en el menor costo
        #meter a la lista los hijos e ir sacando el de menor costo, asi el algoritmo
    
        v= lista.pop(0)#como es una pila, necesitamos sacar el ultimo elemento que fue agregado
       
        print(v[2],"costo por cada acumulado")
        costo+=int(v[2]) #se va sumando el costo del nodo que se está analizando
        
        edgesNode = list(G.edges(v[0],data='weight'))#funcion para encontrar las conexiones de un nodo con su peso
        print(ruta,"soy ruta")
        for i in range((len(edgesNode)-1),-1,-1):#se hace un recorrido inverso de los hijos del nodo, ya que nuestro recorrido de profundidad es hacia la izquierda, esto es para que el ultimo elemento agregado lo podamos popear y analizar         
            if edgesNode[i][1] not in ruta:
                item=[edgesNode[i][1],heuristics[edgesNode[i][1]],edgesNode[i][2]]#se crea una variable con los datos que necesitamos
                lista.append(item)#si el hijo no se ha visitado, se agrega al recorrido
        if v[0] not in ruta:
              ruta.append(v[0])#lo agregamos al recorrido, debido a que ya se visito el nodo   
        if v[0]==targetNode:#si el ultimo elemento que se saco de la pila es el nodo buscado, se termina el programa
            print("Nodo "+targetNode+" encontrado")
            print(ruta,"soy ruta")
            print("El costo total en km carretera es: "+str(costo))
            lista.clear()
            
def aStarAlgortihm(G, rootNode,targetNode,heuristics):
    lista=[]#se crea una estructura de datos stack (pila)
    ruta=[]#se crea una lista que ira guardando el recorrido del algoritmo
    acumWeight={}#diccionario para guardar el costo acumulado de cada nodo
    parents={}#diccionario para guardar el padre de cada nodo
    f_NValues={}#diccionario para guardar la f(n) de cada nodo
    acumWeight[rootNode]=0 #asignamos el costo acumulado del nodo raiz, en este caso es 0, porque de ese se empieza
    parents[rootNode]=rootNode#asignamos el padre del nodo raiz que en este caso es el mismo
    f_NValues[rootNode]=acumWeight[rootNode]+heuristics[rootNode] #para la f(n) sumamos la heuristica del nodo y el costo acumulado del nodo
    root=[rootNode,f_NValues[rootNode],acumWeight[rootNode],parents[rootNode]] #toda la información anterior la asignamos a una variable para agregarla a la pila
    lista.append(root)
    
    while (len(lista))!=0:
        lista.sort(key=lambda x:x[1])#ordenamos la pila de menor a mayor de acuerdo a la f(n)
        v=lista.pop(0) #sacamos el primer elemento
        ruta.append(v[0])#agregamos a la ruta ese nodo
        
        edgesNode = list(G.edges(v[0],data='weight')) #obtenemos los hijos del nodo que se está analizando junto con el peso
        
        for neighbor in edgesNode:#recorremos todos los hijos del nodo
            print(neighbor)
            #checamos si el hijo aun no esta en la ruta
            if neighbor[1]not in ruta:
                    check= checkListNodes(neighbor[1],lista) #checamos si se encuentra en la lista el nodo, si no se encuentra lo agregamos
                    if check[1]==True: #si se encuentra el nodo en la lista continuamos para comparar los costos y si no agregamos directamente ese nuevo nodo 
                        checkingCost=acumWeight[neighbor[0]]+int(neighbor[2])
                        if checkingCost<acumWeight[neighbor[1]]: #checamos el costo anterior y el nuevo costo, si es menor el costo actualizamos ese costo acumulado
                            lista.pop(check[0])#borramos el costo que se encuentra actualmente en la pila
                            parents[neighbor[1]]=neighbor[0]#actualizamos el padre de ese nodo
                            acumWeight[neighbor[1]]=acumWeight[neighbor[0]]+int(neighbor[2]) #actualizamos el costo acumulado del nodo
                            f_NValues[neighbor[1]]=acumWeight[neighbor[1]]+heuristics[neighbor[1]]#actualizamos la f(n) del nodo
                            node=[neighbor[1],f_NValues[neighbor[1]],acumWeight[neighbor[1]],parents[neighbor[1]]]#asignamos los nuevos valores
                            lista.append(node)#metemos ya actualizado el nodo en la pila
                    #agregamos el nuevo nodo con todos sus valores           
                    else:
                        parents[neighbor[1]]=neighbor[0]
                        acumWeight[neighbor[1]]=acumWeight[neighbor[0]]+int(neighbor[2])
                        f_NValues[neighbor[1]]=acumWeight[neighbor[1]]+heuristics[neighbor[1]]
                        node=[neighbor[1],f_NValues[neighbor[1]],acumWeight[neighbor[1]],parents[neighbor[1]]]
                        lista.append(node)
        #si encontramos el nodo que estamos buscando, el programa termina y se despliega la ruta
        if v[0]==targetNode:
            print("Nodo "+targetNode+" encontrado")
            print(ruta,"soy ruta")
            print("costo total: "+str(acumWeight[targetNode]))
            lista.clear()
            #recorremos hacia atras, empezando con el nodo destino y buscando su padre hasta llegar al inicio y así mostrar la ruta
            for i in range((len(ruta)-1),0,-1):
                if parents[ruta[i]]!=ruta[i-1]:
                    ruta.pop(i-1)
                
    print(ruta,"nueva ruta")
    print("aStarAlgorithm")


#Creacion del grafo
Grafo = nx.Graph()

#nombres de los archivos a utilizar 
nombre="ciudades.txt"
locationsTxt="cities_locations.txt"

#abrimos el primer archivo que contiene las carreteras entre ciudades
with open(nombre) as f:
   for line in f:
      table=line.split()
      if len(table)>=3:
        Grafo.add_edge(table[0],table[1],weight=table[2])
      else:
          Grafo.add_node(table[0])

      
print("Nodos del grafo: ")
print(Grafo.nodes)
print("Arcos de cada nodo: ")
print(Grafo.edges.data())
#ingreso de datos, en este caso ciudad inicio y ciudad final
initialCity = input("Ingresa la ciudad de inicio ")
finalCity=input("Ingresa la ciudad destino ")

#diccionarios para las heuristicas y para las locacalizaciones de cada ciudad
heuristics={}
city_locations={}

#en este fragmento se lee el archivo que contiente la latitud y longitud de cada ciudad
with open(locationsTxt) as f:
   for line in f:
      table=line.split()
      city_locations[table[0]]=table[1],table[2]
      
cityB=Position(float(city_locations[finalCity][0]),float(city_locations[finalCity][1]))
#calcular la heuristica dependiendo la ciudad inicial y la ciudad final
for city in city_locations:
    cityA=Position(float(city_locations[city][0]),float(city_locations[city][1]))
    heuristics[city]=distanceInKm(cityA,cityB)

for i in Grafo.edges.data():
    print(i)
    
    
print("Qué algoritmo desea utilizar")
print("1 A Star")
print("2 Greedy")
selectAlgorithm=input()
if selectAlgorithm=="1":
    print("A Star ALGORITHM")
    aStarAlgortihm(Grafo,initialCity,finalCity,heuristics)
elif selectAlgorithm=="2":
    print("Greedy ALGORITHM")
    greedyAlgorithm(Grafo,initialCity,finalCity,heuristics)
 
#aStarAlgortihm(Grafo,initialCity,finalCity,heuristics)

#greedyAlgorithm(Grafo,initialCity,finalCity,heuristics)

print(heuristics)

#fragmento de codigo para mostrar graficamente el grafo basado en el siguiente link:
#https://ernestocrespo13.wordpress.com/2012/11/25/creacion-de-grafos-con-networkx-parte-1-2/
pos=nx.spring_layout(Grafo) 
nx.draw_networkx(Grafo,pos)
labels = nx.get_edge_attributes(Grafo,'weight')
nx.draw_networkx_edge_labels(Grafo,pos,edge_labels=labels)
plt.show()
