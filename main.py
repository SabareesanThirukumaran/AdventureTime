import os, random, time, sys
import colorama
from colorama import Style, Fore, Back
colorama.init(autoreset=True)

randomchoices = ['A deadly lion waits for you, suddenly your dead...', 'You walk into a pit of lava, bye bye...', 'Your life flashes before your eyes as a toxic gas is poured into your lungs...', 'DIE!']

name = str(input("What is your name traveller?:\n >> "))

def ellipsis():
  y = 0
  t = "...\n"
  while y <= len(t):
    os.system("clear")
    print(t[:y])
    time.sleep(0.2)
    y = y + 1
  time.sleep(0.5)


def victory():
  print("-----------------")
  print("----YOU WON!-----")
  print("-----------------")
  print(" ")
  time.sleep(1)
  
  print(Style.DIM + "Press 'Enter' to view your reward")
  victory = str(input())
  if victory == "":
    prizes = ["Mr Beast wrapped Tesla", "Rick Roll", "Shrek"]
    prize = random.choice(prizes)
    print(f"You won {prize}!")

def lose():
  print("--------------")
  print("---YOU LOST!--")
  print("--------------")
  time.sleep(2)
  
def battle():
  os.system("clear")
  time.sleep(0.5)
  fighter = "Suddenly, a fearsome fighter jumps out from the darkness... "
  for characters3 in fighter:
    time.sleep(0.1)
    sys.stdout.write(characters3)
    sys.stdout.flush()
  time.sleep(0.5)
  print(Style.DIM + "Press 'Enter' to continue", end = " ")
  pause10 = str(input())
  if pause10 == "":
    os.system("clear")
    print(" ")
    who = "Who are you ?"
    for characters4 in who:
      time.sleep(0.1)
      sys.stdout.write(characters4)
      sys.stdout.flush()
    time.sleep(2)
    print(f"{'I am your demise' : >305}", end = "")
    print(" " + name + "!")
    time.sleep(2)
    print(" ")
    fight_start = "If you are, then lets fight!"
    for characters5 in fight_start:
      time.sleep(0.1)
      sys.stdout.write(characters5)
      sys.stdout.flush()
    time.sleep(2)
    print(" ")
    print(f'{"Lets do this thing!" : >320}')
    time.sleep(2)
    os.system("clear") 
    
    critchance = random.randint(0,10)
    crit = 2
    defended = random.randint(0,6)
    maxhealth= 60
    bhealthmax = 50
    
    def menu():
	    print("Your Health: {}".format(hp))
	    time.sleep(1)
	    print("Enemy Health: {}".format(bosshp))
	    time.sleep(1)
	    print("\n[Attack] - Damages the enemy.\n[Defend] - Chance to block enemies attack.\n[Heal] - Regain some of your health.\n\n")
    
    def attack():
    	os.system("clear")
    	time.sleep(.2)
    	print("You attack the enemy. \n")
    	critdmg = 1
    	time.sleep(1)
    	if critchance == 10:
    		critdmg = damagedealt * crit
    	print("You dealt {} damage.\n".format(damagedealt * critdmg))
    	return damagedealt * critdmg
    
    def defend():
    	os.system("clear")
    	time.sleep(.2) #but its fun tbf ya, when we stRting big boi
    	print("You prepare your defences. \n")

    def heal():
    	os.system("clear")
    	time.sleep(.2)
    	print("You wrap yourself in bandages. \n")
    	time.sleep(1)
    	print("You gained {} health. \n".format(plushp))
    
    def battack():
    	os.system("clear")
    	time.sleep(.2)
    	print("The Boss attacks you. \n")
    	time.sleep(1)
    	if prompt == "DEFEND":
    			print("You deflected the attack. \n")
    	else:
    		print("You take {} damage. \n".format(damagetaken))
    
    def bdefend():
    	os.system("clear")
    	time.sleep(.2)
    	if prompt == "ATTACK":
    			print("The Boss deflected your attack. \n")
    	else:
    		print("The Boss tried to deflect you attack...\n")
    		time.sleep(1)
    		os.system("clear")
    		print("... but it failed")
    
    def bheal():
    	os.system("clear")
    	time.sleep(.2)
    	print("The Boss regained {} health. \n".format(plusbhp))
    
    play = True
    hp = 25
    bosshp = 15
    while play == True:
    	bturn = random.randint(1,6)
    	damagedealt = random.randint(2,10)
    	plushp = random.randint(5,12)
    	plusbhp = random.randint(3,7)
    	damagetaken = random.randint(1,8)
    	if hp > 0 or bosshp > 0:
    		if hp > 0:
    			menu()
    			prompt = input().upper()
    			if prompt == "ATTACK":
    				if bturn != 5:
    					bosshp = bosshp - attack()
    				time.sleep(1)
    			elif prompt == "DEFEND":
    				defend()
    				time.sleep(1)
    			elif prompt == "HEAL":
    				os.system("clear")
    				heal()
    				hp = hp + plushp
    				if hp > maxhealth:
    					hp = maxhealth
    				time.sleep(1)
    		else:
    			break
    
    		if bosshp > 0:
    			if bturn < 5:
    				battack()
    				if prompt != "DEFEND":
    					hp = hp - damagetaken
    				time.sleep(1)
    				os.system("clear")
    			elif bturn == 5:
    				bdefend()
    				time.sleep(1)
    			elif bturn == 6:
    				bheal()
    				bosshp = bosshp + plusbhp
    				if bosshp > bhealthmax:
    					bosshp = bhealthmax
    				time.sleep(1)
    		else:
    			break
    	else:
    		play = False
    		break
    
    print("Your Health: {}".format(hp))
    print("Enemy Health: {}".format(bosshp))
    if bosshp <= 0:
    	victory()
    elif hp <= 0:
      lose()
      time.sleep(1)
      start()
      
  else:
    os.system("clear")
    error4 = "It SEemS ThERe HAs BeEn A ProBLeM"
    for index4 in error4:
       time.sleep(0.1)
       sys.stdout.write(index4)
       sys.stdout.flush()
    time.sleep(1)
    start()
  
