import socket
import sys

if __name__ == "__main__":
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Cliente: Socket criado com sucesso")
  except socket.error as err:
    print("Falha na conexão!\nErro: {}".format(err))
    sys.exit()

  host = "localhost"
  port = 5433
  msg = "Hello, Server"

  try:
    # print(f"Cliente: {msg}")
    s.sendto(msg.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f"Cliente: {data}")
  except socket.error as err:
    print("Falha na conexão!\nErro: {}".format(err))
    sys.exit() 
  finally:
    print("Cliente: Fechando a conexão")
    s.close()
