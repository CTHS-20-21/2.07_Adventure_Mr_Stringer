#Make sure to use comments for documentation of execition flow
#Greet the user
print("Welcome to the dungeon! Available commands are left, right, up, down, grad and fight. ")

#Variables
done = False
#Start the user at the beginning
player_floor = 1
player_position = 1

#Start the turns

while done == False:
  print(player_floor,":",player_position)
  done = True
