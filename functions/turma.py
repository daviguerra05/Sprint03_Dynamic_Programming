import pandas as pd

# Função para carregar o DataFrame de Turmas
def load_turmas_dataframe():
    return pd.read_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Turmas.csv')

# Função para salvar o DataFrame de Turmas
def save_turmas_dataframe(df):
    df.to_csv(r'C:\Users\labsfiap\Desktop\sprint dynamic\Sprint03_Dynamic_Programming\Tabelas\Turmas.csv', index=False)

# Função para mostrar todas as turmas
def show_all_turmas():
    df = load_turmas_dataframe()
    pd.set_option('display.max_rows', None)
    print(df)

# Função para buscar turma por nome
def search_turma_by_name(nome):
    df = load_turmas_dataframe()
    turma = df[df['Nome'] == nome]
    if not turma.empty:
        print(turma)
    else:
        print(f"Turma com nome {nome} não encontrada.")

# Função para adicionar uma nova turma
def add_turma(nome, periodo, coordenador_responsavel, professor_responsavel):
    df = load_turmas_dataframe()
    
    # Verifica se já existe uma turma com o mesmo nome
    if df[df['Nome'] == nome].empty:
        nova_turma = pd.DataFrame({
            'Nome': [nome],
            'Periodo': [periodo],
            'Coordenador_responsavel': [coordenador_responsavel],
            'Professor_responsavel': [professor_responsavel]
        })
        
        # Concatenar a nova turma com o DataFrame existente
        df = pd.concat([df, nova_turma], ignore_index=True)
        save_turmas_dataframe(df)
        print(f"Turma {nome} adicionada com sucesso.")
    else:
        print(f"Já existe uma turma com o nome {nome}.")

# Função para excluir uma turma por nome
def delete_turma_by_name(nome):
    df = load_turmas_dataframe()
    
    # Verifica se o nome existe
    if not df[df['Nome'] == nome].empty:
        df = df[df['Nome'] != nome]  # Remove a turma com o nome correspondente
        save_turmas_dataframe(df)
        print(f"Turma {nome} excluída com sucesso.")
    else:
        print(f"Turma com nome {nome} não encontrada.")

# Função para modificar turma por nome
def modify_turma_by_name(nome):
    df = load_turmas_dataframe()
    
    # Verifica se a turma existe
    if not df[df['Nome'] == nome].empty:
        turma_index = df[df['Nome'] == nome].index[0]
        print(f"Turma encontrada:\n{df.loc[turma_index]}")
        
        # Menu de opções para modificar atributos
        while True:
            print("\nEscolha o atributo que deseja modificar:")
            print("1 - Nome")
            print("2 - Período")
            print("3 - Coordenador Responsável")
            print("4 - Professor Responsável")
            print("0 - Finalizar modificações")
            
            escolha = input("Digite o número correspondente ao atributo: ")
            
            if escolha == '1':
                novo_nome = input("Digite o novo nome: ")
                df.at[turma_index, 'Nome'] = novo_nome
            elif escolha == '2':
                periodo = input("Digite o novo período: ")
                df.at[turma_index, 'Periodo'] = periodo
            elif escolha == '3':
                coordenador_responsavel = input("Digite o novo coordenador responsável: ")
                df.at[turma_index, 'Coordenador_responsavel'] = coordenador_responsavel
            elif escolha == '4':
                professor_responsavel = input("Digite o novo professor responsável: ")
                df.at[turma_index, 'Professor_responsavel'] = professor_responsavel
            elif escolha == '0':
                print("Modificações finalizadas.")
                break
            else:
                print("Opção inválida. Escolha novamente.")
        
        # Salva o DataFrame modificado
        save_turmas_dataframe(df)
        print(f"\nDados da turma {nome} modificados com sucesso.")
        
        # Printa os dados da turma modificada
        turma_modificada = df.loc[turma_index]
        print(f"Turma modificada:\n{turma_modificada}")
    else:
        print(f"Turma com nome {nome} não encontrada.")

# Exemplo de uso (descomentado se necessário)
#show_all_turmas()                          # Mostra todas as turmas
#search_turma_by_name('5LPNW')               # Busca por nome
#add_turma('9LPNY', 'Matutino', 'John Doe', 'Jane Smith')  # Adiciona turma
#delete_turma_by_name('9LPNY')               # Exclui turma por nome
#modify_turma_by_name('5LPNW')               # Modifica turma por nome
