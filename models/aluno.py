class Aluno:
    def __init__(self, matricula, nome, idade, curso):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def to_dict(self):  
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'curso': self.curso,
            'idade': self.idade
        }