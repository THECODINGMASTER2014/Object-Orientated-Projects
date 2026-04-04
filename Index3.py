class Parrot:
    species = "Dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Teddy", 15)
woo = Parrot("Mini", 10)

print("Teddy is a {}".format(blu.species))
print("Mini is also a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


