# SRP: creamos una clase que va a gestionar unicamente datos y validaciones de una tarea.

class Tarea:
    def __init__(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El titulo no puede estar vacío")
        self._titulo = titulo
        self._descripcion = descripcion
        self._completada = False

    def completar(self):
        self._completada = True #SRP metodo unico que se usa para completar.

    def editar(self, nuevo_titulo, nueva_descripcion):
        #SRP: solo modifica su propio estado.
        if not nuevo_titulo:
            raise ValueError("El titulo no puede estar vacío")
        self._titulo = nuevo_titulo
        self._descripcion = nueva_descripcion

    @property
    def datos(self):
        # proporcionar datos en un formato simple para la vista
        return {
            "titulo": self._titulo,
            "descripcion": self._descripcion,
            "completada": self._completada
        }
