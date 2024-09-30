from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TabelaProfessores:
    # Construtor
    def __init__(self, dataframe):
        self.df = dataframe

    # Estatísticas descritivas ----------------------------------------------------------
    # Por Sexo
    def media_idade_sexo(self):
        display(self.df.groupby('Sexo')['Idade'].mean().reset_index())
    
    def mediana_idade_sexo(self):
        display(self.df.groupby('Sexo')['Idade'].median().reset_index())

    # Desempenho Geral
    def media_geral_idade(self):
        print(f'Média de idade dos professores: {self.df['Idade'].mean()}')
   
    def maiores_idades(self):
        print('\nAs 10 maiores idades dos professores:')
        display(self.df.nlargest(10, 'Idade'))
    
    def distribuicao_idade(self):
        sns.histplot(data=self.df, x='Idade')
        plt.title('Distribuição da Idade dos Professores')
        plt.xlabel('Idade')
        plt.ylabel('Frequência')
        plt.show()

    # Atualização da tabela ----------------------------------------------------------
    def salvar_dataset(self):
        self.df.to_csv('./Tabelas/professores.csv', index=False)

    #Create
    def adicionarProfessor(self, Professor):
        # Verifica se já existe um professor com o mesmo registro
        if self.df[self.df['Registro'] == Professor.Registro].empty:
            if len(str(Professor.Registro)) > 5:
                print('Registro está em um formato incorreto.')
                return 
            novo_professor = pd.DataFrame({
                'Nome': Professor.Nome,
                'Idade': Professor.Idade,
                'Sexo': Professor.Sexo,
                'Registro' : Professor.Registro
            })

            # Concatenar o novo professor com o DataFrame existente
            self.df = pd.concat([self.df, novo_professor], ignore_index=True)
            
            self.salvar_dataset()

            print(f"Professor de registro {Professor.Registro} adicionado com sucesso.")
        else:
            print(f"Já existe um professor com o Registro {Professor.Registro}.")

    #Delete
    def deletar_professor_por_registro(self, registro):
        # Verifica se o registro existe
        if not self.df[self.df['Registro'] == registro].empty:
            self.df = self.df[self.df['Registro'] != registro]  # Remove o professor com o Registro correspondente
            self.salvar_dataset()
            print(f"Professor com Registro {registro} excluído com sucesso.")
        else:
            print(f"Professor com Registro {registro} não encontrado.")
    
    #Update
    # Regras de negócia permite apenas alteração nestes campos
    def modificar_professor_por_registro(self,novo_nome=None, nova_idade=None, Registro=None):
        if Registro:
            # Verifica se o Registro existe
            if not self.df[self.df['Registro'] == Registro].empty:
                professor_index = self.df[self.df['Registro'] == Registro].index[0]

                if novo_nome:
                    self.df.at[professor_index, 'Nome'] = novo_nome
                if nova_idade:
                    self.df.at[professor_index, 'Idade'] = int(nova_idade) 

                # Salva o DataFrame modificado
                self.salvar_dataset()
                print(f"\nDados do professor com Registro {Registro} modificados com sucesso.")
            else:
                print(f"Professor com Registro {Registro} não encontrado.")
        else:
            print('Não foi informado nenhum registro')