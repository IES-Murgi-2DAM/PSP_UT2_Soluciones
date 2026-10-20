import subprocess

# Voy a lanzar el comando ls con -lrtha en el directorio padre de donde estoy ejecutando el script
resultado = subprocess.run(["ls", "-lrtha", ".."], capture_output=True, text=True)

if __name__ == "__main__":
    print("Código de salida:", resultado.returncode)
    print("Salida estándar:")
    print(resultado.stdout)