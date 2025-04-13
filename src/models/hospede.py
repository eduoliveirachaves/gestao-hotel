from src.models.pessoa import Pessoa


class Hospede(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        super().__init__(nome, cpf)
        self.__telefone = telefone
        self.__email = email

    @property
    def nome(self):
        return super().nome

    @property
    def cpf(self):
        return super().cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    #faz sentido ser mutavel? (nome e cpf)
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @email.setter
    def email(self, email):
        self.__email = email


    def exibir_dados(self):
        return (f"Hospede: {super().nome}, cpf: {super().cpf}, "
                f"telefone: {self.__telefone}, email: {self.__email}")


    def __str__(self):
        return (f'Nome: {self.__nome} '
            f'CPF: {self.__cpf} '
            f'Telefone: {self.__telefone} '
            f'Email: {self.__email}')
