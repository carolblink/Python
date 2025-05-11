# Solicita o nome completo da pessoa
nome_completo = input("Digite seu nome completo: ")

# Calcula o número de letras ao todo (sem contar espaços)
total_letras = len(nome_completo.replace(" ", ""))

# Divide o nome completo em partes separadas pelo espaço
partes_nome = nome_completo.split()

# Obtém o primeiro nome
primeiro_nome = partes_nome[0]

# Calcula o número de letras no primeiro nome
letras_primeiro_nome = len(primeiro_nome)

# Mostra os resultados
print("Nome completo:", nome_completo)
print("Número total de letras (sem contar espaços):", total_letras)
print("Número de letras no primeiro nome:", letras_primeiro_nome)
