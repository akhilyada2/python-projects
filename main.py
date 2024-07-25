print('''                         _
                   /_'. _
                 _   \ / '-.
                < ``-.;),--'`
                 '--. |__
      /-/-/|o|-|\-\\|\\   / | \
       '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\
             |-|                      |"\ |__ ,_) \_, |_| |__ |_/  o  o  o
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
stage_1=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
if stage_1 == "left":
  stage_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat or type 'swim' to swim across")
  if stage_2 == "wait":
    stage_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose?")
    if stage_3 == "red":
      print(f"You enter a room of beasts. Game Over.")
    elif stage_3=="yellow":
      print(f"You found the treasure! You Win!")
    elif stage_3=="blue":
      print(f"You enter a room of beasts. Game Over.")
    else:
      print(f"You chose a door that doesn't exist. Game Over.")
  else:
    print(f"You get attacked by an angry trout. Game Over.")
else:
  print(f"You fell into a hole. Game Over.")

     
