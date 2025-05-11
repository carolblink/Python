from colorama import Fore, Style

print(Fore.CYAN + '-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20 + Style.RESET_ALL)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULOS.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULOS.')