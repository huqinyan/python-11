import random

print(set([''.join([chr(random.randint(97,122)) for i in range(6)]) for _ in range(200)]))
