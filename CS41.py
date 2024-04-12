import math
# Q = Square root of [(2 * C * D)/H]
# C is 50. H is 30

numbers = input("Input D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)