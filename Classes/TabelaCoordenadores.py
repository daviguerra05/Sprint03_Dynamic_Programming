from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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