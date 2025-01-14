from Strategy.attackStrategy import AttackStrategy

QUICK_ATTACK_DAMAGE = 5

class QuickAttack(AttackStrategy):
    def execute_attack(self):
        return QUICK_ATTACK_DAMAGE  
