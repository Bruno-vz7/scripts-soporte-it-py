import platform
import subprocess

print("=== DIAGNOSTICO DE RED ===")
sitio = input("Ingresa una web para hacer ping: ")

parametro = "-n" if platform.system().lower() == "windows" else "-c"

comando = ["ping", parametro, "4", sitio]

print(f"\nHaciendo ping a {sitio}...\n")
subprocess.run(comando)
print("\n✅ Diagnostico terminado")
