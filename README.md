# Soluciones de los boletines de la Unidad 2

## Básico

### Ejercicio 1
`Ej1.py` lanza de forma síncrona el comando `ls -lrtha ..` con `subprocess.run`, capturando la salida estándar y la de error como texto para comprobar cómo se ejecuta un proceso externo y se recoge su resultado.

### Ejercicio 2
`Ej3.py` ejecuta `hostname` con `subprocess.run` y muestra el código de salida y el nombre de la máquina obtenido de la salida estándar.

### Ejercicio 3
`Ej3.py` lanza la calculadora de GNOME de forma asíncrona con `subprocess.Popen`, muestra su PID, espera 2 segundos y la cierra con `terminate()`, que envía la señal `SIGTERM`.

### Ejercicio 4
`Ej4.py` muestra el PID del propio proceso Python mediante `os.getpid()`, para poder compararlo con los PID de los procesos que se lanzan en los demás ejercicios.

### Ejercicio 5
`Ej5.py` ejecuta `python --version` con `subprocess.run`, captura la salida y muestra el código de salida junto con la versión del intérprete.

### Ejercicio 6
`Ej6.py` lanza el editor de texto de GNOME con `subprocess.Popen`, muestra su PID, espera 3 segundos y, solo si el proceso sigue en ejecución (`poll()` devuelve `None`), lo termina con `terminate()`. Si ya había una instancia abierta, el proceso lanzado termina de inmediato y no se le envía la señal.

### Ejercicio 7
El orden del ciclo de vida de un proceso es:
1. NUEVO
2. LISTO
3. EJECUCIÓN
4. BLOQUEADO
5. LISTO
6. EJECUCIÓN
7. TERMINADO

### Ejercicio 8
`Ej8.py` ejecuta `ping -c 3 8.8.8.88` con un tiempo máximo de 3 segundos usando el parámetro `timeout` de `subprocess.run`. Si el comando no termina a tiempo, se captura la excepción `subprocess.TimeoutExpired` y se muestra el tiempo transcurrido.
