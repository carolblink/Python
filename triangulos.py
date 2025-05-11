from colorama import Fore, Style

print(Fore.CYAN + '-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20 + Style.RESET_ALL)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULOS', end='')
    if r1 == r2 and r2 == r3:
        print(' Um triângulo equilátero')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print(' É um triângulo escaleno')
    elif r1 == r2 or r2 == r3:
        print(' É um triângulo isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULOS')
