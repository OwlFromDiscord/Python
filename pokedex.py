class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(self.name + " " + self.name)
    def display_details(self):
        print("Entry Number: " + self.entry)
        print("Name: " + self.name)
        print("Type: " + self.types)
        print("Description: " + self.description)
        if self.is_caught == True:
            print(self.name + " has been caught!")
        else:
            print(self.name + " has not been caught yet!")
vibrava = Pokemon(0329, "Vibrava", "Ground & Dragon", "Rather than using its underdeveloped wings for flight, it rubs them together, emitting ultrasonic waves to attack its enemies.", True)
gothita = Pokemon(0574, "Gothita", "Psychic", "This Pokémon is normally very innocent. When it is staring at something invisible, it is unblinking and utterly silent.", False)
sandy_shocks = Pokemon(0989, "Sandy Shocks", "Electric & Ground", "No records exist of this Pokémon being caught. Data is lacking, but the Pokémon’s traits match up with a creature shown in an expedition journal.", True)

sandy_shocks.speak()
sandy_shocks.display_details()

gothita.speak()
gothita.display_details()

vibrava.speak()
vibrava.display_details()