# El problema consiste en un tragamonedas, los valores al azar son números hasta 10, se gana cuando los 3 valores del tragamonedas son iguales, el premio se calcula como la cantidad de monedas apostadas multiplicada por el valor generado por el tragamonedas.

import random

class NoHayMonedasParaPremioException(Exception):
    pass

class NoHayMonedaException(Exception):
    pass

class Tragamonedas:
    def __init__(self):
        self.monedas = 1000 
        self.monedas_tirada = 0 

    def insertar_moneda(self):
        if 10 > self.monedas - self.monedas_tirada * 10:
            raise NoHayMonedasParaPremioException()
        self.monedas_tirada += 1
        self.monedas += 1

    def tirar(self):
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
        aleatorio1 = random.randint(1, 10)
        aleatorio2 = random.randint(1, 10)
        aleatorio3 = random.randint(1, 10)
        if aleatorio1 == aleatorio2 == aleatorio3:
            premio = self.monedas_tirada * aleatorio1
        else:
            premio = 0
        self.monedas -= premio
        self.monedas_tirada = 0
        return premio
