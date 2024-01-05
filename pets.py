dogs = {
    'maya':{
    'breed': 'retriever',
    'food': 'chicken',
    'owner': 'edward'
    },

    'izzy':{
    'breed': 'beagle',
    'food': 'pedigree',
    'owner': 'dan'
    },

    'rex':{
    'breed': 'sheppard',
    'food': 'beef',
    'owner': 'jack'
    },
    
    'blue':{
    'breed': 'husky',
    'food': 'shoes',
    'owner': 'anna'
    }
}

dog_names = ['maya', 'izzy', 'rex', 'blue']

for dog_names, dog_info in dogs.items():
    print(f"\nDog's name: {dog_names.title()}")
    breed = f"{dog_info['breed']}"
    food = f"{dog_info['food']}"
    owner = f"{dog_info['owner']}"

    print(f"\tBreed: {breed.title()}")
    print(f"\tFood: {food.title()}")
    print(f"\tOwner: {owner.title()}")
