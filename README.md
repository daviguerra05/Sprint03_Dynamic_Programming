# Projeto: Gerenciamento de Tabelas de Alunos, Professores, Coordenadores e Turmas

Este projeto realiza o carregamento de dados de diferentes tabelas relacionadas a uma instituição de ensino, utilizando a biblioteca `pandas` para leitura de arquivos CSV. As tabelas carregadas representam informações sobre **alunos**, **professores**, **coordenadores** e **turmas**. O projeto organiza essas informações utilizando classes específicas para cada tipo de dado.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - `pandas`: Utilizada para manipulação e leitura dos dados em formato CSV.

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/daviguerra05/Sprint03_Dynamic_Programming.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd repositorio
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install pandas
   ```

## Arquitetura do Projeto

O projeto é composto por várias classes, organizadas no módulo `Classes.py`, cada uma responsável por manipular dados de uma tabela específica:

- **TabelaAlunos**: Gerencia dados dos alunos.
- **TabelaProfessores**: Gerencia dados dos professores.
- **TabelaCoordenadores**: Gerencia dados dos coordenadores.
- **TabelaTurmas**: Gerencia dados das turmas.

Os dados são carregados a partir de arquivos CSV localizados na pasta `Tabelas` e são manipulados como `dataframes` do `pandas` para facilitar as operações de consulta.

### Estrutura do Código

O código principal faz a leitura dos arquivos CSV correspondentes e utiliza as classes importadas para organizar os dados:

```python
import pandas as pd
from Classes import TabelaAlunos, TabelaTurmas, TabelaCoordenadores, TabelaProfessores

def receber_dados_alunos():
    return TabelaAlunos.TabelaAlunos(pd.read_csv('./Tabelas/alunos.csv')) 

def receber_dados_professores():
    return TabelaProfessores.TabelaProfessores(pd.read_csv('./Tabelas/professores.csv'))

def receber_dados_coordenadores():
    return TabelaCoordenadores.TabelaCoordenadores(pd.read_csv('./Tabelas/coordenadores.csv'))

def receber_dados_turmas():
    return TabelaTurmas.TabelaTurmas(pd.read_csv('./Tabelas/turmas.csv'))
```

### Descrição das Funções

- **receber_dados_alunos()**: Carrega e retorna os dados dos alunos a partir do arquivo `alunos.csv`.
- **receber_dados_professores()**: Carrega e retorna os dados dos professores a partir do arquivo `professores.csv`.
- **receber_dados_coordenadores()**: Carrega e retorna os dados dos coordenadores a partir do arquivo `coordenadores.csv`.
- **receber_dados_turmas()**: Carrega e retorna os dados das turmas a partir do arquivo `turmas.csv`.

### Estrutura de Diretórios

```bash
.
├── Classes
│   ├── __init__.py
│   ├── Aluno.py
│   ├── Coordenador.py
│   ├── Professor.py
│   ├── TabelaAlunos.py
│   ├── TabelaCoordenadores.py
│   ├── TabelaProfessores.py
│   ├── TabelaTurmas.py
│   └── Turma.py
├── main.py
└── Tabelas
    ├── alunos.csv
    ├── professores.csv
    ├── coordenadores.csv
    └── turmas.csv
