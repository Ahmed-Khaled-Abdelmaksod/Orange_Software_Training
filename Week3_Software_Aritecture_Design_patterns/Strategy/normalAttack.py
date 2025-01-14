from Strategy.attackStrategy import AttackStrategy

NORMAL_ATTACK_DAMAGE = 20
# Concrete Strategies
class NormalAttack(AttackStrategy):
    def execute_attack(self):
        return NORMAL_ATTACK_DAMAGE  