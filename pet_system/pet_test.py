from Pet import Pet

def main():
    my_pet = Pet()

    name        = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age         = int(input("Enter your pet's age: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)