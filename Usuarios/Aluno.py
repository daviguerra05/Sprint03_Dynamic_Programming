from Usuario import Usuario

class Aluno(Usuario):

    def __init__(self, nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias):
        super().__init__(self,nome, idade, sexo)
        self.turma= turma, 
        self.rm = rm, 
        self.pontuacao= pontuacao, 
        self.num_simulacoes= num_simulacoes, 
        self.num_insignias= num_insignias

    # Representação da classe em string
    def __str__(self) -> str:
        return (f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, "
                f"Turma: {self.turma}, RM: {self.rm}, Pontuação: {self.pontuacao}, "
                f"Simulações: {self.num_simulacoes}, Insígnias: {self.num_insignias}, "
                f"Rank: {self.rank}, Posição no Rank: {self.pos_rank}")