from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    def exibir_dados(self):
        pass
