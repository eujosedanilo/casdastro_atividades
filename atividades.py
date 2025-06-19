class Atividade:
    contador_id = 1  # contador estático para gerar IDs automaticamente

    def __init__(self, descricao, tipo_atividade, chamado, tempo):
        self.id = Atividade.contador_id
        Atividade.contador_id += 1
        self.descricao = descricao
        self.tipo_atividade = tipo_atividade
        self.chamado = chamado
        self.tempo = tempo
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return (
            f"[ID: {self.id}] {self.tipo_atividade} - {status}\n"
            f"Descrição: {self.descricao}\n"
            f"Chamado: {self.chamado}\n"
            f"Tempo estimado: {self.tempo}h"
        )