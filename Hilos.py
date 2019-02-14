import threading
import time

candado = threading.Lock()

class ImprimeNumeros(threading.Thread):
    def __init__(self, nombre_hilo, n, espera):
        threading.Thread.__init__(self)
        self.nombre_hilo = nombre_hilo
        self.n = n
        self.espera = espera
    def run(self):
        for i in range(0,self.n):
            candado.acquire()
            print(self.nombre_hilo," valor=",i)
            candado.release()
            time.sleep(self.espera)

hilo1 = ImprimeNumeros("Hilo_A",4,1)
hilo_beta = ImprimeNumeros("Hilo_B",5,2)

hilo1.start()
hilo_beta.start()

hilo1.join()
candado.acquire()
print("Termine")
candado.release()
hilo_beta.join()


