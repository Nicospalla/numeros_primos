'''
Nicolas Spalla
NicolasASpalla@gmail.com
'''

from math import sqrt
class Main():
    def __init__(self):
        self.numero_primo()

    def numero_primo(self):
        valor = input("Ingrese el numero que desea conocer si es o no Primo: ")
        valor = int(valor)
        n = 2
        bandera = False
        while valor % n != 0 or n > valor:
            n += 1
            if n == valor:
                bandera = True
                break
        if bandera == False:
            print("El numero No es primo")
        elif bandera == True:
            print("El numero es primo")
            

if __name__ == "__main__":
    f = Main()