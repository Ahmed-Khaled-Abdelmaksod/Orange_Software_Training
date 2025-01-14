from Observer.observer import Observer
import random
# Player and Enemy classes
class Character(Observer):
    def __init__(self, name, health, attack_strategy):
        self.name = name
        self.health = health
        self.attack_strategy = attack_strategy

    def attack(self):
        damage = self.attack_strategy.execute_attack()
        print(f"{self.name} attacks with {damage} damage!")
        return damage

    def defend(self, damage):
        reduced_damage = damage // 2
        self.health -= reduced_damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} defends! Damage reduced to {reduced_damage}. Health is now {self.health}.")

    def dodge(self):
        success = random.random() < 0.5
        if success:
            print(f"{self.name} dodges successfully!")
        else:
            print(f"{self.name} fails to dodge and takes full damage.")
        return success

    def update(self, action):
        print(f"{self.name} sees the enemy's action: {action}")

