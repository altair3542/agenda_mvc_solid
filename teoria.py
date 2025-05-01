# SRP (principio de responsabilidad unica) cada clase y cada metodo van a tener una unica razon de cambio (unica invocacion, unco resultado, unico comportamiento)

# OPC (open or closed principle) cada clase debe estar abierta a extenderse, nunca a modificarse.

# LSP (Liskov substitution) Subcalses sustituibles por su superclase sin romper el sistema.

# ISP (interface segregation principle): interfaces especificas en vez de interfaces monoliticas.

# DIP (dependency inversion): depender de abstracciones y no de implementaciones concretas.

# Separacion de responsabilidades con cohesion y acoplamiento: garantizar una alta cohesion interna y un bajo acoplamiento entre componentes...

# Explicar cada uno de los principios SOLID y reconocerlos en el código.

# Diseñar la arquitectura MVC aplicando separación de responsabilidades.

# Implementar y extender un ejercicio de Agenda de Tareas con creación, listado, edición y eliminación.

# Inyectar dependencias a través de abstracciones (repo. de tareas), demostrando OCP y DIP.

# Proponer mejoras a la interfaz del repositorio (ISP) y a nuevas implementaciones (p.ej. JSON).

# agenda_mvc_solid/
# ├── modelo/
# │   ├── tarea.py
# │   └── repositorio.py
# ├── vista/
# │   └── consola.py
# ├── controlador/
# │   └── gestor_tareas.py
# └── main.py
