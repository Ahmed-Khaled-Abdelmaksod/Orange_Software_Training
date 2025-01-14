
import random
from Decorator.abilityDecorator import AbilityDecorator


class Speed(AbilityDecorator):
    def dodge(self):
        success = random.random() < 0.75
        if success:
            print(f"{self.name} dodges with increased speed successfully!")
        else:
            print(f"{self.name} fails to dodge with speed.")
        return success