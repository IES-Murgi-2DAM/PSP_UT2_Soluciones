import subprocess
import time

if __name__ == "__main__":
    programas = ["gnome-text-editor", "gnome-calculator", "pinta"]
    procesos = [subprocess.Popen(programa) for programa in programas]
    for index, proceso in enumerate(procesos):
        print(f"El PID del proceso {programas[index]} es: {proceso.pid}")

    time.sleep(5)
    for proceso in procesos:
        proceso.terminate()
        print(f"El proceso con PID {proceso.pid} ha sido terminado.")
