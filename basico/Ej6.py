import os
import subprocess
import time

if __name__ == "__main__":
    proceso = subprocess.Popen(["gnome-text-editor"])
    print(f"El PID es: {proceso.pid}")
    time.sleep(3)
    if proceso.poll() is None:
        proceso.terminate()