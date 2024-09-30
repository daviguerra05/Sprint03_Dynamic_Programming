import pandas as pd
from Classes import TabelaAlunos, TabelaTurmas

# Exemplo
def distribuicao_dados_tabela_x():
    pass

# Funções para simular consulta no banco de dados e retornar um dataframe pandas (matrix)
def receber_dados_alunos():
    return TabelaAlunos.TabelaAlunos(pd.read_csv('./Tabelas/alunos.csv')) 

def receber_dados_professores():
    return pd.read_csv('./Tabelas/professores.csv')

def receber_dados_coordenadores():
    return pd.read_csv('./Tabelas/coordenadores.csv')

def receber_dados_turmas():
    return TabelaTurmas.TabelaTurmas(pd.read_csv('./Tabelas/turmas.csv'))


