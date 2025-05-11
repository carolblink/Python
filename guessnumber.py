from random import randint
from time import sleep

pc = randint (0,5)  #Make the machine "THINK"
print('-=-'*20)
print('I will think of number between 0 and 5, try to guess')
print('-=-'*20)
player = int(input('Whats the number that I thought? ')) #Player try to guess
print('Processing...')
sleep(3)
if player == pc:
    print('Congratulations! You are a good guesser.')
else:
    print(f'Sorry, you are wrong. I trought the number {pc} and not {player}. Try again in the next time.')
