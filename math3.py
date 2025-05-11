num = int(input('Write a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analyzing the number: {num}')
print(f'Unidade is: {u}')
print(f'Dezena is: {d}')
print(f'Centena is: {c}')
print(f'Milhar is: {m}')