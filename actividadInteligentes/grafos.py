#Gonzalo Hernández Hernández a01423362
#José Fernando Ramírez Roldán a01422285

from ast import While
from re import A
import networkx as nx

#funcion que encuentra un camino hamiltoneano dentro del grafo, si lo encuentra, se lanza el camino 
def hamilton(G):
    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1]) 
                     if node != path[-1]) #exclude self loops
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                return p
            else:
                F.append((g,p))
    return None

#crear el grafo
Grafo = nx.Graph()
print("Desea ingresar los datos de forma:")
print("1 Manualmente")
print("2 Desde un archivo")
forma=input()
if forma=="1":
    try:
        while True:
           
            nodes = input("ingresa los nodos ")
            #agregar nodos al grafo
            Grafo.add_node(nodes)
            
    except KeyboardInterrupt:
        pass

    try:
        while True:
        
            edges = input("ingresa los edges  ")
            connection= edges.split(",")
            print(connection)
            #agregar vertices del nodo
            Grafo.add_edge(connection[0],connection[1])
        
    except KeyboardInterrupt:
        pass
elif forma=="2":
    orden=input("Ingrese el orden del grafo ")
    tamaño=input("Ingresa el tamaño del grafo ")
    nombre=input("Ingrese el nombre del archivo de forma nombre.txt en caso de estar en la misma carpeta en caso contrario ingrese la ruta ")
    archivo = open(nombre) #hola.txt
    caracter = 1
    for A in range(int(orden)):
        nodes = archivo.readline(1)
        Grafo.add_node(nodes)
        print(nodes)
        archivo.readline(2)

    for A in range(int(tamaño)):
        edges = archivo.readline(3)#Aqui el read line va leyendo linea por linea hasta encontrar un espacio 
        connection= edges.split(",")#y el 3 especifica el numero de espacios que lee 
        print(connection)
        Grafo.add_edge(connection[0],connection[1])
        archivo.readline(3) #Agrege este porque como iba leyendo de 3 en 3 dejaba un espacion en blanco y me mandaba a error


if nx.is_eulerian(Grafo):
    print("Es un grafo Euleriano")

    
#funcion para ver si es conexo
conexo=nx.is_k_edge_connected(Grafo,1)
print(conexo,"conexo")    

print("Grado de cada nodo")
grados_nodos=list(Grafo.degree(Grafo.nodes))
print(list(Grafo.degree(Grafo.nodes)))
par=0 #contado de pares
impar=0 #contador de impares
for A in range(len(grados_nodos)): 
    if  grados_nodos[A][1]%2==0 and grados_nodos[A][1]>0:#Numero de nodos con grado par
        par=par+1
    elif grados_nodos[A][1]%2!=0:#Numero de nodos con grado par
        impar=impar+1
  
if par>0 and impar==2 and conexo==True: #Condicion para saber si es trasversable
    print("Es un grafo transversable")
else:
    print("No traversable")
    
print("cantidad nodos par: ",par)
print("cantidad nodos impar: ",impar)
print("Nodos del grafo: ")
print(Grafo.nodes)
print("Arcos de cada nodo: ")
print(Grafo.edges)


hamiltoneano = hamilton(Grafo)
if hamiltoneano!=None:
    print("Es hamiltoneano")
print(hamiltoneano)
