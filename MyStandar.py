import re, os, sys, numpy as np #se importa re para manejo de expresiones regulares, os para el manejo de archivos y sys para la entrada y salidas


class Parameters: #se crea la clase parametros para el manejo de las variables de entrada
    def get_values(n): #funcion que permite decidir cuantos datos se ingresaran por pantalla
        return sys.argv[1:n+1]    #se piden los  valores de entrada
    class Check():   #subclase para validar y chequear que los parametros sean correctos y emitan mensajes de error respectivos
        def __init__(self,   **kwargs ):
            self.data = kwargs['value']   
        def File(self): #se verifica y valida que el valor corresponda al nombre de un archivo
            if re.findall('[aA-zZ]', str(self.data)): #preguntamos si la entrada es una secuencia de caracteres
                if re.findall('([aA-zZ]*[0-9]*)*.\..*', self.data): #se pregunta si el archivo posee extensión
                    if os.path.exists(self.data): #Preguntamos si el archivo existe
                        return self.data
                    else:
                        sys.exit('El Archivo:   no se encuentra en el directorio. Asegurese de estar escribiendo el nombre correctamente o que el archivo este en el directorio donde se encuentra el archivo Dijkstra.py') #se imprime el mensaje detallado en la linea anterior
                else:
                    sys.exit("El Archivo no Posee Extensión. Ejemplo: grafo8.txt. Ejecute el Programa Nuevamente")
        def Int(self): #se verifica y valida que el valor sea un entero
            if re.findall('[aA-zZ]', str(self.data)): #preguntamos si la entrada es una secuencia de caracteres
                sys.exit("El Parametro Solicitado Debe ser un Numero, Intentelo Nuevamente")
            else: 
                if re.findall('[0-9]*\.[0-9]*',str(self.data)): #preguntamos si la entrada es un decimal
                    sys.exit('El Numero Ingresado debe ser un Numero Entero')
                elif int(self.data) < 0: #preguntamos si el entero ingresado es menor o igual que cero
                    sys.exit('El Indice debe ser mayor que 0')
                else:
                    self.data = int(self.data) #cambiamos el tipo de dato de la entrada que era str a int
                    return self.data  
class Dijkstra(): #clase con las funciones necesarias para obtener el camino mínimo mediante el algoritmo de dijkstra
    def __init__(self, *args, **kwargs): #se iniciaaliza la clase
        self.start = kwargs['Start'] #origen del camino
        self.end = kwargs['End'] #termino del camino
        self.graph = kwargs['Graph'] #matriz que represente al grafo
        if self.graph is not None : self.V =  self.graph[0].size #se pregunnta si hay un  grafo y se establece la cantidad de nodos
        self.path = [] #arreglo donde se almacenara la ruta del camino minimo
        self.Dijkstra_Object = kwargs['Solution'] #objeto con todos los parametros de Dijkstra
        self.dist = 0 #variable que almacenara la distancia total del camino mínimo entre los dos nodos
    def dijkstra(self):   #metodo para calcular el camino minimo solicitado
        distance = [np.inf] * self.V #se inicializa el arreglo de las distancias como infinito
        parent = [-1] * self.V #se inicializa un arreglo que ira guardando los nodos ya visitados
        distance[self.start] = 0 #se establece que la distancia al nodo de origen es 0
        unvisited = [] #se establece un arreglo que ira guardando los nodos no visitados
        [unvisited.append(i) for i in range(self.V)] #se establece que todos los nodos no están visitados 
        while unvisited: #mientras haya nodos sin visitar
            minimum = np.inf; visited = -1 
            for i in range(len(distance)): #ciclo desde 0 hasta cantidad de vertices
                if distance[i] < minimum and i in unvisited: #si la distancia  del nodo actual es menor que el minimo y el nodo no esta visitado
                    minimum = distance[i] #la distancia mínima es igual a la distancia del nodo actual
                    visited = i #se declara el nodo i como visitado
            unvisited.remove(visited) #removemos el nodo visitado de la lista de nodos no visitados
            for i in range(self.V):  #ciclo dede 0 a la cantidad de nodos del grafo
                if self.graph[visited][i] and i in unvisited: #si el nodo consultado existe y ademas no esta visitado
                    if distance[visited] + self.graph[visited][i] < distance[i]: #si la distancia al nuevo nodo es menor a la distancia al nodo utilizado como opcion anterior
                        distance[i] = distance[visited] + self.graph[visited][i] #se actualiza la distancia
                        parent[i] = visited #se incluye en parent el nodo visitado
        self.start = 0 
        for i in range(1, len(distance)):  #ciclo desde 1 a cantidad de elementos en distance
            if i==self.end: #si el nodo i es el nodo de destino del algoritmo
                final_distance = int(distance[i]) #la distancia final será la distancia actual(i)
                nodo = i #se declara la variable nodo y se iguala a i
                while parent[nodo]!=-1: #mientras el nodo no sea el final
                    self.path.append(nodo) #se añade el nodo a la ruta del camino minimo
                    nodo = parent[nodo] #ahora nodo toma el valor del siguiente nodo en la ruta a destino (de manera inversa)
                self.path.append(nodo) #se añade el último nodo a la ruta del camino minimo
        self.dist = final_distance #se establece la distancia total desde el origen al destino
        self.path = self.path[::-1] #se revierte el camino para establecer el camino minimo desde origen a destino
        return self #se retorna el objeto, incluyendo su ruta
    def printSolution(self): #función que imprime el camino minimo y la distancia mínima
        print("La Ruta Mas Corta Entre el Origen:  " +str(self.Dijkstra_Object.start) + " y el Destino:  " + str(self.Dijkstra_Object.end)+"  Es:  ")
        [ print(str(node)+" -> ", end=' ') for node in self.Dijkstra_Object.path ]
        print("Distancia del Recorrido:   "+str(self.Dijkstra_Object.dist), end=' ')
        
                
        
    
    
        
            
            
        
        
            

            
        
                    
       
        