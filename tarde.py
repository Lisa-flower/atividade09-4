def main():
    nome = ""
    idade = 0
    opcao = 0
    email = ""
    cidade = ""
    profissao = ""
    while True: # é comentarios
        print("\n--- MENU PRINCIPAL ---\n")
        print("1. Cadrastrar usuário.\n")
        print("2. Exibir dados cadrastrados\n")
        print("3. Sair\n")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        opcao = int(input("Escolha uma opção:")) 
    
        if opcao == 1:
            print("\n°°°°°° colocação de dados °°°°°°\n")
            nome = input("\nDigite o Nome:")
            idade = int(input("\nDigite a Idade: "))

            while True: 
                email = input('Digite seu E-mail: ')
                if "@gmail" in email:
                    break
                else: 
                    print("E-mail invalido. Por favor, digite um endereço de E-mail válido.")
            cidade = input("\nDigite a sua Cidade: ")
            profissao = input("\nDigite a sua Profissão: ")

            print("\nDados cadrastrado com sucesso!")
        
        elif opcao == 2:
            if nome == "" and idade == 0:
                print("\nNenhum dado cadrastrado.\n")
            else:
                print ("\n°°°°°°° Dados em cadrastro. °°°°°°")
                print(f"Nome: {nome}")
                print(f"Idade: {idade}")
                print(f"E-mail: {email}")
                print(f"Cidade: {cidade}")
                print(f"Profissão: {profissao}")
                print ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

        elif opcao == 3:
            print("\nEcerramento do sistema...\n")
            break
        
        else:
            print("Opção inválida! Tente novamente.") 
if __name__ == "__main__": 

    main()