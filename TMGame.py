#Dungeon - last update 10/6
#Make sure to use comments for documentation of execition flow
#Greet the user
print("Welcome to the dungeon! Available commands are left, right, up, down, grab and fight. ")

#Variables
#Done tracking
done = False

#set a debug system
debug = True

#3 floors and 5 rooms
floor1 = ['empty', 'sword', 'stairs up', 'monster', 'sword']
floor2 = ['magic stones', 'monster','stairs down','empty','stairs up']
floor3 = ['prize', 'boss monster','sword','sword','stairs down']

#player inventory (don't start with a blank)
inventory = []

#Start the user at the beginning
player_floor = 1
player_position = 1

#and set if the game to start
gamestate = 'lost'

#Start the turns
while done == False:
  
  ### DEBUG CODE
  if debug:
    print(player_floor,":",player_position)
    print(done)
  
  if player_floor == 1:
    floor = floor1
  elif player_floor == 2:
    floor = floor2
  else:
    floor = floor3
  room = floor[player_position - 1]

  #### DEBUG CODE
  if debug:
    print(room)
    print(inventory)
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
  elif room == 'magic stones':
    print('You see magic stones in the room.')
  elif room == 'stairs down':
    print('You see stairs leading down.')
  elif room == 'boss monster':
    print('You see a BIG ugly monster in the room.')
  else:
    print("You see the prize!")
    done = True
  
  #get user choice
  action = input('Command? ')

  #Now execute the user's command
  if action == 'help':
    print("You can type 'help', 'left', 'right', 'up', 'down', 'grab', or 'fight'")
    pass
  elif action == 'left':
    # move left - check for position and warn if at the beginning (1) or end (5)
    if player_position == 1:
      print("You cannot move that way")
    #does the room have a monster?
    elif room == 'monster' or room == 'boss monster':  
      print("The monster does not want to dance and eats you.   Find a better partner.")
      done = True
    else:
      player_position -= 1
  elif action == 'right':
    # move right - check positioon
    if player_position == 5:
      print("You cannot move that way.")
    #check for monster
    elif room == 'monster' or room == 'boss monster':
      print("The monster does not want to dance and eats you.   Find a better partner.")
      done = True
    else:
      player_position += 1
  elif action == 'up':
    # move up - if there's stairs leading up
    if room != "stairs up":
      print("You see no stairs - you cannot move that way")
    #check for monster - man I wish I didn't have to keep repeating the same code...
    elif room == 'monster' or room == 'boss monster':
      print("The monster does not want to dance and eats you.   Find a better partner.")
      done = True
    else:
      player_floor += 1
  elif action == 'down':
    # move down - check for stairs
    if room != "stairs down":
      print("You see no stairs - do you need glasses?")
    #check for monster
    elif room == 'monster' or room == 'boss monster':
      print("The monster does not want to dance and eats you.   Find a better partner.")
      done = True
    else:
      player_floor -= 1
  elif action == 'grab':
    # grab items - is there someting to grab?
    if room == "empty":
      print("You see nothing in the room, and you cannot grab air.  Please do something else")
    #can't grab a monster....
    elif room == 'monster' or room == 'boss monster':
      print("The monster does not want a hug and eats you.   Sorry.")
      done = True
    # do they already have one?
    elif room in inventory:
      print("You already have one of those!")
    else:
      #add to inventory
      inventory.append(room)
      #now clear it from the room (floor#)
      if player_floor == 1:
        floor1[player_position-1] = 'empty'
      elif player_floor == 2:
        floor2[player_position-1] = 'empty'
      else:
        floor3[player_position-1] = 'empty'
  elif action == 'fight':
    # fight the monster
    if room == 'monster':
      #need to have a sword
      if 'sword' in inventory:
        print('You slice the monster in half and it falls to the floor.')
        # remove monster from the room
        if player_floor == 1:
          floor1[player_position-1] = 'empty'
        elif player_floor == 2:
          floor2[player_position-1] = 'empty'
        else:
          floor3[player_position-1] = 'empty'
        #now destroy the sword
        print('The monster has ruined your sword.  You will need to find another one.')
        inventory.remove('sword')
    elif room == 'boss monster':
      #need a sword
      if 'sword' in inventory:
        #and magic stones
        if 'magic stones' in inventory:
          print("The big ugly monster runs at you and your sword grows because of the stones - you stab the monster and kill it.")
          #clear the monster
          if player_floor == 1:
            floor1[player_position-1] = 'empty'
          elif player_floor == 2:
            floor2[player_position-1] = 'empty'
          else:
            floor3[player_position-1] = 'empty'
          #kill the sword
          print('Your sword shrinks into nothing after the fight.... I hope there is not more big ones!')
          inventory.remove('sword')
    else:
      print("You don't see a monster - do you need something for your ADD?")

  elif action == 'exit':
    done = True
  else:
    print('Command not recognized. Type "help" to see all commands')


if gamestate == 'won':
  print('You won the game!')
  done = True
else:
  print('Sorry, you lost the game.  Better luck next time.')



