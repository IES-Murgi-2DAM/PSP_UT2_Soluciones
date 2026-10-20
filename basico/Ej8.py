import subprocess
import time

if __name__ == "__main__":
    antes = time.time()
    try:
        proceso = subprocess.run(["ping", "-c", "3", "8.8.8.88"], timeout=3)
    except subprocess.TimeoutExpired:
        print(f"El proceso duró demasiado tiempo. {time.time() - antes}")
