import pandas as pd

# Função para carregar o DataFrame
def load_professor_dataframe():
    return pd.read_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Professores.csv')

# Função para salvar o DataFrame
def save_professor_dataframe(df):
    df.to_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Professores.csv', index=False)

# Função para mostrar todos os professores
def show_all_professors():
    df = load_professor_dataframe()
    pd.set_option('display.max_rows', None)
    print(df)

# Função para buscar professor por Registro
def search_professor_by_registro(registro):
    df = load_professor_dataframe()
    professor = df[df['Registro'] == registro]
    if not professor.empty:
        print(professor)
    else:
        print(f"Professor com Registro {registro} não encontrado.")

# Função para adicionar um novo professor
def add_professor(nome, idade, sexo, registro):
    df = load_professor_dataframe()
    
    # Verifica se já existe um professor com o mesmo Registro
    if df[df['Registro'] == registro].empty:
        novo_professor = pd.DataFrame({
            'Nome': [nome],
            'Idade': [idade],
            'Sexo': [sexo],
            'Registro': [registro]
        })
        
        # Concatenar o novo professor com o DataFrame existente
        df = pd.concat([df, novo_professor], ignore_index=True)
        save_professor_dataframe(df)
        print(f"Professor com Registro {registro} adicionado com sucesso.")
    else:
        print(f"Já existe um professor com o Registro {registro}.")

# Função para excluir um professor por Registro
def delete_professor_by_registro(registro):
    df = load_professor_dataframe()
    
    # Verifica se o Registro existe
    if not df[df['Registro'] == registro].empty:
        df = df[df['Registro'] != registro]  # Remove o professor com o Registro correspondente
        save_professor_dataframe(df)
        print(f"Professor com Registro {registro} excluído com sucesso.")
    else:
        print(f"Professor com Registro {registro} não encontrado.")

# Função para modificar professor por Registro
def modify_professor_by_registro(registro):
    df = load_professor_dataframe()
    
    # Verifica se o Registro existe
    if not df[df['Registro'] == registro].empty:
        professor_index = df[df['Registro'] == registro].index[0]
        print(f"Professor encontrado:\n{df.loc[professor_index]}")
        
        # Menu de opções para modificar atributos
        while True:
            print("\nEscolha o atributo que deseja modificar:")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Sexo")
            print("0 - Finalizar modificações")
            
            escolha = input("Digite o número correspondente ao atributo: ")
            
            if escolha == '1':
                nome = input("Digite o novo nome: ")
                df.at[professor_index, 'Nome'] = nome
            elif escolha == '2':
                idade = input("Digite a nova idade: ")
                df.at[professor_index, 'Idade'] = int(idade)  # Converte para inteiro
            elif escolha == '3':
                sexo = input("Digite o novo sexo (M/F): ")
                df.at[professor_index, 'Sexo'] = sexo
            elif escolha == '0':
                print("Modificações finalizadas.")
                break
            else:
                print("Opção inválida. Escolha novamente.")
        
        # Salva o DataFrame modificado
        save_professor_dataframe(df)
        print(f"\nDados do professor com Registro {registro} modificados com sucesso.")
        
        # Printa os dados do professor modificado
        professor_modificado = df.loc[professor_index]
        print(f"Professor modificado:\n{professor_modificado}")
    else:
        print(f"Professor com Registro {registro} não encontrado.")

# Exemplo de uso das funções
#show_all_professors()  # Mostra todos os professores
#search_professor_by_registro(8252)  # Busca por Registro
#add_professor('Novo Professor', 35, 'M', 1234)  # Adiciona professor
#delete_professor_by_registro(1234)  # Exclui professor por Registro
#modify_professor_by_registro(8252)  # Modifica professor por Registro
