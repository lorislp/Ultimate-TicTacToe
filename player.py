class Player:
    def __init__(self, name, letter, value):
        self.name = name
        self.letter = letter
        self.value = value
        print(f"{self.name} plays letter {self.letter}")
