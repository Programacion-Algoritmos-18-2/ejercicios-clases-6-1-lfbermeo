from Archivos.miarchivo import MiArchivo
from Busqueda.busquedaBinaria import BusquedaBinaria
#Creo mi objeto en el cuál llamo la ruta donde se encuentra "datos.txt"
m = MiArchivo("data/datos.txt")
#obtengo la infromación de mis archivos
lista = m.obtener_informacion()
#Cada linea del archivo lo separo por coma
lista = [l.split(",") for l in lista]
#Creo una nueva lista
lista2 = []
#recorro la lista
for x in lista:
	#A esa nueva lista le agrego las sublistas de archivo
	for l in x:
		#agrego a la lista 2 los elelmentos de la sublista como python toma los elementos como cadena le coloco que sean enteros
		lista2.append(int(l))
#Creo el objeto enviandole la lista final 
busqueda = BusquedaBinaria(lista2)
#imprimo la lista
print(lista2)
#declaro el entero a buscar
enteroBuscar = 3
#Llamo al método donde ordeno los datos
busqueda.ordenarDatos()
#creo una variable donde llamo a su objeto en el cual le envio el valor del entero a buscar
posicion = busqueda.Busqueda(enteroBuscar)
#Realizo un ciclo de comparación 
if(posicion == -1):
	#Imprime dependiendo del resultado
	print("EL entero %d no se encontro" % (enteroBuscar))
else:
	print("EL entero %d se encontro en la posicion %d"%(enteroBuscar, posicion))
