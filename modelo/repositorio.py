from abc import ABC, abstractmethod

# ISP / DIP: interfaz especifica para la gestion de las tareas:
class RepositorioTareas(ABC):
    @abstractmethod
    def agregar(self, tarea): ...

    @abstractmethod
    def listar(self): ...

    @abstractmethod
    def obtener(self, indice): ...

    @abstractmethod
    def eliminar(self, indice): ...

    @abstractmethod
    def actualizar (self, indice, tarea): ...


# OCP / DIP: implementacion en memoria, sustituciones (LSP)
class RepositorioMemoria(RepositorioTareas):
    def __init__(self):
        self._datos =[]

    def agregar(self, tarea):
        self._datos.append(tarea)

    def listar(self):
        # Devuelve lista de diccionarios, pero no expone su implementacion como objetos.
        return [t.datos for t in self._datos]

    def obtener(self, indice):
        return self._datos[indice]

    def eliminar(self, indice):
        del self._datos[indice]

    def actualizar(self, indice, tarea):
        self._datos[indice] = tarea

        
