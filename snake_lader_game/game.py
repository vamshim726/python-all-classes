
import random
player1='jhon'

player2='alice'

def roll_dice():
      dice = random.randint(1,7)
      return dice
# print(dice)

player1_step=0
player2_step=0
c=1
while (player1_step <=100 or player2_step <=100):

      if c%2==0:
            if player1_step>=100:
                  break
            print(f'{player1} turn ')
            input(f'HIt enter to roll')
            player1_step += roll_dice()
            print(f'{player1} step is {player1_step}')

      else:
            if player2_step>=100:
                  break
            print(f'{player2} turn ')
            input(f'HIt enter to roll')
            player2_step += roll_dice()
            print(f'{player2} step is {player2_step}')

      c+=1

if player1_step > player2_step:
      print(f'{player1} won the game')
else:
      print(f'{player2} won the game')



