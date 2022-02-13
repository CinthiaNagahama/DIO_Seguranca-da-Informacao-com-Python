import random
import string

len = int(input("Digite o tamanho da senha que você deseja: "))

chars = string.ascii_letters + string.digits + 'ç!@#$%&()+-/*.,:;?[]\{\}'

rand = random.SystemRandom()

print("Senha gerada: " + "".join(rand.choice(chars) for i in range(len)))