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
    def salvar_dataset(self):
        self.df.to_csv('./Tabelas/coordenadores.csv', index=False)

    #Create
    def adicionarcoordenador(self, coordenador):
        # Verifica se já existe um coordenador com o mesmo registro
        if self.df[self.df['Registro'] == coordenador.Registro].empty:
            if len(str(coordenador.Registro)) > 5:
                print('Registro está em um formato incorreto.')
                return

            novo_coordenador = pd.DataFrame({
                'Nome': coordenador.Nome,
                'Idade': coordenador.Idade,
                'Sexo': coordenador.Sexo,
                'Registro' : coordenador.Registro
            })

            # Concatenar o novo coordenador com o DataFrame existente
            self.df = pd.concat([self.df, novo_coordenador], ignore_index=True)
            self.salvar_dataset()

            print(f"coordenador de registro {coordenador.Registro} adicionado com sucesso.")
        else:
            print(f"Já existe um coordenador com o Registro {coordenador.Registro}.")

    #Delete
    # Função para excluir um coordenador pelo seu registro
    def deletar_coordenador_por_registro(self, registro):
        # Verifica se o registro existe
        if not self.df[self.df['Registro'] == registro].empty:
            self.df = self.df[self.df['Registro'] != registro]  # Remove o coordenador com o Registro correspondente
            self.salvar_dataset()
            print(f"coordenador com Registro {registro} excluído com sucesso.")
        else:
            print(f"coordenador com Registro {registro} não encontrado.")
    
    #Update
    # Regras de negócia permite apenas alteração nestes campos
    def modificar_coordenador_por_registro(self,novo_nome=None, nova_idade=None, Registro=None):
        if Registro:
            # Verifica se o Registro existe
            if not self.df[self.df['Registro'] == Registro].empty:
                coordenador_index = self.df[self.df['Registro'] == Registro].index[0]

                if novo_nome:
                    self.df.at[coordenador_index, 'Nome'] = novo_nome
                if nova_idade:
                    self.df.at[coordenador_index, 'Idade'] = int(nova_idade) 

                # Salva o DataFrame modificado
                self.salvar_dataset()
                print(f"\nDados do coordenador com Registro {Registro} modificados com sucesso.")
            else:
                print(f"coordenador com Registro {Registro} não encontrado.")
        else:
            print('Nenhmum Registro recebido na função.')