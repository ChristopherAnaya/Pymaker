import math
def how_many_pizzas(n):
    pi = math.pi
    eight = 64 * pi
    print((pi * n**2 + 0.0001)//eight, pi * n**2 % eight, int(pi * n**2 % eight/(eight/8) + 0.000000001)%8)
    return f'pizzas: {int((pi * n**2 + 0.0001)//eight)}, slices: {int(pi * n**2 % eight/(eight/8) + 0.000000001)%8}'

print(how_many_pizzas(801472))
#pizzas: 801472, slices: 4