
# Concrete Decorators
from Decorator.abilityDecorator import AbilityDecorator


class IncreasedAttackPower(AbilityDecorator):
    def attack(self):
        print(f"{self.name} uses increased attack power!")
        return self.character.attack() + 10  # Boost attack by 10
