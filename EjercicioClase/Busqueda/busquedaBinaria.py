class BusquedaBinaria(object):
	#Resivo un valor 
	def __init__(self,lista):
		
		self.lista_data = lista
	#metodo agregar  obtener de el arreglo final
	def agregarDatos(self,l):
		
		self.lista_data = l

	def obtenerDatos(self):
		
		return self.lista_data	
	#Relizo esta funcón para ordenar los datos
	def ordenarDatos(self):
	
		self.lista_data.sort()	
		#EL metodo de busqueda binaria enviandole el elemento a buscar
	def Busqueda(self,elemento_buscar):
		#Creación de variables necesarias para realizar la búsqueda
		inferior = 0
		superior = len(self.lista_data) -1
		medio = int((inferior + superior +1) /2)
		ubicacion = -1
		#Mientras la condición se cumplea se realizará ente bucle
		while((inferior <= superior) and (ubicacion == -1)):
			if(elemento_buscar == self.lista_data[medio]):
				ubicacion = medio
			elif (elemento_buscar < self.lista_data[medio]):
				superior = medio -1
			else:
				inferior = medio +1
			medio = int((inferior + superior + 1) / 2)
		#Retorno la ubicación del entero a buscar	
		return ubicacion
		
	def __str__(self):
		temporal = ""

		for i in self.lista_data:
			temporal = "%s %s" % (temporal,elemento_buscar)
		
		temporal = "%s %s\n" % (temporal)
		
		return temporal





					




