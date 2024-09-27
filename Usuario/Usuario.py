from Aluno import Aluno

class Usuarios:
    def __init__(self, id, nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias, rank, pos_rank):
        self.aluno = Aluno(id, nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias, rank, pos_rank)


# usuarios_instance = Usuarios(id=1, nome='John Doe', idade=20, sexo='M', turma='CS101', rm='123456', pontuacao=0, num_simulacoes=0, num_insignias=0, rank='Novice', pos_rank=1)
