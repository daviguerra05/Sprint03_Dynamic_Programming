import pandas as pd
from Classes import TabelaAlunos, TabelaTurmas, TabelaCoordenadores, TabelaProfessores

# Funções para simular consulta no banco de dados e retornar uma estrutura de dados dataframe pandas (matrix).
def receber_dados_alunos():
    return TabelaAlunos.TabelaAlunos(pd.read_csv('./Tabelas/alunos.csv')) 

def receber_dados_professores():
    return TabelaProfessores.TabelaProfessores(pd.read_csv('./Tabelas/professores.csv'))

def receber_dados_coordenadores():
    return TabelaCoordenadores.TabelaCoordenadores(pd.read_csv('./Tabelas/coordenadores.csv'))

def receber_dados_turmas():
    return TabelaTurmas.TabelaTurmas(pd.read_csv('./Tabelas/turmas.csv'))    