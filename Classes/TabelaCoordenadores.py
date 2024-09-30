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
    
    # Atualização da tabela ----------------------------------------------------------

    def salvar_dataset(df):
        df.to_csv('./Tabelas/coordenadores.csv', index=False)

    #Create
    def adicionarcoordenador(self, coordenador):
        # Verifica se já existe um coordenador com o mesmo registro
        if self.df[self.df['Registro'] == coordenador.Registro].empty:
            novo_coordenador = pd.DataFrame({
                'Nome': [coordenador.Nome],
                'Idade': [coordenador.Idade],
                'Sexo': [coordenador.Sexo],
                'Registro' : [coordenador.Registro]
            })

            # Concatenar o novo coordenador com o DataFrame existente
            self.df = pd.concat([self.df, novo_coordenador], ignore_index=True)
            self.save_dataframe(self.df)

            print(f"coordenador de registro {coordenador.Registro} adicionado com sucesso.")
        else:
            print(f"Já existe um coordenador com o Registro {coordenador.Registro}.")

    #Delete
    # Função para excluir um coordenador pelo seu registro
    def deletar_coordenador_por_registro(self, registro):
        # Verifica se o registro existe
        if not self.df[self.df['Registro'] == registro].empty:
            self.df = self.df[self.df['Registro'] != registro]  # Remove o coordenador com o Registro correspondente
            self.save_dataframe(self.df)
            print(f"coordenador com Registro {registro} excluído com sucesso.")
        else:
            print(f"coordenador com Registro {registro} não encontrado.")
    
    #Update
    # Regras de negócia permite apenas alteração nestes campos
    def modificar_coordenador_por_registro(self,novo_nome=None, nova_idade=None, coordenador=None):
        if coordenador:
            # Verifica se o Registro existe
            if not self.df[self.df['Registro'] == coordenador.Registro].empty:
                coordenador_index = self.df[self.df['Registro'] == coordenador.Registro].index[0]

                if novo_nome:
                    self.df.at[coordenador_index, 'Nome'] = novo_nome
                if nova_idade:
                    self.df.at[coordenador_index, 'Idade'] = int(nova_idade) 

                # Salva o DataFrame modificado
                self.salvar_dataset(self.df)
                print(f"\nDados do coordenador com Registro {coordenador.Registro} modificados com sucesso.")

                # Printa os dados do coordenador modificado
                coordenador_modificado = self.df.loc[coordenador_index]
                print(f"coordenador modificado:\n{coordenador_modificado}")
            else:
                print(f"coordenador com Registro {coordenador.Registro} não encontrado.")
        else:
            print('Nenhmum coordenador recebido na função.')