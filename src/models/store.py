from src.models.user import User


class Store:

    def __init__(self):
        self.bd = [
            User('Thiago', 'Tester'),
            User('Marcos', 'Dev'),
            User('Carlos', 'TI'),
            User('Pedro', 'QA'),
            User('Ana', 'Analista de Sistemas'),
            User('Juliana', 'Desenvolvedora'),
            User('Lucas', 'Suporte Técnico'),
            User('Fernanda', 'Gerente de Projetos'),
            User('Roberto', 'DevOps'),
            User('Mariana', 'Designer'),
            User('Claudio', 'Arquiteto de Software'),
            User('Tatiane', 'Product Owner'),
            User('Ricardo', 'Cibersegurança'),
            User('Larissa', 'Business Analyst'),
            User('Gustavo', 'Data Scientist'),
            User('Camila', 'Front-end Developer')
        ]

