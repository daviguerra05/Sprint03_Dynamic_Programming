from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def receber_dados_professores():
    return pd.read_csv('./Tabelas/professores.csv')

class TabelaProfessores:
    # Construtor
    def __init__(self, dataframe) -> None:
        self.df = dataframe

    # Estatísticas descritivas ----------------------------------------------------------
    # Por Sexo
    def media_idade_sexo(self):
        display(self.df.groupby('Sexo')['Idade'].mean().reset_index())
    
    def mediana_idade_sexo(self):
        display(self.df.groupby('Sexo')['Idade'].median().reset_index())

    # Desempenho Geral
    def media_geral_idade(self):
        m = self.df['Idade'].mean()
        print(f'Média de idade dos professores: {m}')

    def maiores_idades(self):
        print('\nAs 10 maiores idades dos professores:')
        display(self.df.nlargest(10, 'Idade'))
    
    def distribuicao_idade(self):
        sns.histplot(data=self.df, x='Idade')
        plt.title('Distribuição da Idade dos Professores')
        plt.xlabel('Idade')
        plt.ylabel('Frequência')
        plt.show()

# Exemplo de uso:
df_professores = receber_dados_professores()  # Recebe os dados através da função

tabela_professores = TabelaProfessores(df_professores)  # Instancia a tabela com os dados recebidos
tabela_professores.media_geral_idade()  # Calcula e exibe a média de idade
tabela_professores.maiores_idades()  # Exibe as 10 maiores idades
tabela_professores.distribuicao_idade()  # Plota a distribuição de idades
