from car import Car
car = Car(2025, "992 GT3 RS")

print("Accelerating:")
for _ in range(5):
    car.accelerate()
    print("Speed:", car.get_speed())

print("\nBraking:")
for _ in range(5):
    car.brake()
    print("Speed:", car.get_speed())