#Make sure to use comments for documentation of execition flow
#Greet the user
print("Welcome to the dungeon! Available commands are left, right, up, down, grab and fight. ")

#Variables
done = False
debug = False
floormain = [['empty', 'sword', 'stairs up', 'monster', 'empty'],['magic stones', 'monster','stairs down','empty','stairs up'],['prize', 'boss monster','sword','sword','stairs down']]
inventory = []
danger = 0
#3 floors and 5 rooms
#Start the user at the beginning
player_floor = 1
player_position = 1
#and set if the game of won
gamestate = 'lost'

#Start the turns
while done == False:
  if debug:
    print(player_floor,":",player_position)
    print(done)
  floorindex = player_floor - 1
  floor = floormain[floorindex]
  roomindex = player_position - 1
  room = floor[roomindex]
  if debug:
    print(floorindex,", ",roomindex)
    print(room)
    print(inventory)
    print(floor)
  print()
  #now print room and options
  if room == 'empty':
    print('You are in an empty room.')
  elif room == 'sword':
    print('You see a sword in the room.')
  elif room == 'stairs up':
    print('You see stairs leading up.')
  elif room == 'monster':
    print('There is a monster in the room!')
    danger = 1
  elif room == 'magic stones':
    print('You see magic stones in the room.')
  elif room == 'stairs down':
    print('You see stairs leading down.')
  elif room == 'boss monster':
    print('You see a huge and vaporial monster in the room.  I hope you have more than a sword.')
    danger = 2
  else:
    print("You see the prize!")
    done = True
  
  #get user choice
  action = input('Command? ')

  #Now execute the user's command and hide exit
  if action == 'help':
    print("You can type 'help', 'left', 'right', 'up', 'down', 'grab', or 'fight'")
    
  elif action == 'left':
    # move left - playerpostion + 1
    if player_position == 1:
      print("You cannot move that way.")
    elif danger > 0:
      print("You need to fight the monster.")
    else:
      player_position -= 1
  elif action == 'right':
    # move right
    if player_position == 5:
      print("You cannot move that way.")
    elif danger > 0:
      print("You need to fight the monster.")
    else:
      player_position += 1
  elif action == 'up':
    if room != 'stairs up':
      print("You cannot move that way.")
    elif danger > 0:
      print("You need to fight the monster.")
    else:
      # move up
      player_floor += 1
  elif action == 'down':
    if room != 'stairs down':
      print("You cannot move that way.")
    elif danger > 0:
      print("You need to fight the monster.")
    else:
      # move down
      player_floor -= 1
    
  elif action == 'grab':
    if room != 'magic stones' and room != 'sword' and room != 'prize':
      print('There is nothing to grab in this room.')
    if danger > 1:
      print('The monster eats your arm and you die.')
      done = True
    # grab items
    else:
      #do they already have it?
      if room in inventory:
        print("You already have one of those.")
      #are they in the prize room?
      elif room == 'prize':
        print('You grab the prize and are teleported to the command line.')
        gamestate = 'won'
        Done = True
      else:
        # add to inventory
        inventory.append(room)
        # and remove from room
        floormain[floorindex][roomindex]='empty'
      
  elif action == 'fight':
    if room != 'monster' and room != 'boss monster':
      print("You do not see a monster.  Are you fighting the air?")
    elif room == 'monster':
      if "sword" in inventory:
      # fight the monster
        print('You defeated the monster!')
        floormain[floorindex][roomindex] = 'empty'
        danger = 0
      else:
        print('You swing your fist at the monster and it tears your arm off.')
        done = True
    else:
      #fight the boss monster - do you have the stones and sword?
      if "magic stones" in inventory:
        if "sword" in inventory:
          print("Holding the stones up, the monster solidifies and your sword kills it.")
          floormain[floorindex][roomindex] = 'empty'
          danger = 0
      else:
        print("you swing at the boss monster and your sword pass through its body with no damage off.  It eats your head.")
        done = True
  elif action == 'exit':
    done = True
  else:
    print('Command not recognized. Type "help" to see all commands')
  
  #now let's check for



if gamestate == 'won':
  print('You won the game!')
  done = True
else:
  print('Sorry, you lost the game.  Better luck next time.')



