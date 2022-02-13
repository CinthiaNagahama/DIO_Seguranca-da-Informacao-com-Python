import socket
import sys

if __name__ == "__main__":
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    print("Socket criado com sucesso")
  except socket.error as err:
    print("Falha na conexão!\nErro: {}".format(err))
    sys.exit()

  target_host = input("Digite o host ou IP a ser conectado: ")
  target_port = int(input("Digite a porta a ser utilizada: "))

  try:
    s.connect((target_host, target_port))
    print("Cliente TCP conectado com sucesso!")
    s.shutdown(2)
  except socket.error as err:
    print("Falha na conexão com o host {} na porta {}!\nErro: {}".format(target_host, target_port, err))
    sys.exit()
  

  