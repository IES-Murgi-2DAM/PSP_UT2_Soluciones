import subprocess

if __name__ == "__main__":
    proceso = subprocess.run(["ip", "addr"], capture_output=True, text=True)
    lineas = proceso.stdout.split("\n")

    for linea in lineas:
        if "inet " in linea:
            print(linea.strip())