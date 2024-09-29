from IPython.display import display
import pandas as pd
import seaborn as sns

class TabelaAlunos:
    #Construtor
    def __init__(self,dataframe) -> None:
        self.df = dataframe

    #Estastísticas descritivas ----------------------------------------------------------
    #Por turma
    def media_pontuacao_turma(self):
        display(self.df.groupby('Turma')['Pontuacao'].mean().reset_index())
    def mediana_pontuacao_turma(self):
        display(self.df.groupby('Turma')['Pontuacao'].median().reset_index())

    #Por Idade
    def media_pontuacao_idade(self):
        display(self.df.groupby('Idade')['Pontuacao'].mean().reset_index())
    def mediana_pontuacao_idade(self):
        display(self.df.groupby('Idade')['Pontuacao'].median().reset_index())

    #Por Sexo
    def media_pontuacao_sexo(self):
        display(self.df.groupby('Sexo')['Pontuacao'].mean().reset_index())
    def mediana_pontuacao_sexo(self):
        display(self.df.groupby('Sexo')['Pontuacao'].median().reset_index())

    #Correlação ----------------------------------------------------------
    def correlacaoPontuacao(self):
        display(self.df[['Pontuacao', 'Num_simulacoes', 'Num_insignias']].corr())

    # Desempenho Geral
    def media_geral(self):
        m = self.df['Pontuacao'].mean()
        print(f'Média pontuação dos alunos: {m}')

    def melhores_pontuacoes(self):
        print('\nAs 10 maiores pontuações')
        display(self.df.nlargest(10, 'Pontuacao'))
    
    def distribuicao_pontuacao(self):
        sns.histplot(data=self.df,x='Pontuacao')