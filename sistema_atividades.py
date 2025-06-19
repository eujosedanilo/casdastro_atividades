from atividades import Atividade

class SistemaAtividades:
    def __init__(self):
        self.atividades = []

    def cadastrar_atividade(self):
        print("\n Cadastro de Nova Atividade")
        descricao = input("Descrição: ")
        tipo_atividade = input("Tipo de Atividade: ")
        chamado = input("Código do Chamado (ex: CH1234): ")
        try:
            tempo = float(input("Tempo estimado (em horas): "))
        except ValueError:
            print("Tempo inválido. Use apenas números.")
            return

        nova = Atividade(descricao, tipo_atividade, chamado, tempo)
        self.atividades.append(nova)
        print(f"\n Atividade cadastrada com ID {nova.id}!\n")

    def listar_atividades(self):
        print("\n Lista de Atividades:")
        if not self.atividades:
            print("Nenhuma atividade cadastrada.\n")
            return

        for atividade in self.atividades:
            print(atividade)
            print("-" * 40)

    def marcar_atividade_concluida(self):
        if not self.atividades:
            print("Nenhuma atividade para concluir.\n")
            return

        try:
            id_busca = int(input("Digite o ID da atividade a ser concluída: "))
        except ValueError:
            print("ID inválido.\n")
            return

        for atividade in self.atividades:
            if atividade.id == id_busca:
                atividade.marcar_concluida()
                print(f"Atividade {id_busca} marcada como concluída.\n")
                return

        print(f"Atividade com ID {id_busca} não encontrada.\n")