def game():
  time.sleep(0.8)
  time.sleep(1)
  os.system("clear")
  phrase = "You spawn inside a dungeon..."
  for characters in phrase:
    time.sleep(0.1)
    sys.stdout.write(characters)
    sys.stdout.flush()
  print(Style.DIM + '   Press "Enter" to continue.', end = " ")
  pause1 = str(input())
  if pause1 == "":
    os.system("clear")
    phrase1 = "There are three doors, infront of you..."
    for characters1 in phrase1:
      time.sleep(0.1)
      sys.stdout.write(characters1)
      sys.stdout.flush()
    print(" ")
    print("Which one do you choose?")
    print(Style.DIM + "   Pick either 1,2 or 3 to continue.")
    choice = int(input())
    if choice == 1:
      os.system("clear")
      ellipsis()
      time.sleep(0.5)
      os.system("clear")
      print(random.choice(randomchoices))
      time.sleep(2)
      os.system("clear")
      start()
    elif choice == 2:
      os.system("clear")
      ellipsis()
      time.sleep(1)
      os.system("clear")
      print(random.choice(randomchoices))
      time.sleep(2)
      os.system("clear")
      start()
    elif choice == 3:
      os.system("clear")
      ellipsis()
      time.sleep(1)
      os.system("clear")
      survival = "You survived!"
      for character in survival:
        time.sleep(0.1)
        sys.stdout.write(character)
        sys.stdout.flush()
      time.sleep(1)
      print(Style.DIM + " Press 'Enter' to continue", end = " ")
      battle_continue = str(input())
      if battle_continue == "":
        battle() 
      else:
        os.system("clear")
        error = "It SEemS ThERe HAs BeEn A ProBLeM"
        for index in error:
          time.sleep(0.1)
          sys.stdout.write(index)
          sys.stdout.flush()
        time.sleep(1)
        start()
    else:
      os.system("clear")
      error1 = "It SEemS ThERe HAs BeEn A ProBLeM"
      for index1 in error1:
        time.sleep(0.1)
        sys.stdout.write(index1)
        sys.stdout.flush()
      time.sleep(1)
      start()
  else:
    os.system("clear")
    error2 = "It SEemS ThERe HAs BeEn A ProBLeM "
    for index2 in error2:
      time.sleep(0.1)
      sys.stdout.write(index2)
      sys.stdout.flush()
    time.sleep(1)
    start()
        
