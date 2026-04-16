class CnA:

    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

blu = CnA(10, 3.14)

a = blu.pi * blu.radius ** 2
print(a)

p = blu.pi * blu.radius * 2
print(p)