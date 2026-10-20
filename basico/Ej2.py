import subprocess

# Voy a ejecutar el comando para sacar con `hostname` el nombre de la máquina donde me estoy ejecutando
resultado = subprocess.run(["hostname"], capture_output=True, text=True)

print("Código de salida:", resultado.returncode)
print("Salida estándar:")
print(resultado.stdout)