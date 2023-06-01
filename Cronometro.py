import threading
import time

def cronometro():
    contador = 0
    while True:
        contador += 1
        print("Tiempo transcurrido:", contador * 5, "segundos")
        time.sleep(5)

# Crear un hilo para el cronómetro
hilo_cronometro = threading.Thread(target=cronometro)

# Iniciar el hilo
hilo_cronometro.start()
