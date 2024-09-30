import pandas as pd

class TabelaTurmas:
    #Construtor
    def __init__(self,dataframe) -> None:
        self.df = dataframe
  
    # Atualização da tabela ----------------------------------------------------------
    def salvar_dataset(self):
        self.df.to_csv('./Tabelas/turmas.csv', index=False)

    #Create
    def adicionarTurma(self, Turma):
        professores = list(pd.read_csv('./Tabelas/professores.csv')['Nome'])
        coordenadores = pd.read_csv('./Tabelas/coordenadores.csv')

        # Verifica se já existe um Turma com o mesmo Nome
        if self.df[self.df['Nome'] == Turma.Nome].empty:
            if Turma.Professor_responsavel not in professores:
                print('Professor não existe no banco de dados.')
                return
            
            if Turma.Coordenador_responsavel[0] not in list(coordenadores['Nome']):
                print('Coordenador não existe no banco de dados.')
                print(Turma.Coordenador_responsavel)
                return
            
            novo_Turma = pd.DataFrame({
                'Nome': Turma.Nome,
                'Periodo': Turma.Periodo,
                'Coordenador_responsavel': Turma.Coordenador_responsavel,
                'Professor_responsavel' : Turma.Professor_responsavel
            })

            # Concatenar o novo Turma com o DataFrame existente
            self.df = pd.concat([self.df, novo_Turma], ignore_index=True)
            self.salvar_dataset()

            print(f"Turma de Nome {Turma.Nome[0]} adicionado com sucesso.")
        else:
            print(f"Já existe um Turma com o Nome {Turma.Nome}.")

    #Delete
    def deletar_Turma_por_Nome(self, Nome):
        # Verifica se o Nome existe
        if not self.df[self.df['Nome'] == Nome].empty:
            self.df = self.df[self.df['Nome'] != Nome]  # Remove o Turma com o Nome correspondente
            self.salvar_dataset()
            print(f"Turma com Nome {Nome} excluído com sucesso.")
        else:
            print(f"Turma com Nome {Nome} não encontrado.")
    
    #Update
    # Regras de negócia permite apenas alteração nestes campos
    def modificar_Turma_por_Nome(self, novo_periodo=None, Nome=None):
        if Nome:
            # Verifica se o Nome existe
            if not self.df[self.df['Nome'] == Nome].empty:
                Turma_index = self.df[self.df['Nome'] == Nome].index[0]

                if novo_periodo:
                    self.df.at[Turma_index, 'Periodo'] = novo_periodo

                # Salva o DataFrame modificado
                self.salvar_dataset()
                print(f"\nDados do Turma com Nome {Nome} modificados com sucesso.")
            else:
                print(f"Turma com Nome {Nome} não encontrado.")
        else:
            print('Nenhmum Nome recebido na função.')