import os
import time

def simple_ping():
  target = input("Digite o IP ou o host a ser verificado: ")

  print("\n" + "-" * 60)
  os.system("ping -n 4 {}".format(target))
  print("-" * 60)

def multiple_pings():
  filename = input("Digite o nome do arquivo com os IPs/hosts a serem verificados: ")

  with open(filename) as file:
    dump = file.read().splitlines()

    for target in dump:
      print("\n" + "-" * 60)
      os.system("ping -n 3 {}".format(target))
      print("-" * 60)
      
      time.sleep(5)

if __name__ == "__main__":
  # simple_ping()
  multiple_pings()