#Actividad 7 Naive Bayes 
#Gonzalo Hernández Hernández a01423362
#José Fernando Ramírez Roldán a01422285
def tablas(puestos, categorias, tipo,z,m):
    lista=[]
    mem=[]
    for i in range(int(categorias[tipo])):
        s=puestos[z].split()
        for j in s:
            lista.append(j)
        z+=1
        
    for i in range(len(m)):
        mem.append(lista.count(m[i]))
    return(mem,z)
       
def tabla_total(puestos):
    p=[] #para guardar las palabras utilizadas en todos los puestos
    g=[] #lista para guardar 1 sola vez todas las palabras de la base de datos corresponde a la variable m
    lista=[]#guarda las frecuencia con que se repiten las palabras en la base de datos
    
    for i in range(len(puestos)):
        s=puestos[i].split() 
        for j in s:
            p.append(j)
            if j not in g:
                g.append(j)
                        
    g.sort() #Acomodar el banco de palabras en orden alfabetico
    for i in range(len(g)):# Para contar el numero de veces que se repiten las palabras en g
        lista.append(p.count(g[i]))
    print(lista)   
    return(g,lista)     
def pCk(puestos,categorias,tipo):
    c_k=categorias[tipo]/len(puestos)
    return c_k
def pxiC_k(categorias,memoria,l_new):
    px=1
    for i in range(len(l_new)):
        if l_new[i]==1:
            px=px*(memoria[i]/categorias)
        elif l_new[i]==0 and memoria[i]!=0:
            px=px*(1-(memoria[i]/categorias))
    print(px)
    return(px)
def PXI(cat,pck,pxick):
    px=0
    for i in cat:
        px=px+(pck[i]*pxick[i])
    return px        
            
        
nombre="puestos.txt"

puestos=[] #Memoria de puestos en la base de datos
categorias={}#Numero de puestos por categoria
cat=[]#Lista para guardar cada categoria

#abrimos el primer archivo que contiene las carreteras entre ciudades
with open(nombre) as f:
   for line in f:
      table=line.split('/')
      puestos.append(table[0])
      t= table[1].split('\n')
      if t[0] not in cat:
          cat.append(t[0])

      if categorias.get(t[0])==None:
         
         categorias[t[0]]=1
      else:
          categorias[t[0]]=categorias[t[0]]+1

memoria={}# En esta memoria se guarda la frecuencia con que se repete cada palabra por tipo de puesto
(m,memoria["Total"])=tabla_total(puestos) # Es el banco de palabras 
z=0#Contador
pck={}#Diccionario donde se guarda p(C_k)
pxick={}#Diccionario deonde se guarda la p(x_i|C_k)

for i in range(len(cat)):# Aqui se calcula la probabilidad de que tipo de puesto es
    (memoria[cat[i]],z)=tablas(puestos,categorias,cat[i],z,m)#Se calcula la tabla de frecuencias de acuerdo al tipo de empleo
    pck[cat[i]]=pCk(puestos,categorias,cat[i]) #Se calcula la probabilidad de que sea un determinado tipo de puesto
    print("PcK ", cat[i], "  ", pck[cat[i]])
    print(memoria[cat[i]])
repetir=1
while repetir==1:          
    nuevopuesto=input("Ingresa el nombre del nuevo puesto a clasificar \n")#Se ingresa el puesto que se desea determinar
    novo=nuevopuesto.split() #se guardan las palabras por separado
    l_new=[]#lista para guardar las frecuencias del nuevo puesto
    for i in range(len(m)): 
            l_new.append(novo.count(m[i]))# Se cuenta la palabras y se guarda en una lista de manera ordenada
    for i in range(len(cat)):
        pxick[cat[i]]=pxiC_k(int(categorias[cat[i]]),memoria[cat[i]],l_new)# Se calcula la p(xi|C_k)
    pxi=PXI(cat,pck,pxick)
    proba=[]# Lista para guardar las probabilidades de que sea un determinado tipo de puesto
    p=0
    for i in range(len(cat)):
        proba.append((pck[cat[i]]*pxick[cat[i]])/pxi)
        print(cat[i], " es de ", proba[i])
        if proba[i]>p:
            p=i
    if proba.count(0)==len(proba):
        print("No se puede determinar debido a los datos")
    else:
        print("El puesto de ",nuevopuesto," es del area de ", cat[p], "con una probabilidad de",proba[p])
    repetir=int(input("Desea clasificar otro puesto:\n 1- Si\n 2-No\n"))
   