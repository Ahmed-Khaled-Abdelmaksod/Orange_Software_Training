from abc import ABC, abstractmethod


# Strategy Interface
class AttackStrategy(ABC):
    @abstractmethod
    def execute_attack(self):
        pass