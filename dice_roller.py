import random
def main():
  dice_sum = 0
  dice_roll =int (input("how many dice you want to roll:  "))
  dice_size = int(input("how many side dice you want to rolll:  "))
  for i in range (0,dice_roll):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print ("You have rolled a", roll,"Critical fail")
    elif roll == dice_size:
      print("You have rolled a", roll,"Critical success")
    else:
      print ("You have rolled a", roll)
  print ("You have rolled a total of", dice_sum)

if __name__== "__main__":
  main()
