from modelo.tarea import Tarea
from modelo.repositorio import RepositorioTareas, RepositorioMemoria
from vista.consola import Consola

# SRP: coordina repositorio y vista, controla flujo
class GestorTareas:
    def __init__(self, repo: RepositorioTareas = None):
        # DIP/OCP: se inyecta abstracción, permite cambiar la implementación
        self._repo = repo or RepositorioMemoria()

    def correr(self):
        opcion = None
        while opcion != "0":
            Consola.mostrar_menu()
            opcion = input("Opción: ")
            {
                "1": self._crear,
                "2": self._listar,
                "3": self._completar,
                "4": self._editar,
                "5": self._eliminar
            }.get(opcion, lambda: None)()

    def _crear(self):
        titulo, desc = Consola.solicitar_datos_crear()
        tarea = Tarea(titulo, desc)      # SRP: creación de tarea
        self._repo.agregar(tarea)       # DIP: uso de abstracción
        Consola.notificar("Tarea creada.")

    def _listar(self):
        datos = self._repo.listar()
        Consola.mostrar_tareas(datos)

    def _completar(self):
        self._listar()
        idx = Consola.solicitar_indice()
        try:
            tarea = self._repo.obtener(idx)
            tarea.completar()             # SRP: tarea gestiona su propio estado
            self._repo.actualizar(idx, tarea)
            Consola.notificar("Tarea completada.")
        except (IndexError, ValueError):
            Consola.notificar("Índice inválido.")

    def _editar(self):
        self._listar()
        idx = Consola.solicitar_indice()
        try:
            tarea = self._repo.obtener(idx)
            nuevo_t, nueva_d = Consola.solicitar_datos_crear()
            tarea.editar(nuevo_t, nueva_d)  # SRP: tarea gestiona su edición
            self._repo.actualizar(idx, tarea)
            Consola.notificar("Tarea editada.")
        except (IndexError, ValueError):
            Consola.notificar("Operación inválida.")

    def _eliminar(self):
        self._listar()
        idx = Consola.solicitar_indice()
        try:
            self._repo.eliminar(idx)      # SRP: repositorio gestiona la eliminación
            Consola.notificar("Tarea eliminada.")
        except IndexError:
            Consola.notificar("Índice inválido.")
