import subprocess

if __name__ == "__main__":
    proceso = subprocess.run(["ping", "8.8.8.8", "-c", "5"], capture_output=True, text=True)
    filtrados = (linea for linea in proceso.stdout.split("\n") if "time=" in linea or "tiempo=" in linea)
    for linea in filtrados:
        print(linea.strip())