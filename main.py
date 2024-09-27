from functions.aluno import (
    modify_student_by_rm,
    show_all_students,
    search_student_by_rm,
    add_student,
    delete_student_by_rm
)
from functions.turma import (
    show_all_turmas,
    search_turma_by_name,
    add_turma,
    delete_turma_by_name,
    modify_turma_by_name
)
from functions.professor import (
    show_all_professors,
    search_professor_by_registro,
    add_professor,
    delete_professor_by_registro,
    modify_professor_by_registro
)

def main():
    while True:
        op = int(input("Digite\n 1 para professor\n 2 para coordenadores\n 0 para sair: "))
        if op == 1:
            senha = input("Digite a senha: ")
            if senha == "lepic":
                while True:
                    op2 = int(input(
                        "Digite:\n"
                        "1 para ver todos os alunos\n"
                        "2 para buscar aluno por RM\n"
                        "3 para modificar aluno\n"
                        "4 para adicionar aluno\n"
                        "5 para deletar aluno\n"
                        "0 para sair\n"
                    ))

                    if op2 == 1:
                        show_all_students()
                    elif op2 == 2:
                        rm = int(input("Digite o RM do aluno a ser buscado: "))
                        search_student_by_rm(rm)
                    elif op2 == 3:
                        rm = int(input("Digite o RM do aluno a ser modificado: "))
                        modify_student_by_rm(rm)
                    elif op2 == 4:
                        nome = input("Digite o nome do aluno: ")
                        idade = int(input("Digite a idade do aluno: "))
                        sexo = input("Digite o sexo do aluno (M/F): ")
                        turma = input("Digite a turma do aluno: ")
                        rm = int(input("Digite o RM do aluno: "))
                        pontuacao = float(input("Digite a pontuação do aluno: "))
                        num_simulacoes = int(input("Digite o número de simulações do aluno: "))
                        num_insignias = int(input("Digite o número de insígnias do aluno: "))
                        add_student(nome, idade, sexo, turma, rm, pontuacao, num_simulacoes, num_insignias)
                    elif op2 == 5:
                        rm = int(input("Digite o RM do aluno a ser deletado: "))
                        delete_student_by_rm(rm)
                    elif op2 == 0:
                        print("Saindo do menu de operações do professor.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Senha incorreta.")
        
        elif op == 2:
            senha = input("Digite a senha dos coordenadores: ")
            if senha == "lepic":
                while True:
                    opcao = int(input(
                        "Digite:\n"
                        "1 para manipulação de turmas\n"
                        "2 para manipulação de professores\n"
                        "0 para sair\n"
                    ))
                    if opcao == 1:
                        while True:
                            op2 = int(input(
                                "Digite:\n"
                                "1 para ver todas as turmas\n"
                                "2 para buscar turma por nome\n"
                                "3 para adicionar turma\n"
                                "4 para deletar turma\n"
                                "5 para modificar turma\n"
                                "0 para sair\n"
                            ))

                            if op2 == 1:
                                show_all_turmas()
                            elif op2 == 2:
                                nome = input("Digite o nome da turma a ser buscada: ")
                                search_turma_by_name(nome)
                            elif op2 == 3:
                                nome = input("Digite o nome da turma a ser adicionada: ")
                                periodo=input ("digite o periodo da turma")
                                coordenador_responsavel=input ("digite o coordenador_responsavel da turma")
                                professor_responsavel= input ("digite o professor_responsavel da turma")
                                add_turma(nome,periodo,coordenador_responsavel,professor_responsavel)
                            elif op2 == 4:
                                nome = input("Digite o nome da turma a ser deletada: ")
                                delete_turma_by_name(nome)
                            elif op2 == 5:
                                nome_antigo = input("Digite o nome da turma a ser modificada: ")
                                modify_turma_by_name(nome)
                            elif op2 == 0:
                                print("Saindo do menu de operações dos coordenadores.")
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                    
                    elif opcao == 2:
                        while True:
                            op3 = int(input(
                                "Digite:\n"
                                "1 para ver todos os professores\n"
                                "2 para buscar professor por registro\n"
                                "3 para adicionar professor\n"
                                "4 para deletar professor\n"
                                "5 para modificar professor\n"
                                "0 para sair\n"
                            ))

                            if op3 == 1:
                                show_all_professors()
                            elif op3 == 2:
                                registro = int(input("Digite o registro do professor a ser buscado: "))
                                search_professor_by_registro(registro)
                            elif op3 == 3:
                                nome = input("Digite o nome do professor: ")
                                idade = int(input("Digite a idade do professor: "))
                                registro = int(input("Digite o registro do professor: "))
                                disciplina = input("Digite a disciplina do professor: ")
                                add_professor(nome, idade, registro, disciplina)
                            elif op3 == 4:
                                registro = int(input("Digite o registro do professor a ser deletado: "))
                                delete_professor_by_registro(registro)
                            elif op3 == 5:
                                registro = int(input("Digite o registro do professor a ser modificado: "))
                                modify_professor_by_registro(registro)
                            elif op3 == 0:
                                print("Saindo do menu de operações dos coordenadores.")
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
            else:
                print("Senha incorreta.")
        
        elif op == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()
