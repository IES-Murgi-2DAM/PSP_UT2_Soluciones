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

## Avanzado

### Ejercicio 1
`Ej1.py` ejecuta `ip addr` con `subprocess.run`, captura toda la salida como texto y la divide con `split("\n")` para mostrar únicamente las líneas que contienen `inet `, es decir, las direcciones IP de las interfaces.

### Ejercicio 2
`Ej2.py` ejecuta `which python` con `subprocess.run` y comprueba el código de retorno: si es `0`, informa de que Python está instalado y accesible desde la terminal; en caso contrario, indica que no se ha encontrado.

### Ejercicio 3
`Ej3.py` abre el navegador predeterminado del sistema con `subprocess.Popen` mediante `xdg-open https://localhost:4321`, sin bloquear el programa principal.

### Ejercicio 4
`Ej4.py` lanza tres programas a la vez (`gnome-text-editor`, `gnome-calculator` y `pinta`) con una comprensión de listas de `subprocess.Popen`, muestra el PID de cada uno, espera 5 segundos con `time.sleep()` y los termina todos con `terminate()`.

### Ejercicio 5
`Ej5.py` ejecuta `ping 8.8.8.8 -c 5` con `subprocess.run` capturando la salida como texto, y usa una expresión generadora para mostrar solo las líneas que contienen `time=` o `tiempo=`, que son las que incluyen el tiempo de respuesta.

### Ejercicio 6
`Ej6.py` muestra el PID del propio proceso con `os.getpid()` y el PID del proceso padre con `os.getppid()`, para poder compararlos con los procesos lanzados en los demás ejercicios.

### Ejercicio 7
`Ej7.py` crea un proceso hijo con `subprocess.Popen` que ejecuta `python -c "print(input().upper())"`, con `stdin` y `stdout` conectados por tuberías y `text=True`. Después envía el texto y recoge la respuesta con `communicate(input=...)`, comprobando la comunicación en las dos direcciones.

### Ejercicio 8
`Ej8.py` ejecuta `ping -c 3 1.2.3.4` con un `timeout` de 3 segundos y un máximo de 3 intentos (`MAX_INTENTOS`). El bucle `while` se controla con la condición, sin `break`, y captura `subprocess.TimeoutExpired` en cada intento. Si se agotan los intentos, lanza la excepción personalizada `TimeoutException`. El archivo incluye además, comentada, una versión equivalente con `for` y `else` para comparar ambas estructuras.

### Ejercicio 9
`Ej9.py` lanza `gnome-calculator` con `subprocess.Popen` y lo monitoriza en un bucle `while proceso.poll() is None`, comprobando cada segundo con `time.sleep(1)` si el proceso sigue vivo. Al cerrarse, muestra el código de salida obtenido de `returncode`.
