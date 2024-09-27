import pandas as pd

# Função para carregar o DataFrame
def load_dataframe():
    return pd.read_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Alunos.csv')

# Função para salvar o DataFrame
def save_dataframe(df):
    df.to_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Alunos.csv', index=False)

# Função para mostrar todos os alunos
def show_all_students():
    df = load_dataframe()
    pd.set_option('display.max_rows', None)
    print(df)

# Função para buscar aluno por RM
def search_student_by_rm(rm):
    df = load_dataframe()
    aluno = df[df['Rm'] == rm]
    if not aluno.empty:
        print(aluno)
    else:
        print(f"Aluno com RM {rm} não encontrado.")


# Função para adicionar um novo aluno
def add_student(nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias):
    df = load_dataframe()
    
    # Verifica se já existe um aluno com o mesmo RM
    if df[df['Rm'] == rm].empty:
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
        df = pd.concat([df, novo_aluno], ignore_index=True)
        save_dataframe(df)
        print(f"Aluno com RM {rm} adicionado com sucesso.")
    else:
        print(f"Já existe um aluno com o RM {rm}.")


# Função para excluir um aluno por RM
def delete_student_by_rm(rm):
    df = load_dataframe()
    
    # Verifica se o RM existe
    if not df[df['Rm'] == rm].empty:
        df = df[df['Rm'] != rm]  # Remove o aluno com o RM correspondente
        save_dataframe(df)
        print(f"Aluno com RM {rm} excluído com sucesso.")
    else:
        print(f"Aluno com RM {rm} não encontrado.")


def modify_student_by_rm(rm):
    df = load_dataframe()
    
    # Verifica se o RM existe
    if not df[df['Rm'] == rm].empty:
        aluno_index = df[df['Rm'] == rm].index[0]
        print(f"Aluno encontrado:\n{df.loc[aluno_index]}")
        
        # Menu de opções para modificar atributos
        while True:
            print("\nEscolha o atributo que deseja modificar:")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Sexo")
            print("4 - Turma")
            print("5 - Pontuação")
            print("6 - Número de Simulações")
            print("7 - Número de Insígnias")
            print("0 - Finalizar modificações")
            
            escolha = input("Digite o número correspondente ao atributo: ")
            
            if escolha == '1':
                nome = input("Digite o novo nome: ")
                df.at[aluno_index, 'Nome'] = nome
            elif escolha == '2':
                idade = input("Digite a nova idade: ")
                df.at[aluno_index, 'Idade'] = int(idade)  # Converte para inteiro
            elif escolha == '3':
                sexo = input("Digite o novo sexo (M/F): ")
                df.at[aluno_index, 'Sexo'] = sexo
            elif escolha == '4':
                turma = input("Digite a nova turma: ")
                df.at[aluno_index, 'Turma'] = turma
            elif escolha == '5':
                pontuacao = input("Digite a nova pontuação: ")
                df.at[aluno_index, 'Pontuacao'] = float(pontuacao)  # Converte para float se necessário
            elif escolha == '6':
                num_simulacoes = input("Digite o novo número de simulações: ")
                df.at[aluno_index, 'Num_simulacoes'] = int(num_simulacoes)  # Converte para inteiro
            elif escolha == '7':
                num_insignias = input("Digite o novo número de insígnias: ")
                df.at[aluno_index, 'Num_insignias'] = int(num_insignias)  # Converte para inteiro
            elif escolha == '0':
                print("Modificações finalizadas.")
                break
            else:
                print("Opção inválida. Escolha novamente.")
        
        # Salva o DataFrame modificado
        save_dataframe(df)
        print(f"\nDados do aluno com RM {rm} modificados com sucesso.")
        
        # Printa os dados do aluno modificado
        aluno_modificado = df.loc[aluno_index]
        print(f"Aluno modificado:\n{aluno_modificado}")
    else:
        print(f"Aluno com RM {rm} não encontrado.")

#modify_student_by_rm(123456)  # Altere o RM conforme necessário
#show_all_students()                # Mostra todos os alunos
#search_student_by_rm(772237)        # Busca por RM
#add_student('João Silva', 22, 'M', '3LPNY', 12356, 500, 2, 5)  # Adiciona aluno
#delete_student_by_rm(12356)        # Exclui aluno por RM

