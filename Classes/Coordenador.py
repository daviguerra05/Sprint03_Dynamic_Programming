class Coordenador:
    def __init__(self, id: int, nome: str, idade: int, sexo: str, registro: int):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.registro = registro

    # Métodos get e set para registro
    def getRegistro(self) -> int:
        return self.registro

    def setRegistro(self, registro: int) -> None:
        self.registro = registro

    # Representação da classe em string
    def __str__(self) -> str:
        return (f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, "
                f"Registro: {self.registro}")