```

### Como Executar

1. Coloque seus arquivos CSV na pasta `Tabelas`.
2. Execute o script principal (`main.py`) para carregar os dados e utilizá-los nas operações necessárias:
   ```bash
   python main.py
   ```


# Sistema de Gerenciamento de Alunos

Este projeto contém classes para gerenciar dados de alunos e turmas em um sistema de escola. Ele permite a criação, leitura, atualização e exclusão (CRUD) de registros de alunos, bem como análises descritivas e manipulações nos dados.

## Classes Principais

### 1. `Aluno`
A classe `Aluno` é responsável por armazenar os dados de um aluno individual.

#### Atributos:
- `Nome`: Nome do aluno.
- `Idade`: Idade do aluno.
- `Sexo`: Sexo do aluno.
- `Turma`: Turma à qual o aluno pertence.
- `Rm`: Registro do aluno (deve ter 6 dígitos).
- `Pontuacao`: Pontuação do aluno em avaliações/simulações.
- `Num_simulacoes`: Número de simulações realizadas pelo aluno.
- `Num_insignias`: Número de insígnias obtidas pelo aluno.

#### Métodos:
- `getDados()`: Retorna todos os dados do aluno como uma lista.

### 2. `TabelaAlunos`
A classe `TabelaAlunos` é responsável por realizar operações em um DataFrame que contém dados de múltiplos alunos.

#### Atributos:
- `df`: O DataFrame que contém os dados dos alunos.

#### Funcionalidades Principais:

##### Estatísticas Descritivas:
- `media_pontuacao_turma()`: Exibe a média de pontuação por turma.
- `mediana_pontuacao_turma()`: Exibe a mediana de pontuação por turma.
- `media_pontuacao_idade()`: Exibe a média de pontuação por idade.
- `mediana_pontuacao_idade()`: Exibe a mediana de pontuação por idade.
- `media_pontuacao_sexo()`: Exibe a média de pontuação por sexo.
- `mediana_pontuacao_sexo()`: Exibe a mediana de pontuação por sexo.

##### Correlações:
- `correlacaoPontuacao()`: Exibe a correlação entre pontuação, número de simulações e número de insígnias.

##### Desempenho Geral:
- `media_geral()`: Exibe a média geral da pontuação dos alunos.
- `melhores_pontuacoes()`: Exibe as 10 maiores pontuações.
- `distribuicao_pontuacao()`: Exibe a distribuição de pontuações em um gráfico.

##### Simulações:
- `media_simulacoes_realizadas_por_turma()`: Exibe a média de simulações realizadas por turma.
- `pontuaca_media_por_quantidade_simulacoes()`: Exibe a pontuação média por número de simulações realizadas.

##### Insígnias:
- `distribuicao_insignias()`: Exibe a distribuição de insígnias.
- `pontuacao_por_numero_insignias()`: Exibe a pontuação média por número de insígnias.

##### Funções de CRUD (Gerenciamento de Alunos):
- `search_student_by_rm(rm)`: Busca um aluno pelo número de RM.
- `add_student(nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias)`: Adiciona um novo aluno ao sistema após validar os dados.
- `delete_student_by_rm(rm)`: Remove um aluno do sistema baseado no RM.
- `modify_student_by_rm(rm, novo_nome=None, nova_idade=None)`: Modifica os dados de um aluno específico pelo RM.

### Observações:
- A pontuação máxima de um aluno é definida como o número de simulações multiplicado por 1000.
- O número máximo de simulações permitidas é 3.
- O número máximo de insígnias permitidas é 15.
- A idade mínima para um aluno é de 18 anos.



# Gerenciamento de Turmas

Este projeto implementa uma estrutura para gerenciar turmas em uma instituição de ensino, com operações de CRUD (Create, Read, Update, Delete). Abaixo, uma descrição detalhada das classes `Turma` e `TabelaTurmas`, assim como suas funcionalidades.

## Estrutura do Projeto

### Arquivo `turma.py`
Este arquivo contém a classe `Turma`, que define os atributos básicos de uma turma.

```python
class Turma:
    def __init__(self, Nome, Periodo, Coordenador_responsavel, Professor_responsavel) -> None:
        self.Nome = Nome
        self.Periodo = Periodo
        self.Coordenador_responsavel = Coordenador_responsavel
        self.Professor_responsavel = Professor_responsavel
