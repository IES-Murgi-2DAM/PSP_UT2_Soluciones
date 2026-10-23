import subprocess
import time

if __name__ == "__main__":
    proceso = subprocess.Popen(["gnome-calculator"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    # Lo mantengo preguntando cada segundo si sigue abierto, hasta que se cierre.
    while proceso.poll() is None:
        print("La calculadora sigue abierta...")
        time.sleep(1)

    print("La calculadora se cerró con código de salida:", proceso.returncode)