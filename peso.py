from colorama import Fore, Style
nome = input('Qual seu nome? ')
peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é: {imc:.1f}')
if imc < 18.5:
    print(Fore.RED + f'{nome} está abaixo do peso. Precisa comer mais.' + Style.RESET_ALL)
elif 18.5 <= imc < 25:
    print(Fore.GREEN + f'Parabéns, {nome}. Você está no peso ideal!' + Style.RESET_ALL)
elif 25 <= imc < 30:
    print(Fore.YELLOW + f'Você está com sobrepeso, {nome}. Coma menos!' + Style.RESET_ALL)
elif 30 <= imc < 40:
    print(Fore.YELLOW + f'Você está obeso, {nome}.' + Style.RESET_ALL)
elif imc >= 40:
    print(Fore.RED + f'Você está com OBESIDADE MÓRBIDA, {nome}. Por favor, procure um médico!' + Style.RESET_ALL)
