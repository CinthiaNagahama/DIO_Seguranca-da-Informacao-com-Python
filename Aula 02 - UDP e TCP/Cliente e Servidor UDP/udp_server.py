import socket
import sys

if __name__ == "__main__":
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Servidor: Socket criado com sucesso")
  except socket.error as err:
    print("Falha na conexão!\nErro: {}".format(err))
    sys.exit()
  
  host = "localhost"
  port = 5432

  s.bind((host, port))
  
  msg = "\nServidor: Hello, Client"

  while True:
    data, end = s.recvfrom(4096)

    if data:
      print("Servidor enviando mensagem . . . ")
      s.sendto(data + (msg.encode()), end)