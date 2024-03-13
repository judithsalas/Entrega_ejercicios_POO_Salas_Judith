# Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:

class A: 
    #Clase A con dos métodos: z e y, el método z semplemente devuelve self mientra que el método y toma un argumento y y te devuelve la longtud de t
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 

# Crea una instancia de la clase A
objeto_a = A()

# Imprime la representación de la clase A
print(objeto_a.z())

# Crea una nueva instancia de la clase A
otra_instancia_a = A()

# Comprueba si las dos instancias son el mismo objeto
print(objeto_a is otra_instancia_a)

# Obtener el método 'y' de la instancia 'objeto_a'
metodo_y = objeto_a.y

# Llamar al método 'y' con una tupla vacía
print(metodo_y(()))

# Crear una nueva instancia de la clase A y llamar al método 'y' con una tupla que contiene la clase A
print(A().y((A,)))

# Llamar al método 'y' de la clase A con la instancia 'objeto_a' y una tupla que contiene la clase A y el método 'y'
print(A.y(objeto_a, (A, metodo_y)))

# Llamar al método 'y' de la instancia 'objeto_a' con una tupla que contiene el método 'y', un entero y una cadena
print(objeto_a.y((metodo_y, 1, 'z')))
