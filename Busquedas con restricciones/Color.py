
import networkx as nx

#Actividad 4.1 Busqueda con Informacion
#Gonzalo Hernández Hernández a01423362
#José Fernando Ramírez Roldán a01422285
  
#Algoritmo para decidir que color asignar y comprobar los colores de los vecinos 
def checkvecino(G,node,color):
    edgesNode=list(G.edges(node))  #funcion para encontrar las conexiones de un nodo
    Azul=0
    Rojo=0
    Verde=0
    for neighbor in edgesNode:
        #Buscar si alguno de los vecinos tiene color asignado y cuales ya estan asignados
        if neighbor[1] in color: 
            if color[neighbor[1]]=="Azul":
                Azul=1+Azul
            elif color[neighbor[1]]=="Rojo":
                Rojo=1+Rojo
            elif color[neighbor[1]]=="Verde":
                Verde=1+Verde
    # Condiciones para saber que color se le debe asignar al nodo que se esta analizando
    if Azul==0 and Rojo==0 and Verde==0: 
        color[node]="Azul"
        return False
    elif Azul==0 and Rojo==0 and Verde!=0:
        color[node]="Azul"
        return False
    elif Azul==0 and Rojo!=0 and Verde==0:
        color[node]="Verde"
        return False
    elif Azul==0 and Rojo!=0 and Verde!=0:
        color[node]="Azul"
        return False
    elif Azul!=0 and Rojo==0 and Verde==0:
        color[node]="Rojo"
        return False
    elif Azul!=0 and Rojo==0 and Verde!=0:
        color[node]="Rojo"
        return False
    elif Azul!=0 and Rojo!=0 and Verde==0:
        color[node]="Verde"
        return False
    elif Azul!=0 and Rojo!=0 and Verde==0:
        color[node]="Verde"
        return False
    elif Azul!=0 and Rojo!=0 and Verde!=0:
        print("fallo")
        return True

         

#algoritmo de busqueda por Anchura, le tenemos que ingresar nodo raiz y el nodo a buscar                            
def findNodeBy_Bfs(G,rootNode,colorNode):          
    lista=[]#se crea una estructura de datos queue (cola)
    ruta=[]#se crea una lista que ira guardando el recorrido del algoritmo
    color={}
    color[rootNode]=colorNode
    lista.append(rootNode) #se empieza agregando la raiz para las dos estructuras de datos
    ruta.append(rootNode)
    
    while (len(lista))!= 0:#condicion de para cuando la cola este vacia
        v= lista.pop(0)#como es una cola, sacaremos el primero que fue agregado a la esctructura
        edgesNode=list(G.edges(v))  #funcion para encontrar las conexiones de un nodo
        print(ruta,"soy ruta")
        for neighbor in edgesNode:#recorremos todos los hijos del nodo
            if neighbor[1] not in color:
              x=  checkvecino(G,neighbor[1],color)
            if neighbor[1] not in ruta:#si no se encuentran dentro de ruta, los agregamos
                lista.append(neighbor[1])
                ruta.append(neighbor[1])
            if x==True: #Si x es True se vuelve a iniciar el programa y la asignación de colores desde el nodo que se equivoco
                color.clear()
                lista.clear()
                ruta.clear()
                color[neighbor[1]]=colorNode
                lista.append(neighbor[1]) #se empieza agregando la raiz para las dos estructuras de datos
                ruta.append(neighbor[1])
                break

    print(ruta,"soy ruta")
    print(color)
        #print("Nodo "+targetNode+" encontrado") 
            

#Creacion del grafo
Grafo = nx.Graph()

#nombres de los archivos a utilizar 
nombre="act5.txt"

#abrimos el primer archivo que contiene las carreteras entre ciudades
with open(nombre) as f:
   for line in f:
        table=line.split()
        Grafo.add_edge(table[0],table[1])
      

"""  
print("Nodos del grafo: ")
print(Grafo.nodes)
print("Arcos de cada nodo: ")
print(Grafo.edges)
"""   
#ingreso de datos, en este caso ciudad inicio
initialCity = input("Ingresa la ciudad de inicio ")

findNodeBy_Bfs(Grafo,initialCity,"Azul")