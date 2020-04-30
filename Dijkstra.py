import numpy as np, MyStandar as ms #se importa la libreria numpy para manejar arreglos y la libreria personal creada manualmente
file, start, end = ms.Parameters.get_values(3) #pedimos el nombre del archivo, el nodo de inicio y el nodo de termino
file, start, end = ms.Parameters.Check(value=file).File(), ms.Parameters.Check(value=start).Int(), ms.Parameters.Check(value=end).Int() #se chequea que los parametros sean correctos dentro de un rango y correspondiente al tipo de dato
Solution = ms.Dijkstra(Start = start, End = end, Graph = np.loadtxt(file, skiprows=1), Solution = None).dijkstra() #Se Aplica el Algoritmo de Dijkstra al grafo recibido desde el archivo
ms.Dijkstra(Start=None, End=None, Graph=None, Solution = Solution).printSolution() #se imprime el camino mínimo entre el origen y el destino dado por los usuarios
