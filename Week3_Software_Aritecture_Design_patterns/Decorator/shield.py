from Decorator.abilityDecorator import AbilityDecorator


class Shield(AbilityDecorator):
    def defend(self, damage):
        print(f"{self.name} uses a shield!")
        super().defend(damage // 2)  # Further reduce damage by half
