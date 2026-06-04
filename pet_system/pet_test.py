from pet import Pet

def main():
    my_pet = Pet()

    name        = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age         = int(input("Enter your pet's age: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print("\n--- Pet Information ---")
    print("Name:", my_pet.get_name())
    print("Animal Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

main()