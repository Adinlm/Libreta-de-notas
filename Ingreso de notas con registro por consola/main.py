"""
Proyecto Python y Mysql
-Abrir asistente
-Login o registro
-si elige registro, crea usuario en la BD
-si elige login, identifica el usuario y preguntara
-crea nota, muestra nota, borra nota
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("¿Que desea hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
