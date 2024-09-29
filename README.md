# Gerenciamento de Alunos, Turmas e Professores

Este projeto é uma aplicação interativa em Python para gerenciar alunos, turmas e professores. A aplicação oferece um menu onde professores e coordenadores podem acessar diferentes funcionalidades de acordo com seu nível de acesso. A aplicação realiza operações como adicionar, modificar, deletar e buscar informações de alunos, turmas e professores. 

## Funcionalidades

### Professores
Acesso disponível após fornecer a senha correta ("lepic"). As operações permitidas incluem:

1. **Visualizar todos os alunos**: Exibe uma lista de todos os alunos registrados.
2. **Buscar aluno por RM**: Permite buscar um aluno específico pelo seu número de registro (RM).
3. **Modificar aluno**: Modifica as informações de um aluno a partir de seu RM.
4. **Adicionar aluno**: Adiciona um novo aluno ao sistema.
5. **Deletar aluno**: Remove um aluno do sistema com base em seu RM.

### Coordenadores
Coordenadores também têm acesso mediante senha ("lepic"). Eles podem gerenciar tanto turmas quanto professores:

#### Gerenciamento de Turmas:
1. **Visualizar todas as turmas**: Exibe uma lista de todas as turmas registradas.
2. **Buscar turma por nome**: Busca uma turma específica pelo nome.
3. **Adicionar turma**: Permite adicionar uma nova turma ao sistema.
4. **Deletar turma**: Remove uma turma existente do sistema.
5. **Modificar turma**: Modifica as informações de uma turma.

#### Gerenciamento de Professores:
1. **Visualizar todos os professores**: Exibe uma lista de todos os professores registrados.
2. **Buscar professor por registro**: Busca um professor específico pelo número de registro.
3. **Adicionar professor**: Adiciona um novo professor ao sistema.
4. **Deletar professor**: Remove um professor do sistema com base no número de registro.
5. **Modificar professor**: Modifica as informações de um professor a partir do registro.

## Requisitos

- Python 3.x
- Bibliotecas internas:
  - `functions.aluno`: Funções relacionadas à gestão de alunos.
  - `functions.turma`: Funções relacionadas à gestão de turmas.
  - `functions.professor`: Funções relacionadas à gestão de professores.

## Como Executar

1. Clone o repositório.
2. Certifique-se de que as funções para `aluno`, `turma`, e `professor` estão corretamente implementadas no diretório `functions`.
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Escolha as opções de acordo com o menu para acessar as funcionalidades de professores ou coordenadores.

## Estrutura de Diretórios

```
project/
│
├── main.py                  # Arquivo principal
├── functions/
│   ├── aluno.py             # Funções de gerenciamento de alunos
│   ├── turma.py             # Funções de gerenciamento de turmas
│   └── professor.py         # Funções de gerenciamento de professores
```

