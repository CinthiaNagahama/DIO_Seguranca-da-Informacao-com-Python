import hashlib

print("\n" + "#" * 25 + "    GERADOR DE HASHES    " + "#" * 25 + "\n")

option = input(""" ESCOLHA O TIPO DE HASH
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    Digite o número do hash a ser gerado: """)

if option == "1":
  res = hashlib.md5(input("Digite o texto do qual será gerado o hash: ").encode("utf-8"))
elif option == "2":
  res = hashlib.sha1(input("Digite o texto do qual será gerado o hash: ").encode("utf-8"))
elif option == "3":
  res = hashlib.sha256(input("Digite o texto do qual será gerado o hash: ").encode("utf-8"))
elif option == "4":
  res = hashlib.sha512(input("Digite o texto do qual será gerado o hash: ").encode("utf-8"))

print("\nHash gerado: " + res.hexdigest())

print("\n" + "#" * 75 + "\n")