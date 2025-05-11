nome = str(input("Whats your name? "))
if nome == 'Ana Carolina':
    print("That pretty name!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Your name is very popular in Brazil.")
elif nome in 'Faye Yoko Engfa Charlotte Rebecca Freen':
    print("Seu nome é um das mais famosas da Tailândia")
else:
   print("Your name is normal.")
print(f"Have a good day {nome}")