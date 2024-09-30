from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def receber_dados_coordenadores():
    return pd.read_csv('./Tabelas/coordenadores.csv')

class TabelaCoordenadores:
    # Construtor
    def __init__(self, dataframe) -> None:
        self.df = dataframe

    # Gráfico: Distribuição de Sexo por Idade
    def grafico_sexo_por_idade(self):
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x='Idade', hue='Sexo', palette='Set2')
        plt.title('Distribuição de Sexo por Idade dos Coordenadores')
        plt.xlabel('Idade')
        plt.ylabel('Número de Coordenadores')
        plt.legend(title='Sexo')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

# Exemplo de uso:
df_coordenadores = receber_dados_coordenadores()  # Recebe os dados através da função

tabela_coordenadores = TabelaCoordenadores(df_coordenadores)  # Instancia a tabela com os dados recebidos
tabela_coordenadores.grafico_sexo_por_idade()  # Gráfico de sexo por idade






