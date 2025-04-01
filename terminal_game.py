import random
import time

def print_slow(text, delay=0.05):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    print_slow("Welcome aboard the starship 'Infinity Quest'!")
    print_slow("You are part of a courageous crew of curious individuals exploring an unknown galaxy.")
    print_slow("Today is a new day filled with adventure, tough choices, and exciting challenges!")
    crew_introduction()
    morning_phase()

def crew_introduction():
    crew = ["Captain Nova", "Lieutenant Vega", "Engineer Orion", "Medic Luna"]
    print_slow("\nYour crew includes:")
    for member in crew:
        print_slow("- " + member)
    print_slow("Together, you set out to uncover the mysteries of space.\n")

def morning_phase():
    print_slow("=== Morning Phase ===")
    print_slow("The ship's systems hum as the sun rises over distant stars.")
    print_slow("As you start your day, you can choose how to begin:")
    print_slow("1. Check the ship's systems and plan the day's route.")
    print_slow("2. Enjoy a hearty breakfast with your crew in the mess hall.")
    
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print_slow("\nYou head to the control room and review navigation charts and system diagnostics.")
        print_slow("The course is set for a mysterious nebula that might hide new worlds.")
    elif choice == '2':
        print_slow("\nYou join your crew in the mess hall, sharing laughter and stories over a delicious meal.")
        print_slow("This boosts everyone's morale for the adventures ahead!")
    else:
        print_slow("Invalid choice. Please try again.")
        morning_phase()
    
    afternoon_phase()

def afternoon_phase():
    print_slow("\n=== Afternoon Phase ===")
    print_slow("After a refreshing morning, the ship glides into an uncharted sector of space.")
    print_slow("A strange signal is detected from a nearby planet.")
    print_slow("Do you:")
    print_slow("1. Set course for the planet to investigate the signal.")
    print_slow("2. Continue exploring the sector from a safe distance.")
    
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print_slow("\nYou decide to land on the planet. The atmosphere shimmers with alien colors.")
        encounter_npc()
    elif choice == '2':
        print_slow("\nYou choose to observe the planet from orbit, gathering data remotely.")
        print_slow("The information might prove useful later, but nothing immediate happens.")
    else:
        print_slow("Invalid choice. Please try again.")
        afternoon_phase()
    
    evening_phase()

def evening_phase():
    print_slow("\n=== Evening Phase ===")
    print_slow("As night falls, your ship drifts into a quiet sector of the galaxy.")
    print_slow("Suddenly, an enemy vessel appears on the radar!")
    print_slow("Prepare for a classic mini-RPG battle!")
    mini_rpg_battle()

def encounter_npc():
    print_slow("\nWhile exploring the planet, you encounter a mysterious local NPC named Zorlax.")
    print_slow("Zorlax appears friendly but his intentions are unclear.")
    print_slow("Do you:")
    print_slow("1. Engage in a conversation to learn about the planet.")
    print_slow("2. Remain cautious and prepare for potential conflict.")
    
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        print_slow("\nZorlax shares secrets about hidden resources and forgotten relics on the planet.")
        print_slow("This valuable knowledge might help your crew in future adventures!")
    elif choice == '2':
        print_slow("\nYour caution pays off as Zorlax reveals himself to be a scout for a rival faction!")
        print_slow("A skirmish ensues, setting the stage for a mini-RPG battle later.")
    else:
        print_slow("Invalid choice. Please try again.")
        encounter_npc()

def mini_rpg_battle():
    player_hp = 100
    enemy_hp = 100

    print_slow("\nBattle Start!")
    print_slow("You engage with the enemy captain of the rival vessel.")
    print_slow("Choose your moves wisely: Attack, Block, or Heal.")
    
    while player_hp > 0 and enemy_hp > 0:
        print_slow(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
        print_slow("Your moves:")
        print_slow("1. Attack")
        print_slow("2. Block")
        print_slow("3. Heal")
        move = input("Choose your move (1/2/3): ")

        enemy_move = random.choice(["Attack", "Block", "Heal"])
        
        # Player's move effects
        if move == '1':
            print_slow("You launch an attack!")
            damage = random.randint(15, 30)
            # If enemy blocks, reduce damage
            if enemy_move == "Block":
                damage = int(damage / 2)
                print_slow("Enemy blocks part of your attack!")
            enemy_hp -= damage
            print_slow(f"You deal {damage} damage to the enemy.")
        elif move == '2':
            print_slow("You raise your defenses to block the enemy's attack.")
        elif move == '3':
            heal_amount = random.randint(10, 20)
            player_hp += heal_amount
            print_slow(f"You heal yourself for {heal_amount} HP.")
        else:
            print_slow("Invalid move. You lose your turn!")
        
        # Enemy's move effects (if enemy is still alive)
        if enemy_hp > 0:
            print_slow(f"Enemy chooses to {enemy_move}!")
            if enemy_move == "Attack":
                damage = random.randint(15, 30)
                if move == '2':  # player blocked
                    damage = int(damage / 2)
                    print_slow("Your block reduces the incoming damage!")
                player_hp -= damage
                print_slow(f"Enemy deals {damage} damage to you.")
            elif enemy_move == "Heal":
                heal_amount = random.randint(10, 20)
                enemy_hp += heal_amount
                print_slow(f"Enemy heals for {heal_amount} HP.")
            elif enemy_move == "Block":
                print_slow("Enemy braces for your next move!")
        
        # Short delay for dramatic effect
        time.sleep(1)
    
    if player_hp <= 0:
        print_slow("\nYour ship's defenses have fallen. You lost the battle!")
    else:
        print_slow("\nVictory! The enemy vessel retreats into the void of space!")
    
    end_game()

def end_game():
    print_slow("\nThe day comes to an end as you return to your ship.")
    print_slow("Reflecting on your choices and battles, you know tomorrow holds new adventures in this vast galaxy.")
    print_slow("Thank you for playing this 'Day in the Life by Pry Uchiha' space adventure!")

if __name__ == "__main__":
    start_game()
