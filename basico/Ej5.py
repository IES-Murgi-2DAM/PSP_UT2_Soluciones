import subprocess

if __name__ == "__main__":
    # Voy a ejecutar el comando para sacar con `hostname` el nombre de la máquina donde me estoy ejecutando
    resultado = subprocess.run(["python", "--version"], capture_output=True, text=True)

    print("Código de salida:", resultado.returncode)
    print(f"Salida estándar: {resultado.stdout.strip()}")