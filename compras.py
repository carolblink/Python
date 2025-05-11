print(f'{" LOJAS CAROL ":=^40}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
from colorama import Fore, Style
print(Fore.BLUE + '[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print(Style.RESET_ALL)  # Reset da cor para evitar efeitos indesejados
opcao = int(input('Qual é a opção? '))
desconto1 = preco - (preco * 10 / 100)
desconto2 = preco - (preco * 5 / 100)
desconto3 = preco + (preco * 20 / 100)
if opcao == 1:
    print(f'Você ganhou um desconto de 10%')
    print(f'O valor R${preco:.2f} com desconto, vai passar a ser de R${desconto1:.2f}')
elif opcao ==2:
    print(f'Você ganhou um desconto de 5%')
    print(f'O valor R${preco:.2f} à vista no cartão com desconto, vai ser de R${desconto2:.2f}')
elif opcao ==3:
    print(f'Sua compra vai ser parcelada em 2x sem juros de R${preco/2:.2f}')
    print(f'O valor vai ser R${preco}')
elif opcao ==4:
    print('Por ser parcelada em mais de 3x, vai ter o acréscimo de 20%')
    print(f'O valor R${preco:.2f} vai passar a ser de R${desconto3} com 20% a mais de juros.')
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')