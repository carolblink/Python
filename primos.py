tot = 0
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')  # Amarelo para divisores
        tot += 1
    else:
        print('\033[31m', end='')  # Vermelho para não divisores
    print(f'{c}', end=' ')
print(f'\n\033[0mO número {num} foi dividido {tot} vezes.')

if tot == 2:
    print('E por isso, ele é primo.')
else:
    print('Ele não é primo.')
