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
        sns.displot(data=self.df,x='Pontuacao',kde=True)

    #Simulacoes realizadas ----------------------------------------------------------
    def media_simulacoes_realizadas_por_turma(self):
        m = self.df.groupby('Turma')['Num_simulacoes'].mean().reset_index()
        display(m)

    def pontuaca_media_por_quantidade_simulacoes(self):
        display(self.df.groupby('Num_simulacoes')['Pontuacao'].mean().reset_index())

    #Insígnias ----------------------------------------------------------
    def distribuicao_insignias(self):
        display(self.df['Num_insignias'].value_counts().reset_index())
    
    def pontuacao_por_numero_insignias(self):
        display(self.df.groupby('Num_insignias')['Pontuacao'].mean().reset_index())


    #desempenho ----------------------------------------------------------
    def diferenca_desempenho_por_turma(self):
        display(self.df.groupby('Turma')[['Pontuacao', 'Num_simulacoes']].mean().reset_index())

    # Função para salvar o DataFrame
    def save_dataframe(df):
        df.to_csv('./Tabelas/alunos.csv', index=False)

    # Função para buscar aluno por RM
    def search_student_by_rm(self,rm):
        aluno = self.df[self.df['Rm'] == rm]
        if not aluno.empty:
            print(aluno)
        else:
            print(f"Aluno com RM {rm} não encontrado.")

    # Função para adicionar um novo aluno
    def add_student(self, nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias):
        # Verifica se já existe um aluno com o mesmo RM
        if self.df[self.df['Rm'] == rm].empty:
            novo_aluno = pd.DataFrame({
                'Nome': [nome],
                'Idade': [idade],
                'Sexo': [sexo],
                'Turma': [turma],
                'Rm': [rm],
                'Pontuacao': [pontuacao],
                'Num_simulacoes': [num_simulacoes],
                'Num_insignias': [num_insignias]
            })

            # Concatenar o novo aluno com o DataFrame existente
            self.df = pd.concat([self.df, novo_aluno], ignore_index=True)
            TabelaAlunos.save_dataframe(self.df)
            print(f"Aluno com RM {rm} adicionado com sucesso.")
        else:
            print(f"Já existe um aluno com o RM {rm}.")

    # Função para excluir um aluno por RM
    def delete_student_by_rm(self,rm):
        # Verifica se o RM existe
        if not self.df[self.df['Rm'] == rm].empty:
            self.df = self.df[self.df['Rm'] != rm]  # Remove o aluno com o RM correspondente
            TabelaAlunos.save_dataframe(self.df)
            print(f"Aluno com RM {rm} excluído com sucesso.")
        else:
            print(f"Aluno com RM {rm} não encontrado.")

    def modify_student_by_rm(self,rm,novo_nome ,nova_idade):
        # Verifica se o RM existe
        if not self.df[self.df['Rm'] == rm].empty:
            aluno_index = self.df[self.df['Rm'] == rm].index[0]
            print(f"Aluno encontrado:\n{self.df.loc[aluno_index]}")

            if novo_nome is not None:
                self.df.at[aluno_index, 'Nome'] = novo_nome
            if nova_idade is not None:
                self.df.at[aluno_index, 'Idade'] = int(nova_idade)  
            # Salva o DataFrame modificado
            TabelaAlunos.save_dataframe(self.df)
            print(f"\nDados do aluno com RM {rm} modificados com sucesso.")

            # Printa os dados do aluno modificado
            aluno_modificado = self.df.loc[aluno_index]
            print(f"Aluno modificado:\n{aluno_modificado}")
        else:
            print(f"Aluno com RM {rm} não encontrado.")