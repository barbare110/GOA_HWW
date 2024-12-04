fav_animals = []
print("Please enter the name of your five fav animals:")

for i in range(5):
    animals = input("Enter animal" + str(i + 1) + ":")
    fav_animals.append(animals)
print("The first animal is:" + fav_animals[0])
print("The last animal:" + fav_animals[-1])

new_animal = input("Enter a new name for second animal:")
fav_animals[1] = new_animal
print("Uodated list of fav animals:" + str(fav_animals))