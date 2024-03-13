import time

class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena.lower()  # Convertir la cadena a minúsculas para ignorar diferencias de mayúsculas

    @classmethod
    def esPalindromo(cls, cadena):
        cadena_limpia = cadena.lower()  # Convertir la cadena a minúsculas para ignorar diferencias de mayúsculas
        return cadena_limpia == cadena_limpia[::-1]  # Verificar si la cadena es igual a su inversa

    def test(self): 
        print(self.cadena.upper(), end=": ")  # Imprimir la cadena en mayúsculas para mostrar la palabra original
        return self.esPalindromo(self.cadena)  # Utilizar el método de clase para verificar el palíndromo

    def __del__(self):
        print(f"La palabra: {self.cadena.upper()} ha sido eliminada de la memoria")  # Imprimir un mensaje al eliminar el objeto de la memoria


def preguntar(num):
    while True:
        if num == 1:
            respuesta = input("Introduce la palabra que quieres comprobar si es un palíndromo o no: ")
            if isinstance(respuesta, str):  # Verificar si la entrada es una cadena
                return respuesta
        elif num == 2:
            respuesta = input("¿Cuántas palabras quieres comprobar?: ")
            if respuesta.isdigit():  # Verificar si la entrada es un número
                return int(respuesta)  
        else:
            print("Introduce otra cosa")


def main():
    num_palabras = preguntar(2)  # Solicitar al usuario el número de palabras a verificar
    for _ in range(num_palabras):
        palabra = Palindromo(preguntar(1))  # Solicitar al usuario una palabra
        print(palabra.test())  # Imprimir el resultado de la verificación del palíndromo

    time.sleep(1)  # Esperar un segundo antes de continuar

    print("Además, a modo de ejemplo, mostraremos las siguientes palabras para entender mejor el comportamiento\n")
    
    palabras_ejemplo = ["radar", "sonar", "Arde ya la yedra", "Ardeyalayedra"]
    for palabra_ejemplo in palabras_ejemplo:
        palabra = Palindromo(palabra_ejemplo)  # Crear una instancia de Palindromo para cada palabra de ejemplo
        print(palabra.test())  # Imprimir el resultado de la verificación del palíndromo
        time.sleep(0.5)  # Esperar medio segundo antes de continuar


if __name__ == "__main__":
    main()
