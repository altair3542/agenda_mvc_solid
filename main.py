from controlador.gestor_tareas import GestorTareas
from modelo.repositorio import RepositorioMemoria

if __name__ == "__main__":
    # DIP: inyectamos la implementación concreta del repositorio
    gestor = GestorTareas(repo=RepositorioMemoria())
    gestor.correr()
