from colorama import Fore, Style

sal = float(input("Qual o seu salário? R$ "))

if sal >= 1250:
    novo_salario = sal + (sal * 10 / 100)
    print(f"{Fore.CYAN}O salário R${sal:.2f} passou a ser de R${novo_salario:.2f} com o aumento.{Style.RESET_ALL}")
else:
    novo_salario = sal + (sal * 15 / 100)
    print(f"{Fore.CYAN}O salário R${sal:.2f} passou a ser de R${novo_salario:.2f} com o aumento.{Style.RESET_ALL}")
