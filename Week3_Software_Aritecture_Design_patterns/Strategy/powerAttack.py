from Strategy.attackStrategy import AttackStrategy
POWER_ATTACK_DAMAGE = 30

class PowerAttack(AttackStrategy):
    def execute_attack(self):
        return POWER_ATTACK_DAMAGE  