def start():
  os.system("clear")
  print("                         .               . . ")
  print("✦ 　　 　　　　　　　 　　　　　.　　　　　　　　   ")
  print(". 　　　˚　　　　　　　　　　　　　　    　　. 　 　")
  print(". 　　　　　   　　　　　.　　　   　　　　.　     ")
  print("* .　　　　　 　　　　　　　　　   　　. ✦ 　˚ . ✦")
  print("✦ﾟ　　　　　.　　　　　　　　　　　　　　　.  　　　　　　　　　　　　. ✦")
  print("        .       .  . .                .     .")
  print(" .              .  .WELCOME .              ..")
  print("  . .                                        ")
  print("                         .               . . ")
  print("✦ 　　 　　　　　　　 　　　　　.　　　　　　　　   ")
  print(". 　　　˚　　　　　　　　　　　　　　    　　. 　 　")
  print(". 　　　　　   　　　　　.　　　   　　　　.　     ")
  print("* .　　　　　 　　　　　　　　　   　　. ✦ 　˚ . ✦")
  print("✦ﾟ　　　　　.　　　　　　　　　　　　　　　.  　　　　　　　　　　　　. ✦")
  print("☀️    .     .       ✦       .         .     ")
  print("˚  　　　　　　　　　　　　　.　　　　　　. ✦    　")
  print(", .　　　　　　　　　　　　　.　　　ﾟ　  　　　.　　  　　")
  print("✦ 　　　　　　,　　　　　　　. . 　　　　　　　　　 ")
  print(". 　　　　　　　　.　　　　　　　　　　　　　. ✦ 　 ")
  print(", 　　　　　　　　　　　　. 　　　.　　　　　　　　　")
  print(" ")
  print(Style.DIM + "            Press 'enter' to start")
  start = str(input())
  if start == "":
    time.sleep(1)
  else:
    os.system("clear")
    error3 = "It SEemS ThERe HAs BeEn A ProBLeM "
    for index3 in error3:
      time.sleep(0.1)
      sys.stdout.write(index3)
      sys.stdout.flush()
    time.sleep(1)
    print(" ")
    exit()


def helpmenu():
  os.system('clear')
  print("---------------------------------")
  print("    Welcome to Sabs' Text RPG    ")
  print('---------------------------------')
  print('You will be given a series of choices and situations')
  print('Use commands by typing them when >> pops up.')
  print('Use the commands given to proceed.')
  print("And lasty, Sabs is always better than you.")
  print(' Copyright 2009-2022 © Aydd Inc ')
  print("---------------------------------")
  print(Style.DIM + "write 'Back' to go back", end = " ")
  option = input(">> ")
  if option.lower() == "back":
    titlescreen()
  titleScreenSelect()

def titleScreenSelect():
  print("")
  option = input(">> ")
  if option.lower() == ("play"):
    ellipsis()
    os.system('clear')
    print("Good Luck Traveller, Have Fun.")
    time.sleep(0.8)
    os.system('clear')
    game()
  elif option.lower() == ("help"):
    helpmenu()
  elif option.lower() == ("quit"):
    sys.exit()
  while option.lower() not in ['play','help','quit']:
    print("Please enter a valid option.")
    option = input(">> ")
    if option.lower() == ("play"):
      ellipsis()
      os.system('clear')
      print("Good Luck Traveller, Have Fun.")
      time.sleep(0.8)
      os.system('clear')
      game()
    elif option.lower() == ("help"):
      helpmenu()
    elif option.lower() == ("quit"):
      sys.exit()

def titlescreen():
  start()
  os.system('clear')
  print("---------------------------------")
  print(f"{'            - Play -             ': >30}")
  print(f'{"            - Help -             ": >30}')
  print(f'{"            - Quit -             ": >30}')
  print(f'{" Copyright 2009-2022 © Aydd Inc  ": >30}')
  print("---------------------------------")
  titleScreenSelect()
titlescreen()