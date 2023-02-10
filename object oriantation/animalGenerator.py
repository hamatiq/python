import Animal
repeat = True
animals=[]
while (repeat):
    repeat=False
    animal_type = input("What type of animal would you like to create?")
    animal_type = animal_type.strip()
    name = input("What is the animal’s name?")
    name = name.strip()
    animals.append(Animal.Animal(name,animal_type))
    repeat = input("Would you like to add more animals (y/n)?")
    if (repeat == 'y'):
        repeat = True
    else:
        repeat= False

print ("Animal List:")
for x in animals:
    print (x.get_name()+" the "+x.get_animal_type()+" is "+x.check_mood()+".")