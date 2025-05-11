casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100 #Para calcular 30% do salário
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos')
print(f'A prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Parabéns! Seu empréstimo foi aprovado.')
else:
    print('Infelizmente seu empréstimo não foi aprovado.')
