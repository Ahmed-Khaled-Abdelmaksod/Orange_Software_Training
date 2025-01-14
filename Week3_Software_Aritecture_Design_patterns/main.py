from Decorator.increasedAttackPower import IncreasedAttackPower
from Observer.gameState import GameState
from Observer.charachter import Character
from Strategy.normalAttack import NormalAttack
from Strategy.powerAttack import PowerAttack
from Strategy.quickAttack import QuickAttack
import random

from Decorator.shield import Shield
from Decorator.speed import Speed

def get_player_choice():
    temp = ['attack', 'defend', 'dodge']
    
    while True:
        print("It's your turn :)")
        print("1. Attack")
        print("2. Defence")
        print("3. Dodge")
        
        try:
            choice = int(input("Choose one option: "))
            if 1 <= choice <= 3:
                return temp[choice - 1]
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# GameState instance
game_state = GameState()

# Initialize player and enemy
player = Character("Player", 100, NormalAttack())
enemy = Character("Enemy", 100, QuickAttack())

# Add them as observers to the game state
game_state.add_observer(player)
game_state.add_observer(enemy)

turn_count = 0 # to indicate the number of the current turn

while player.health > 0 and enemy.health > 0:
    turn_count += 1
    print(f"\nTurn {turn_count}:")
    
    # Player chooses an action
    
    player_action = get_player_choice()
    enemy_action = random.choice(['attack', 'defend', 'dodge'])

    # Notify actions
    game_state.notify_observers(f"Player chose {player_action}, Enemy chose {enemy_action}")

    # Player's action
    if player_action == 'attack':
        damage = player.attack()
        if enemy_action == 'defend':
            enemy.defend(damage)
        elif enemy_action == 'dodge':
            if not enemy.dodge():
                enemy.health -= damage
        else:
            enemy.health -= damage

    # Enemy's action
    if enemy_action == 'attack':
        damage = enemy.attack()
        if player_action == 'defend':
            player.defend(damage)
        elif player_action == 'dodge':
            if not player.dodge():
                player.health -= damage
        else:
            player.health -= damage
    
    # Every two turns, randomly grant an ability to the player
    if turn_count % 2 == 0:
        random_ability = random.choice([IncreasedAttackPower, Shield, Speed])
        player = random_ability(player)
        print(f"{player.name} gains a temporary ability: {random_ability.__name__}")
    if player.health < 0:
        player.health = 0
    if enemy.health < 0:
        enemy.health = 0
    print(f"Player Health: {player.health}, Enemy Health: {enemy.health}")
    print("-"*50)

if player.health <= 0:
    print("Enemy wins!")
elif enemy.health <= 0:
    print("Player wins!")
