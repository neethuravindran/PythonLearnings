import random

lst = [i for i in range(1, 1000) if i % 5 == 0 and i % 7 == 0]

print(random.sample(lst, 5))

