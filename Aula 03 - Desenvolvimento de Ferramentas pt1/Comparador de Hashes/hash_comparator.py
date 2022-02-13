import hashlib

file1 = "a.txt"
file2 = "b.txt"

hash_ripemd160_1 = hashlib.new("ripemd160")
hash_ripemd160_1.update(open(file1, "rb").read())
print(f"Hash do {file1}: " + hash_ripemd160_1.hexdigest())


hash_ripemd160_2 = hashlib.new("ripemd160")
hash_ripemd160_2.update(open(file2, "rb").read())
print(f"Hash do {file2}: " + hash_ripemd160_2.hexdigest())

if hash_ripemd160_1.digest() != hash_ripemd160_2.digest():
  print(f"{file1} é diferente de {file2}")
else:
  print(f"Os arquivos {file1} e {file2} são iguais")