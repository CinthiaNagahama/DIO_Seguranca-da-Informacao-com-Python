import itertools
import string

chars = string.ascii_letters + string.digits

res = itertools.permutations(chars, 6)

for i in res:
  print("".join(i))