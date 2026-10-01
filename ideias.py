import random

def menu():
    print("\n=== BANCO DE IDEIAS ===")
    print("1. Adicionar nova ideia")
    print("2. Listar todas as ideias")
    print("3. Sortear uma ideia aleatória")
    print("4. Editar uma ideia")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ").strip()

def main():
    ideias = [
        "Criar um bot para o Telegram que envia piadas ruins",
        "Aprender a fazer pão de fermentação natural",
        "Desenvolver um pequeno jogo 2D usando Pygame"
    ]

    while True:
        opcao = menu()

        if opcao == "1":
            nova_ideia = input("\nDigite sua nova ideia: ").strip()
            if nova_ideia:
                ideias.append(nova_ideia)
                print(f"✨ Ideia '{nova_ideia}' adicionada com sucesso!")
            else:
                print("⚠️ Nenhuma ideia foi digitada.")

        elif opcao == "2":
            print("\n--- SUAS IDEIAS ---")
            if not ideias:
                print("Nenhuma ideia cadastrada ainda.")
            else:
                for i, ideia in enumerate(ideias, start=1):
                    print(f"{i}. {ideia}")

        elif opcao == "3":
            if ideias:
                ideia_sorteada = random.choice(ideias)
                print(f"\n💡 Ideia sorteada: **{ideia_sorteada}**")
            else:
                print("\n⚠️ Nenhuma ideia disponível para sortear.")

        elif opcao == "4":
            if not ideias:
                print("\n⚠️ Nenhuma ideia para editar.")
            else:
                print("\n--- SUAS IDEIAS ---")
                for i, ideia in enumerate(ideias, start=1):
                    print(f"{i}. {ideia}")
                
                num_str = input("\nDigite o número da ideia que deseja editar: ").strip()
                if num_str.isdigit():
                    num = int(num_str)
                    if 1 <= num <= len(ideias):
                        novo_texto = input("Digite o novo texto da ideia: ").strip()
                        if novo_texto:
                            ideias[num - 1] = novo_texto
                            print("✏️ Ideia atualizada com sucesso!")
                        else:
                            print("⚠️ O texto não pode ser vazio.")
                    else:
                        print("⚠️ Número inválido.")
                else:
                    print("⚠️ Digite um número válido.")

        elif opcao == "5":
            print("\nAté logo! Continue tendo ótimas ideias. 👋")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()