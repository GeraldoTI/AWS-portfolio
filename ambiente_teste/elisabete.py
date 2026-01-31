def mostrar_informacoes():
    # Variáveis e atribuição
    nome = "João"
    idade = 25
    altura = 1.75
    estudante = True
    
    # Operações com strings
    concatenacao = nome + " tem " + str(idade) + " anos"
    interpolacao = f"{nome} tem {idade} anos e {altura}m de altura"
    
    # Mostrando os resultados
    print("=== Informações ===")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}")
    print(f"É estudante: {estudante}")
    print(f"\\nConcatenação: {concatenacao}")
    print(f"Interpolação: {interpolacao}")

# Chamando a função
mostrar_informacoes()
