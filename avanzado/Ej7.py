import subprocess

if __name__ == "__main__":
    proceso = subprocess.Popen(["python", "-c", "print(input().upper())"], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, text=True)
    salida, _ = proceso.communicate(input="hola que te cuentas")
    print(salida)


