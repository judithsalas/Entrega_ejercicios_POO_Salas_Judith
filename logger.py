class Logger:
    def __init__(self, filename="log.txt"):
        self.filename = filename  # Nombre del archivo de registro
        self.count = 0  # Inicializa el contador de registros
        self._start_log()  # Inicia el registro escribiendo el mensaje de inicio

    def _start_log(self):
        # Abre el archivo en modo escritura y escribe el mensaje de inicio
        with open(self.filename, "w") as file:
            file.write("--Start log--\n")

    def log(self, message):
        self.count += 1  # Incrementa el contador de registros
        # Abre el archivo en modo de adición y escribe el mensaje de registro
        with open(self.filename, "a") as file:
            file.write(message + "\n")

    def __del__(self):
        # Al destruir la instancia, escribe el mensaje de finalización con el recuento de registros
        with open(self.filename, "a") as file:
            file.write(f"--End log: {self.count} log(s)--\n")


class Test:
    def __init__(self):
        # Inicializa una instancia de la clase Logger para el registro
        self.logger = Logger()

    def llamada(self, mensaje):
        # Llama al método log del Logger para registrar un mensaje
        self.logger.log(mensaje)


# Uso de la clase Test
test = Test()
for i in range(1, 6):
    # Realiza algunas llamadas para registrar mensajes
    # Si es la primera llamada, registra "Primera llamada", de lo contrario, registra el número de llamada
    test.llamada("Primera llamada" if i == 1 else f"{i}ª llamada")

# Verificación del archivo de registro (log.txt)
with open("log.txt", "r") as file:
    print(file.read())
