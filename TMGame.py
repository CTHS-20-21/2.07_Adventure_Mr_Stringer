#Make sure to use comments for documentation of execition flow
#Greet the user
print("Welcome to the dungeon! Available commands are left, right, up, down, grad and fight. ")

#Variables
done = False
debug = True
floor1 = ['empty', 'sword', 'stairs up', 'monster', 'empty']
floor2 = ['magic stones', 'monster','stairs down','empty','stairs up']
floor3 = ['prize', 'boss monster','sword','sword','stairs down']
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
  
  if player_floor == 1:
    floor = floor1
  elif player_floor == 2:
    floor = floor2
  else:
    floor = floor3
  room = floor[player_position - 1]
  if debug:
    print(room)
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
    # move left
    pass
  elif action == 'right':
    # move right
    pass
  elif action == 'up':
    # move up
    pass
  elif action == 'down':
    # move down
    pass
  elif action == 'grab':
    # grab items
    pass
  elif action == 'fight':
    # fight the monster
    pass
  elif action == 'exit':
    done = True
  else:
    print('Command not recognized. Type "help" to see all commands')


if gamestate == 'won':
  print('You won the game!')
  done = True
else:
  print('Sorry, you lost the game.  Better luck next time.')



