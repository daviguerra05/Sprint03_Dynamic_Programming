from IPython.display import display
import pandas as pd
import seaborn as sns
from sklearn import linear_model 

class TabelaAlunos:
    #Atributos
    modelo = None
    
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

    #Correlação
    def correlacaoPontuacao(self):
        display(self.df[['Pontuacao', 'Num_simulacoes', 'Num_insignias']].corr())

    # Desempenho Geral
    def media_geral(self):
        print(f'Média pontuação dos alunos: {self.df['Pontuacao'].mean()}')

    def melhores_pontuacoes(self):
        print('\nAs 10 maiores pontuações')
        display(self.df.nlargest(10, 'Pontuacao'))
    
    def distribuicao_pontuacao(self):
        sns.displot(data=self.df,x='Pontuacao',kde=True)

    #Simulacoes realizadas
    def media_simulacoes_realizadas_por_turma(self):
        display(self.df.groupby('Turma')['Num_simulacoes'].mean().reset_index())

    def pontuaca_media_por_quantidade_simulacoes(self):
        display(self.df.groupby('Num_simulacoes')['Pontuacao'].mean().reset_index())

    #Insígnias 
    def distribuicao_insignias(self):
        display(self.df['Num_insignias'].value_counts().reset_index())
    
    def pontuacao_media_por_numero_insignias(self):
        display(self.df.groupby('Num_insignias')['Pontuacao'].mean().reset_index())

    #Desempenho 
    def diferenca_desempenho_por_turma(self):
        display(self.df.groupby('Turma')[['Pontuacao', 'Num_simulacoes']].mean().reset_index())

    # Atualização da tabela ----------------------------------------------------------
    def salvar_dataframe(self):
        self.df.to_csv('./Tabelas/alunos.csv', index=False)

    def add_student(self, nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias):
        df_turmas = pd.read_csv('./Tabelas/turmas.csv')
        turmas = list(df_turmas['Nome'])
        
        # Validação de idade
        if idade <= 17:
            print("A idade deve ser maior que 17.")
            return
        
        # Verifica se a turma existe na tabela "Turmas"
        if turma not in turmas:
            print("A turma fornecida não existe.")
            return

        # Verifica se o RM tem 6 dígitos
        if len(str(rm)) != 6:
            print("O RM deve ter 6 dígitos.")
            return

        # Verifica se a pontuação máxima é válida
        max_pontuacao = num_simulacoes * 1000
        if pontuacao > max_pontuacao:
            print(f"A pontuação máxima permitida é {max_pontuacao}.")
            return
        
        # Verifica se o número de simulações está dentro do limite
        if num_simulacoes > 3:
            print("O número máximo de simulações é 3.")
            return
        
        # Verifica se o número de insígnias está dentro do limite
        if num_insignias > 15:
            print("O número máximo de insígnias é 15.")
            return

        # Verifica se já existe um aluno com o mesmo RM
        aluno = self.df[self.df['Rm'] == rm]
        # Inverte a lógica: se o aluno não existe, adiciona
        if aluno.empty:
            # Cria o novo aluno apenas se não existir um aluno com o mesmo RM
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
            self.df.to_csv('./Tabelas/alunos.csv', index=False)
            print(f"Aluno com RM {rm} adicionado com sucesso.")
        else:
            print(f"Já existe um aluno com o RM {rm}.")

    # Função para excluir um aluno por RM
    def delete_student_by_rm(self, rm):
        # Verifica se o RM existe
        if not self.df[self.df['Rm'] == rm].empty:
            self.df = self.df[self.df['Rm'] != rm]  # Remove o aluno com o RM correspondente
            self.df.to_csv('./Tabelas/alunos.csv', index=False)
            print(f"Aluno com RM {rm} excluído com sucesso.")
        else:
            print(f"Aluno com RM {rm} não encontrado.")

    def modify_student_by_rm(self, rm, novo_nome=None, nova_idade=None):
        # Verifica se o RM existe
        if not self.df[self.df['Rm'] == rm].empty:
            aluno_index = self.df[self.df['Rm'] == rm].index[0]

            if novo_nome is not None:
                self.df.at[aluno_index, 'Nome'] = novo_nome
              
            if nova_idade is not None:
                self.df.at[aluno_index, 'Idade'] = int(nova_idade)  # Converte para inteiro
              
            # Salva o DataFrame modificado
            self.df.to_csv('./Tabelas/alunos.csv', index=False)
            print(f"\nDados do aluno com RM {rm} modificados com sucesso.")
        else:
            print(f"Aluno com RM {rm} não encontrado.")

    #Funções para prever pontuação do aluno e realizar análise ----------------------------------------------------------
    def treinarModelo(self):
        Y = self.df['Pontuacao']
        X = self.df[['Num_simulacoes','Num_insignias']]

        self.model = linear_model.BayesianRidge()
        self.model.fit(X,Y)

    def prever(self,num_simulacoes, num_insignias):
        if not self.modelo:
            self.treinarModelo()

        teste = {
            'Num_simulacoes': [num_simulacoes],
            'Num_insignias': [num_insignias]
        }
        return self.model.predict(pd.DataFrame(teste))[0]
    
    def analiseAluno(self, aluno):
        pont = aluno.Pontuacao[0] 
        prev = self.prever(aluno.Num_simulacoes[0],aluno.Num_insignias)
        dif = pont - prev
        if dif > 0:
            print(f'Parabéns, você teve uma pontuação maior do que o previsto. Continue assim!')
        else:
            print('Você não obteve uma pontuação maior do que o previsto. Continue treinando!')
        
        print(f'Pontuação prevista de {round(prev,2)}, sua pontuacao foi de {round(pont,2)}')