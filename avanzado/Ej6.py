import os

if __name__ == "__main__":
    print(f"Mi PID es: {os.getpid()}")
    print(f"El PID de mi padre es: {os.getppid()}")