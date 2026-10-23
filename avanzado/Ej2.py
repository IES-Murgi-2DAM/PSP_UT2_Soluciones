import subprocess

if __name__ == "__main__":
    proceso = subprocess.run(["which", "python"])
    if proceso.returncode == 0:
        print("Python está instalado en el sistema.")
    else:
        print("Python no está instalado en el sistema.")