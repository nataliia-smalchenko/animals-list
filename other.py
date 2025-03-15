"""
Модуль для роботи із списком тварин. 
Містить класи тварин та додаткові функції для роботи зі списком.
"""
import json

class Animal:
    """..."""
    def __init__(self, age: int, species: str):
        self.age = age
        self.species = species
        self.friends = []

    def age_up(self):
        self.age += 1
        return f"Вік успішно змінено. Поточний вік {self.age}"

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            return f"Друга {friend.get_short_info()} додано до спику друзів"
        return f"Друг {friend.get_short_info()} уже є у списку друзів"

    def get_short_info(self):
        return f"[{self.species}, {self.age}]"

    def __str__(self):
        info = ""
        info += f"Вид: {self.species} \n"
        info += f"Вік: {self.age} \n"
        if len(self.friends) < 1:
            info += "Друзі: -"
        else:
            info += f"Друзі: {self.get_friends_info()}"
        info += "--------------"
        return info

    def get_friends_info(self):
        friends_info = []
        for friend in self.friends:
            friends_info.append(friend.get_short_info())
        return ", ".join(friends_info)

    def to_json(self):
        return {"age": self.age, "species": self.species}


class Pet(Animal):
    def __init__(self, name: str, age: int , species: str, owner_name: str):
        self.name = name
        self.owner = owner_name
        super().__init__(age, species)

    def change_owner(self, new_owner: str):
        self.owner = new_owner
        return f"Власника успішно змінено. Поточний власник {self.owner}"

    def change_name(self, new_name: str):
        """Метод для зміни імені"""
        self.name = new_name
        return f"Імʼя успішно змінено. Поточне імʼя {self.name}"

    def get_short_info(self):
        return f"[{self.name}, {self.species}, {self.age}]"

    def __str__(self):
        info = f"Імʼя: {self.name} \n"
        info += f"Власник: {self.owner} \n"
        info += super().__str__()
        return info

    def to_json(self):
        return {"name": self.name, "age": self.age, "species": self.species, "owner": self.owner}


class Snake(Pet):
    def __init__(self, name: str, age: int, owner_name: str):
        super().__init__(name, age, "Змія", owner_name)

    @classmethod
    def from_json(cls, animal: dict):
        return cls(animal.get("name"), animal.get("age"), animal.get("owner"))


class Cat(Pet):
    def __init__(self, name: str, age: int, owner_name: str):
        super().__init__(name, age, "Кіт", owner_name)

    @classmethod
    def from_json(cls, animal: dict):
        return cls(animal.get("name"), animal.get("age"), animal.get("owner"))


class Dog(Pet):
    def __init__(self, name: str, age: int, owner_name: str):
        super().__init__(name, age, "Пес", owner_name)

    @classmethod
    def from_json(cls, animal: dict):
        return cls(animal.get("name"), animal.get("age"), animal.get("owner"))


class Bird(Pet):
    def __init__(self, name: str, age: int, owner_name: str):
        super().__init__(name, age, "Пташка", owner_name)

    @classmethod
    def from_json(cls, animal: dict):
        return cls(animal.get("name"), animal.get("age"), animal.get("owner"))

def show_menu():
    print("МЕНЮ")
    print("1. Переглянути всіх тварин")
    print("2. Додати нову тварину")
    print("3. Змінити відомості про тварину")
    print("4. Видалити тварину зі списку")
    print("5. Показати меню")
    print("6. Вийти")

def add_animal(animals):
    animal_type = input("Введіть тип тварини (1 - змія, 2 - кіт, 3 - пес, 4 - птах): ").strip()
    name = input("Введіть імʼя тварини: ").strip()
    try:
        age = int(input("Введіть вік тварини: "))
    except ValueError:
        print("Ви ввели не ціле число. Спробуйте ще раз.")
        return
    owner_name = input("Введіть імʼя власника: ")

    match animal_type:
        case "1":
            animals.append(Snake(name, age, owner_name))
        case "2":
            animals.append(Cat(name, age, owner_name))
        case "3":
            animals.append(Dog(name, age, owner_name))
        case "4":
            animals.append(Bird(name, age, owner_name))

def save_animals(animals, filename):
    animals_list = []
    for animal in animals:
        animals_list.append(animal.to_json())

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(animals_list, file, indent=2, ensure_ascii=False)

def load_animals(animals, filename):
    with open(filename, "r", encoding="utf-8") as file:
        animals_list = json.load(file)

    for animal in animals_list:
        species =  animal.get("species")
        match species:
            case "Змія":
                animals.append(Snake.from_json(animal))
            case "Кіт":
                animals.append(Cat.from_json(animal))
            case "Пес":
                animals.append(Dog.from_json(animal))
            case "Пташка":
                animals.append(Bird.from_json(animal))


def main():
    """Головна функція програми"""
    animals = []
    load_animals(animals, "animal2.json")
    # animals.pop(index)

    show_menu()
    while True:
        print()
        answer = input(">>>  ")
        match answer:
            case "1":
                for index, animal in enumerate(animals):
                    print(index)
                    print(animal)
                    print()
            case "2":
                add_animal(animals)
                save_animals(animals, "animal2.json")
            case "3":
                pass
            case "4":
                pass
            case "5":
                show_menu()
            case "6":
                break

if __name__ == "__main__":
    main()
