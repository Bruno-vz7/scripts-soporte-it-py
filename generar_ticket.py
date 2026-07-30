import datetime

print("=== SISTEMA DE TICKETS DE SOPORTE ===")

nombre = input("Nombre del usuario: ")
problema = input("Describi el problema: ")
solucion = input("¿Cuál fue la solución?: ")

fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

ticket = f"""
Fecha: {fecha}
Usuario: {nombre}
Problema: {problema}
Solución: {solucion}

"""

with open("tickets.txt", "a", encoding="utf-8") as archivo:
    archivo.write(ticket)

print("\n✅ Ticket guardado en tickets.txt")
