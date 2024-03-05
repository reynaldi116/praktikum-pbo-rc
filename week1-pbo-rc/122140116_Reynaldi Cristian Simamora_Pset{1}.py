import random
def newline():
  print("\n\n")
class Robot:
  def __init__(self, name, hp, attack, accuracy, heal_power):
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.attack = attack
    self.accuracy = accuracy
    self.heal_power = heal_power

  def receive_damage(self, damage):
    self.hp -= damage
  
  def healing_hp(self):
    heal_amount = random.randint(1, self.heal_power)
    self.hp = min(self.hp + heal_amount, self.max_hp)
    print(f"Robot {self.name} healed for {heal_amount} HP.")

  def is_alive(self):
    return self.hp > 0

  def show_hp(self):
    print(f"Robot {self.name} has {self.hp} hp ")
    
  def robot_attack(self, target):
    if random.random() < self.accuracy :
      damage = random.randint(1, self.attack)
      target.receive_damage(damage)
      print(f"Robot {self.name} attacked {target.name} for {damage} damage.")
    else:
      print(f"Robot {self.name} missed the attack.")

Robot_B = Robot("Megatron", 100, 30, 75/100, 10)
Robot_A = Robot("Autobot", 160, 18, 65/100, 30)

while Robot_A.is_alive() and Robot_B.is_alive():
  print("Choose an action: \t1. Attack enemy \t2. Heal your HP\t3. Give up")
  action = input("Enter your action (1 or 2 or 3) :\n")
  if action == '1':
    Robot_A.robot_attack(Robot_B)
    if Robot_B.is_alive():
        Robot_B.robot_attack(Robot_A)
  elif action == '2':
    Robot_A.healing_hp()
    if Robot_B.is_alive():
      Robot_B.robot_attack(Robot_A)
  elif action == '3':
    print(f"You gave up. Game over.\nThe Winner is {Robot_B.name} !")
    break
  else:
    print(f"Invalid action. Please choose again.")
  Robot_A.show_hp()
  Robot_B.show_hp()
  newline()
if Robot_A.is_alive():
      print(f"You win with your last hp {Robot_A.hp} ! {Robot_A.name} is the winner!")
else:
      print(f"You lose! {Robot_B.name} is the winner with {Robot_B.hp} hp!")
