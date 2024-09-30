import pandas as pd
from Classes import TabelaAlunos, TabelaTurmas, TabelaCoordenadores, TabelaProfessores

#Read
# Funções para simular consulta no banco de dados e retornar um dataframe pandas (matrix)
def receber_dados_alunos():
    return TabelaAlunos.TabelaAlunos(pd.read_csv('./Tabelas/alunos.csv')) 

def receber_dados_professores():
    return TabelaProfessores.TabelaProfessores(pd.read_csv('./Tabelas/professores.csv'))

def receber_dados_coordenadores():
    return TabelaCoordenadores.TabelaCoordenadores(pd.read_csv('./Tabelas/coordenadores.csv'))

def receber_dados_turmas():
    return TabelaTurmas.TabelaTurmas(pd.read_csv('./Tabelas/turmas.csv'))

#Create
def adicionarAluno(dataframe, Aluno):
    dataframe.loc[len(dataframe)] = Aluno.getDados()