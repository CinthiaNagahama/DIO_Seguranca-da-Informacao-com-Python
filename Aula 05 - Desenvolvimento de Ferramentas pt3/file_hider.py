import ctypes

def hide_file():
  file_path = input("Digite o nome/caminho do arquivo a ser ocultado: ")

  res = ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)

  if res:
    print("Arquivo foi ocultado")
  else:
    print("Arquivo não foi ocultado")

def unhide_file():
  file_path = input("Digite o nome/caminho do arquivo a ser mostrado: ")

  res = ctypes.windll.kernel32.SetFileAttributesW(file_path, 128)

  if res:
    print("Arquivo não está mais oculto")
  else:
    print("Arquivo continua ocultado")

if __name__ == "__main__":
  hide_file()
  # unhide_file()