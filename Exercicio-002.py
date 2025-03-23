import math

a = 2
b = 2
c = -6

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes reais são: x1 = {x1} e x2 = {x2}")

elif delta == 0:
    x = -b / (2 * a)
    print(f"A única raiz real é: x = {x}")
    