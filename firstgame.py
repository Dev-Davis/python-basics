print('Welcome to your new adventure!')
name = input('What is your name? ')
age = int(input('What is your age? '))

health = 10

if age >= 18:
  print('You are old enough to play. ')

  wants_to_play = input('Do you want to play? ').lower()
  if wants_to_play == 'yes':
    print("You are starting with", health, "health")
    print("Let's play!")

    left_or_right = input("First choice... Left or right (left/right)? ")
    if left_or_right == "left":
      ans = input("Nice, you followed the path and reached a lake. Do you swim across or go around (across/around)? ")

      if ans == "around":
        print("You went around and reached the other side of the lake. ")
      elif ans == "across":
        print("You managed to get across, but bitten by a fish and lost 5 health. ")
        # health -= 5

      ans = input("You notice a cabin and a river. Which do you go to (river/house)? ")
      if ans == "house":
        print("You go to the house and are greeted by the owner. He doesn't like you and you lose 5 health.")
        health -= 5

        if health <= 0:
          print("You now have 0 health and you lost the game. ")
        else:
          print("You survived the game.")
      else:
        print("You fell in the river and lost. ")
    else:
      print("Bummer. You died.")

  else:
    print("See ya! ")

else:
  print('You are not quite old enough to play... ') 





