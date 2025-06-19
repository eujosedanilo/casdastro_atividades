from sistema_atividades import SistemaAtividades

def menu():
    sistema = SistemaAtividades()

    while True:
        print("\n====== MENU - SISTEMA DE ATIVIDADES ======")
        print("1. Cadastrar nova atividade")
        print("2. Listar atividades")
        print("3. Marcar atividade como concluída")
        print("4. Sair")
        print("==========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sistema.cadastrar_atividade()
        elif opcao == '2':
            sistema.listar_atividades()
        elif opcao == '3':
            sistema.marcar_atividade_concluida()
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()