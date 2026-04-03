class Vehicle :

    def __init__(self, name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle("konisegg Jesko Absolut",530,21)

print("Model Name : ",modelX.name)
print("Model Max Speed : ",modelX.max_speed)
print("Model Mile Age : ",modelX.mileage)