class Turma:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Aluno:
    def __init__(self, id: int, nome: str, idade: int, sexo: str, turma: Turma, rm: int, pontuacao: int, num_simulacoes: int, num_insignias: int, rank: str, pos_rank: int):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.turma = turma
        self.rm = rm
        self.pontuacao = pontuacao
        self.num_simulacoes = num_simulacoes
        self.num_insignias = num_insignias
        self.rank = rank
        self.pos_rank = pos_rank

    # Métodos get e set para pontuação
    def getPontuacao(self) -> int:
        return self.pontuacao

    def setPontuacao(self, pontuacao: int) -> None:
        self.pontuacao = pontuacao

    # Métodos get e set para rank
    def getRank(self) -> str:
        return self.rank

    def setRank(self, rank: str) -> None:
        self.rank = rank

    # Métodos get e set para RM
    def getRm(self) -> int:
        return self.rm

    def setRm(self, rm: int) -> None:
        self.rm = rm

    # Métodos get e set para turma
    def getTurma(self) -> Turma:
        return self.turma

    def setTurma(self, turma: Turma) -> None:
        self.turma = turma

    # Métodos get e set para número de simulações
    def getNum_simulacoes(self) -> int:
        return self.num_simulacoes

    def setNum_simulacoes(self, num_simulacoes: int) -> None:
        self.num_simulacoes = num_simulacoes

    # Métodos get e set para número de insígnias
    def getNum_insignias(self) -> int:
        return self.num_insignias

    def setNum_insignias(self, num_insignias: int) -> None:
        self.num_insignias = num_insignias

    # Métodos get e set para posição no rank
    def getPos_rank(self) -> int:
        return self.pos_rank

    def setPos_rank(self, pos_rank: int) -> None:
        self.pos_rank = pos_rank

    # Método para comparar alunos pela pontuação
    def compareTo(self, outroAluno) -> int:
        if self.pontuacao > outroAluno.getPontuacao():
            return 1
        elif self.pontuacao < outroAluno.getPontuacao():
            return -1
        return 0

    # Representação da classe em string
    def __str__(self) -> str:
        return (f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, "
                f"Turma: {self.turma}, RM: {self.rm}, Pontuação: {self.pontuacao}, "
                f"Simulações: {self.num_simulacoes}, Insígnias: {self.num_insignias}, "
                f"Rank: {self.rank}, Posição no Rank: {self.pos_rank}")
