import pandas as pd

class Turma:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Aluno:
    def __init__(self, id: int, nome: str, idade: int, sexo: str, turma: Turma, rm: int, pontuacao: int, num_simulacoes: int, num_insignias: int, rank: str, pos_rank: int):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.turma = turma
        self.rm = rm
        self.pontuacao = pontuacao
        self.num_simulacoes = num_simulacoes
        self.num_insignias = num_insignias
        self.rank = rank
        self.pos_rank = pos_rank

    # Métodos get e set para pontuação
    def getPontuacao(self) -> int:
        return self.pontuacao

    def setPontuacao(self, pontuacao: int) -> None:
        self.pontuacao = pontuacao

    # Métodos get e set para rank
    def getRank(self) -> str:
        return self.rank

    def setRank(self, rank: str) -> None:
        self.rank = rank

    # Métodos get e set para RM
    def getRm(self) -> int:
        return self.rm

    def setRm(self, rm: int) -> None:
        self.rm = rm

    # Métodos get e set para turma
    def getTurma(self) -> Turma:
        return self.turma

    def setTurma(self, turma: Turma) -> None:
        self.turma = turma

    # Métodos get e set para número de simulações
    def getNum_simulacoes(self) -> int:
        return self.num_simulacoes

    def setNum_simulacoes(self, num_simulacoes: int) -> None:
        self.num_simulacoes = num_simulacoes

    # Métodos get e set para número de insígnias
    def getNum_insignias(self) -> int:
        return self.num_insignias

    def setNum_insignias(self, num_insignias: int) -> None:
        self.num_insignias = num_insignias

    # Métodos get e set para posição no rank
    def getPos_rank(self) -> int:
        return self.pos_rank

    def setPos_rank(self, pos_rank: int) -> None:
        self.pos_rank = pos_rank

    # Método para comparar alunos pela pontuação
    def compareTo(self, outroAluno) -> int:
        if self.pontuacao > outroAluno.getPontuacao():
            return 1
        elif self.pontuacao < outroAluno.getPontuacao():
            return -1
        return 0

    # Representação da classe em string
    def __str__(self) -> str:
        return (f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, "
                f"Turma: {self.turma}, RM: {self.rm}, Pontuação: {self.pontuacao}, "
                f"Simulações: {self.num_simulacoes}, Insígnias: {self.num_insignias}, "
                f"Rank: {self.rank}, Posição no Rank: {self.pos_rank}")
    
    # Função para carregar o DataFrame de Coordenadores
    def load_coordenadores_dataframe():
        return pd.read_csv(r'Tabelas\Coordenadores.csv')

    # Função para salvar o DataFrame de Coordenadores
    def save_coordenadores_dataframe(df):
        df.to_csv(r'Tabelas\Coordenadores.csv', index=False)

    # Função para mostrar todos os coordenadores
    def show_all_coordenadores():
        df = Aluno.load_coordenadores_dataframe()
        pd.set_option('display.max_rows', None)
        print(df)

    # Função para buscar coordenador por registro
    def search_coordenador_by_registro(registro):
        df = Aluno.load_coordenadores_dataframe()
        coordenador = df[df['Registro'] == registro]
        if not coordenador.empty:
            print(coordenador)
        else:
            print(f"Coordenador com registro {registro} não encontrado.")

    # Função para adicionar um novo coordenador
    def add_coordenador(nome, idade, sexo, registro):
        df = Aluno.load_coordenadores_dataframe()
        
        # Verifica se já existe um coordenador com o mesmo registro
        if df[df['Registro'] == registro].empty:
            novo_coordenador = pd.DataFrame({
                'Nome': [nome],
                'Idade': [idade],
                'Sexo': [sexo],
                'Registro': [registro]
            })
            
            # Concatenar o novo coordenador com o DataFrame existente
            df = pd.concat([df, novo_coordenador], ignore_index=True)
            Aluno.save_coordenadores_dataframe(df)
            print(f"Coordenador {nome} adicionado com sucesso.")
        else:
            print(f"Já existe um coordenador com o registro {registro}.")

    # Função para excluir um coordenador por registro
    def delete_coordenador_by_registro(registro):
        df = Aluno.load_coordenadores_dataframe()
        
        # Verifica se o registro existe
        if not df[df['Registro'] == registro].empty:
            df = df[df['Registro'] != registro]  # Remove o coordenador com o registro correspondente
            Aluno.save_coordenadores_dataframe(df)
            print(f"Coordenador com registro {registro} excluído com sucesso.")
        else:
            print(f"Coordenador com registro {registro} não encontrado.")

    # Função para modificar coordenador por registro
    def modify_coordenador_by_registro(registro):
        df = Aluno.load_coordenadores_dataframe()
        
        # Verifica se o coordenador existe
        if not df[df['Registro'] == registro].empty:
            coordenador_index = df[df['Registro'] == registro].index[0]
            print(f"Coordenador encontrado:\n{df.loc[coordenador_index]}")
            
            # Menu de opções para modificar atributos
            while True:
                print("\nEscolha o atributo que deseja modificar:")
                print("1 - Nome")
                print("2 - Idade")
                print("3 - Sexo")
                print("0 - Finalizar modificações")
                
                escolha = input("Digite o número correspondente ao atributo: ")
                
                if escolha == '1':
                    novo_nome = input("Digite o novo nome: ")
                    df.at[coordenador_index, 'Nome'] = novo_nome
                elif escolha == '2':
                    idade = input("Digite a nova idade: ")
                    df.at[coordenador_index, 'Idade'] = idade
                elif escolha == '3':
                    sexo = input("Digite o novo sexo (M/F): ")
                    df.at[coordenador_index, 'Sexo'] = sexo
                elif escolha == '0':
                    print("Modificações finalizadas.")
                    break
                else:
                    print("Opção inválida. Escolha novamente.")
            
            # Salva o DataFrame modificado
            Aluno.save_coordenadores_dataframe(df)
            print(f"\nDados do coordenador com registro {registro} modificados com sucesso.")
            
            # Printa os dados do coordenador modificado
            coordenador_modificado = df.loc[coordenador_index]
            print(f"Coordenador modificado:\n{coordenador_modificado}")
        else:
            print(f"Coordenador com registro {registro} não encontrado.")

# Exemplo de uso (descomentado se necessário)
# show_all_coordenadores()                          # Mostra todos os coordenadores
#search_coordenador_by_registro(4964)               # Busca por registro
#add_coordenador('Nova Coordenador', 30, 'M', 1234)  # Adiciona coordenador
#delete_coordenador_by_registro(1234)               # Exclui coordenador por registro
# modify_coordenador_by_registro(4964)               # Modifica coordenador por registro

