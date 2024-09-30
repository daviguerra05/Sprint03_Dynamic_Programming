class Aluno:
    def __init__(self,Nome,Idade,Sexo,Turma,Rm,Pontuacao,Num_simulacoes,Num_insignias) -> None:
        self.Nome=Nome,
        self.Idade=Idade,
        self.Sexo=Sexo,
        self.Turma=Turma,
        self.Rm=Rm,
        self.Pontuacao=Pontuacao,
        self.Num_simulacoes=Num_simulacoes,
        self.Num_insignias=Num_insignias
    
    def getDados(self):
        return [
            self.Nome,
            self.Idade,
            self.Sexo,
            self.Turma,
            self.Rm,
            self.Pontuacao,
            self.Num_simulacoes,
            self.Num_insignias
        ]