#https://docs.python.org/3/library/random.html

import random

random_integer=random.randint(1,10)
print(random_integer)

random_float=random.random()
print(random_float)

random_float=random.uniform(1,10)
print(random_float)

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))