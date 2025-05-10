# Assignment 1: Simple AnimeCharacter Class
class AnimeCharacter:
    name = "Goku"
    anime = "Dragon Ball Z"
    power = "Super Saiyan"
    
    # Methods/behaviours
    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.anime}!")
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")
    
    def train(self):
        print(f"{self.name} is training to get stronger!")

# Create an instance of AnimeCharacter
my_character = AnimeCharacter()

# Call the methods
my_character.introduce()
my_character.use_power()
my_character.train()

# Access the attributes
print(f"Character name: {my_character.name}")
print(f"From anime: {my_character.anime}")
print(f"Special power: {my_character.power}")

# Create a custom character by changing attributes
custom_character = AnimeCharacter()
custom_character.name = "Naruto"
custom_character.anime = "Naruto"
custom_character.power = "Rasengan"

# Use the custom character
print("\nCustom character:")
custom_character.introduce()
custom_character.use_power()


# Assignment 2: Simple Polymorphism with Anime Characters
class Ninja:
    def move(self):
        return "The ninja moves silently through the shadows!"
    
class Saiyan:
    def move(self):
        return "The saiyan flies through the air at high speed!"
    
class MagicalGirl:
    def move(self):
        return "The magical girl leaps gracefully leaving sparkles!"

# Polymorphism in action
print("\nPolymorphism demonstration:")
for character in [Ninja(), Saiyan(), MagicalGirl()]:
    print(character.move())