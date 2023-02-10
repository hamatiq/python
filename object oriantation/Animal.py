import random
class Animal:
    __name = ""
    __animal_type = ""
    __mood = ""
    __mood_list = ["hungry","sleepy","happy"]

    def __init__ (self, name, animal_type):
        self.__name = name
        self.__animal_type = animal_type
        self.__mood = random.choice(self.__mood_list)
        
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def check_mood(self):
        return self.__mood


