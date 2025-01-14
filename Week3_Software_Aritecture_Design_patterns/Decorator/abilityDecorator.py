from Observer.charachter import Character
# Base Decorator
class AbilityDecorator(Character):
    def __init__(self, character):
        self.character = character
        self.name = character.name
        self.health = character.health
        self.attack_strategy = character.attack_strategy
