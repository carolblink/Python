from datetime import date
atual = date.today().year
ano_nasc = int(input('Qual ano você nasceu? '))
cal = atual - ano_nasc
if cal <=9:
    print(f'Você tem {cal} anos. E sua categoria é MIRIM.')
elif cal >= 10 and cal <= 14:
    print(f'Você tem {cal} anos. E sua categoria é INFANTIL.')
elif cal >=15 and cal <=19:
    print(f'Você tem {cal} anos. E sua categoria é JUNIOR.')
elif cal >=20 and cal <=25:
    print(f'Você tem {cal} anos. E sua categoria é SÊNIOR.')
elif cal >=25:
    print(f'Você tem {cal} anos. E sua categoria é MASTER.')