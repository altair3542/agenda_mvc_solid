# SRP: sólo gestiona la presentación e interacción con el usuario
class Consola:
    @staticmethod
    def mostrar_menu():
        print("\n--- Agenda MVC SOLID ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Editar una tarea")
        print("5. Eliminar una tarea")
        print("0. salir")

    @staticmethod
    def solicitar_datos_crear():
        titulo = input("Titulo: ")
        descripcion = input("Descripcion: ")
        return titulo, descripcion

    @staticmethod
    def solicitar_indice():
        return int(input("Numero de la tarea: ")) -1

    @staticmethod
    def mostrar_tareas(lista):
        if not lista:
            print("- No hay ni una mondá -")
        for i, t in enumerate(lista, 1):
            estado ="🆗" if t["completada"] else ""
            print(f"{i}. [{estado}] {t['titulo']}: {t['descripcion']}")

    @staticmethod
    def notificar(msj):
        print(msj)
