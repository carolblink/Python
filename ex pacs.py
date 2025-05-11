from random import randint
from time import sleep
from colorama import Fore
from colorama import Fore
print('Suas opções:')
print(f'[{Fore.GREEN} 0 {Fore.RESET}] {Fore.GREEN}PEDRA{Fore.RESET}')
print(f'[{Fore.BLUE} 1 {Fore.RESET}] {Fore.BLUE}PAPEL{Fore.RESET}')
print(f'[{Fore.RED} 2 {Fore.RESET}] {Fore.RED}TESOURA{Fore.RESET}')

jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

itens = ('pedra', 'papel', 'tesoura')
pc = randint (0,2)
print(f'Jogador jogou {Fore.MAGENTA}{itens[jogada]}{Fore.RESET}')
print(f'O computador escolheu {Fore.RED}{itens[pc]}{Fore.RESET}')
if jogada ==0 and pc ==0:
    print(f'Empate!')
elif jogada ==0 and pc ==1:
    print(f'O jogador ganhou!')
elif jogada ==0 and pc ==2:
    print(f'O jogador ganhou!')
elif jogada == 1 and pc == 0:
    print(f'O jogador ganhou!')
elif jogada ==1 and pc== 1:
    print('Empate!')
elif jogada ==1 and pc == 2:
    print(f'O computador ganhou!')
elif jogada ==2 and pc ==0:
    print('O computador ganhou!')
elif jogada ==2 and pc==1:
    print('Empate!')
elif jogada == 2 and pc == 1:
    print(f'O computador ganhou!')
elif jogada ==2 and pc ==2:
    print('Empate!')
