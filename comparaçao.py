###criando uma lista 
#Victor
#Ivan
#fabricio
#Gabriel
#Gustavo
#Rafael
#Tarso

#qual seria o print e
# input para pedir os nomes?
print("*** lista de nome ***\n")

nomes = input("digite os nomes separados por virgula: ").split(", ")

#nomes = [nome.strip() for nome in nomes]

print(nomes)

print("\ nQuais operações voce quer fazer:")
print("1 - Adicionar um nome")
print("2 - Remover um nome")
print("3 - Listar nomes")
print("4 - Sair")

#faça um loop para pedir a opção do usuario 

while True:
    opcao = input("\ndigite a opção desejada (1-4): ")

    if opcao == "1":
        #novo_nome = input("Digite o nome a ser adicionado: ")
        #nomes.append(novo_nome)
        #print(f"{novo_nome} foi adicionado a lista. ")
        print(f" foi aficionado a lista. ")

    elif opcao == "2":
        #nome_remover = imput("Dogote o nome a ser removido:")
        # if nome remover in nomes: 