```

#### Atributos:
- **Nome**: Nome da turma.
- **Período**: O período da turma (ex: manhã, tarde, noite).
- **Coordenador_responsável**: Nome do coordenador responsável pela turma.
- **Professor_responsável**: Nome do professor responsável pela turma.



### Arquivo `tabelaturmas.py`
Este arquivo contém a classe `TabelaTurmas`, que realiza a gestão e operações sobre as turmas armazenadas em um DataFrame.

```python
import seaborn as sns
import pandas as pd
```

#### Construtor:
- `__init__(self, dataframe)` - Recebe um DataFrame contendo os dados das turmas.

#### Funcionalidades:
1. **Distribuição por Período**:
    - `distribuicao_periodo(self)` - Exibe a distribuição das turmas por período usando um gráfico de distribuição.
  
    ```python
    def distribuicao_periodo(self):
        sns.displot(data=self.df, x='Periodo')
    ```

2. **Listagem de Nomes**:
    - `getNomes(self)` - Retorna uma lista com os nomes de todas as turmas.

    ```python
    def getNomes(self):
        return list(self.df['Nome'])
    ```

3. **Adicionar Turma**:
    - `adicionarTurma(self, Turma)` - Adiciona uma nova turma ao DataFrame, verificando se o professor e coordenador estão presentes no banco de dados, além de evitar duplicatas.

    ```python
    def adicionarTurma(self, Turma):
        professores = list(pd.read_csv('./Tabelas/professores.csv')['Nome'])
        coordenadores = pd.read_csv('./Tabelas/coordenadores.csv')

        if self.df[self.df['Nome'] == Turma.Nome].empty:
            # Verificações de professor e coordenador
            if Turma.Professor_responsavel not in professores:
                print('Professor não existe no banco de dados.')
                return

            if Turma.Coordenador_responsavel not in coordenadores['Nome'].values:
                print('Coordenador não existe no banco de dados.')
                return

            novo_Turma = pd.DataFrame({
                'Nome': Turma.Nome,
                'Periodo': Turma.Periodo,
                'Coordenador_responsavel': Turma.Coordenador_responsavel,
                'Professor_responsavel': Turma.Professor_responsavel
            })

            self.df = pd.concat([self.df, novo_Turma], ignore_index=True)
            self.salvar_dataset()
            print(f"Turma de Nome {Turma.Nome} adicionada com sucesso.")
        else:
            print(f"Já existe uma turma com o Nome {Turma.Nome}.")
    ```

4. **Excluir Turma**:
    - `deletar_Turma_por_Nome(self, Nome)` - Exclui uma turma com base no seu nome.

    ```python
    def deletar_Turma_por_Nome(self, Nome):
        if not self.df[self.df['Nome'] == Nome].empty:
            self.df = self.df[self.df['Nome'] != Nome]
            self.salvar_dataset()
            print(f"Turma com Nome {Nome} excluída com sucesso.")
        else:
            print(f"Turma com Nome {Nome} não encontrada.")
    ```

5. **Modificar Turma**:
    - `modificar_Turma_por_Nome(self, novo_periodo=None, Nome=None)` - Modifica o período de uma turma com base no seu nome.

    ```python
    def modificar_Turma_por_Nome(self, novo_periodo=None, Nome=None):
        if Nome and not self.df[self.df['Nome'] == Nome].empty:
            turma_index = self.df[self.df['Nome'] == Nome].index[0]
            if novo_periodo:
                self.df.at[turma_index, 'Periodo'] = novo_periodo
            self.salvar_dataset()
            print(f"\nDados da turma com Nome {Nome} modificados com sucesso.")
        else:
            print(f"Turma com Nome {Nome} não encontrada.")
    ```

6. **Salvar DataFrame**:
    - `salvar_dataset(self)` - Salva o DataFrame de turmas no arquivo `turmas.csv`.

    ```python
    def salvar_dataset(self):
        self.df.to_csv('./Tabelas/turmas.csv', index=False)
    ```



### Arquivos CSV:
Os dados das turmas são armazenados no arquivo `./Tabelas/turmas.csv`. Além disso, o sistema depende de dois arquivos adicionais para verificar a existência de professores e coordenadores:
- `./Tabelas/professores.csv`
- `./Tabelas/coordenadores.csv`



## Como Usar

1. **Carregar DataFrame**:
   Inicialize a classe `TabelaTurmas` passando um DataFrame com os dados das turmas.

   ```python
   df = pd.read_csv('./Tabelas/turmas.csv')
   tabela_turmas = TabelaTurmas(df)
   ```

2. **Adicionar uma Turma**:
   Para adicionar uma turma, crie uma instância da classe `Turma` e passe-a para o método `adicionarTurma`.

   ```python
   nova_turma = Turma('Turma A', 'Manhã', 'Coordenador X', 'Professor Y')
   tabela_turmas.adicionarTurma(nova_turma)
   ```

3. **Excluir uma Turma**:
   Use o método `deletar_Turma_por_Nome` para excluir uma turma.

   ```python
   tabela_turmas.deletar_Turma_por_Nome('Turma A')
   ```

4. **Modificar o Período de uma Turma**:
   Utilize o método `modificar_Turma_por_Nome` para alterar o período de uma turma específica.

   ```python
   tabela_turmas.modificar_Turma_por_Nome(novo_periodo='Noite', Nome='Turma A')
   ```

5. **Visualizar a Distribuição das Turmas**:
   Gere um gráfico de distribuição dos períodos das turmas.

   ```python
   tabela_turmas.distribuicao_periodo()
   ```


# Sistema de Professores

## Introdução
Este sistema gerencia informações sobre professores, utilizando classes para representar professores individuais e uma tabela de professores para realizar operações como inserção, exclusão, e modificação de dados. A tabela de professores também fornece estatísticas descritivas e visualizações gráficas dos dados.

### Estrutura do Projeto

- `professor.py`: Define a classe `Professor`, que representa um professor individual.
- `tabelaprofessor.py`: Define a classe `TabelaProfessores`, que é responsável pela manipulação dos dados dos professores e inclui métodos para estatísticas, visualizações e operações CRUD (Create, Read, Update, Delete).



## `professor.py`

### Classe `Professor`

A classe `Professor` é responsável por armazenar os atributos de um professor.

#### Atributos:

- **Nome**: Nome do professor.
- **Idade**: Idade do professor.
- **Sexo**: Sexo do professor.
- **Registro**: Identificação única do professor.


### Classe `TabelaProfessores`

Esta classe gerencia um conjunto de professores através de um DataFrame do Pandas. Ela oferece funcionalidades para manipular os dados, gerar estatísticas e criar visualizações gráficas.

#### Atributos:

- **df**: DataFrame que armazena os dados dos professores.

#### Métodos:

##### 1. **show()**
Exibe o DataFrame atual com todos os professores.

##### 2. **Estatísticas Descritivas**
- **media_idade_sexo()**: Exibe a média de idade por sexo.
- **mediana_idade_sexo()**: Exibe a mediana da idade por sexo.
- **media_geral_idade()**: Exibe a média geral da idade dos professores.
- **maiores_idades()**: Exibe as 10 maiores idades.
- **distribuicao_idade()**: Exibe um gráfico de distribuição das idades dos professores.

##### 3. **Atualização da Tabela**
- **salvar_dataset()**: Salva o DataFrame atualizado no arquivo CSV `professores.csv`.

##### 4. **Operações CRUD**

###### Create:
- **adicionarProfessor(Professor)**: Adiciona um novo professor ao DataFrame e ao arquivo CSV, verificando se o registro já existe. O registro deve ter até 5 caracteres.

###### Delete:
- **deletar_professor_por_registro(registro)**: Remove um professor do DataFrame e do CSV, baseado no seu registro.

###### Update:
- **modificar_professor_por_registro(novo_nome=None, nova_idade=None, Registro=None)**: Permite modificar o nome ou a idade de um professor, baseado no registro.



#  Sistema de Coordenadores

## Introdução
Este sistema gerencia informações sobre coordenadores, utilizando classes para representar coordenadores individuais e uma tabela de coordenadores para realizar operações como inserção, exclusão e modificação de dados. A tabela também oferece uma visualização gráfica da distribuição de coordenadores por idade e sexo.

### Estrutura do Projeto

- `cordenador.py`: Define a classe `Coordenador`, que representa um coordenador individual.
- `tabelacordenador.py`: Define a classe `TabelaCoordenadores`, que é responsável pela manipulação dos dados dos coordenadores, além de incluir métodos para visualizações gráficas e operações CRUD (Create, Read, Update, Delete).



## `cordenador.py`

### Classe `Coordenador`

A classe `Coordenador` é responsável por armazenar os atributos de um coordenador.

#### Atributos:

- **Nome**: Nome do coordenador.
- **Idade**: Idade do coordenador.
- **Sexo**: Sexo do coordenador.
- **Registro**: Identificação única do coordenador.

## `tabelacordenador.py`

### Classe `TabelaCoordenadores`

Esta classe gerencia um conjunto de coordenadores através de um DataFrame do Pandas. Ela oferece funcionalidades para manipular os dados, gerar visualizações gráficas e realizar operações CRUD.

#### Atributos:

- **df**: DataFrame que armazena os dados dos coordenadores.

#### Métodos:

##### 1. **Visualização Gráfica**
- **grafico_sexo_por_idade()**: Gera um gráfico de barras que exibe a distribuição de coordenadores por idade e sexo.

##### 2. **Atualização da Tabela**
- **salvar_dataset()**: Salva o DataFrame atualizado no arquivo CSV `coordenadores.csv`.

##### 3. **Operações CRUD**

###### Create:
- **adicionarcoordenador(coordenador)**: Adiciona um novo coordenador ao DataFrame e ao arquivo CSV, verificando se o registro já existe. O registro deve ter até 5 caracteres.

###### Delete:
- **deletar_coordenador_por_registro(registro)**: Remove um coordenador do DataFrame e do CSV, baseado no seu registro.

###### Update:
- **modificar_coordenador_por_registro(novo_nome=None, nova_idade=None, Registro=None)**: Permite modificar o nome ou a idade de um coordenador, baseado no registro.
