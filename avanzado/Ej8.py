import subprocess

MAX_INTENTOS = 3

class TimeoutException(Exception):
    pass


# Regla práctica: elige el bucle por su semántica.
#   - for  -> bucle definido: recorre un iterable y se espera consumirlo entero.
#   - while -> bucle indefinido: no sabemos cuántas vueltas dará, solo cuándo parar.
# Reintentar "hasta 3 veces o hasta que funcione" es indefinido y acotado: while.
# Si un for sale antes de tiempo con break, deja de expresar lo que hace el programa.

# Versión equivalente con for. El else se ejecuta solo si el bucle termina sin break,
# así que no es un break encubierto: la salida anticipada queda documentada.
#
# if __name__ == "__main__":
#     try:
#         for intento in range(1, MAX_INTENTOS + 1):
#             print(f"Intento {intento}.")
#             try:
#                 proceso = subprocess.run(
#                     ["ping", "-c", "3", "1.2.3.4"],
#                     capture_output=True,
#                     text=True,
#                     check=False,
#                     timeout=3,
#                 )
#                 print(proceso.stdout)
#                 break
#             except subprocess.TimeoutExpired:
#                 print("El comando no ha terminado en 3 segundos.")
#         else:
#             raise TimeoutException("El proceso ha tardado demasiado tiempo en completarse.")
#     except TimeoutException as e:
#         print(e)

if __name__ == "__main__":
    exito = False
    intento = 0
    try:
        # La condición del while controla la salida: no hace falta break
        while intento < MAX_INTENTOS and not exito:
            intento += 1
            print(f"Intento {intento}.")
            try:
                proceso = subprocess.run(
                    ["ping", "-c", "3", "1.2.3.4"],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=3,
                )
                print(proceso.stdout)
                exito = True
            except subprocess.TimeoutExpired:
                print("El comando no ha terminado en 3 segundos.")
        if not exito:
            raise TimeoutException("El proceso ha tardado demasiado tiempo en completarse.")
    except TimeoutException as e:
        # Imprimo el mensaje de la excepción
        print(e)