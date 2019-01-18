import codecs
import sys
class MiArchivo:
    """
    """
    #Realizo el contructor enivaindo un parametro
    def __init__(self, nombre):
        """
        """
        self.nombre_archivo = nombre 
        #EL archivo se abrira detendiendo del nombre del archivo
        self.archivo = codecs.open(self.nombre_archivo, "r")


    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()

class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "a")
        #Se imprime la infrmacion
    def agregar_informacion(self, p):
        self.archivo.write("%s\n" % (p.obtenerNombres()))

    def cerrar_archivo(self):
        self.archivo.close()
        