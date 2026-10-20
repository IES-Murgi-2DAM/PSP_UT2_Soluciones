import subprocess
import time

if __name__ == "__main__":
    # Voy a abrir la calculadora de Gnome
    proceso = subprocess.Popen(["gnome-calculator"])
    print(f"El PID es: {proceso.pid}")
    # Duermo 2 segundos para que el usuario vea la calculadora abierta
    time.sleep(2)
    # Voy a cerrar la calculadora
    proceso.terminate()
