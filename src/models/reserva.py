from src.models.quarto import Quarto
from src.models.hospede import Hospede
from datetime import datetime

from src.models.servico import Servico


class Reserva:
    def __init__(self, hospede: Hospede, quarto: Quarto, data_checkin: datetime, data_checkout: datetime):
        if not isinstance(hospede, Hospede):
            raise Exception
        if not isinstance(quarto, Quarto):
            raise Exception
        if not isinstance(data_checkin, datetime) or not isinstance(data_checkout, datetime):
            raise Exception

        self.__hospede = hospede
        self.__quarto = quarto
        self.__servicos_adicionais = []
        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout
        self.__ativa = True

    @property
    def hospede(self):
        return self.__hospede

    @hospede.setter
    def hospede(self, hospede):
        self.__hospede = hospede

    @property
    def quarto(self):
        return self.__quarto

    @quarto.setter
    def quarto(self, quarto: Quarto):
        self.__quarto = quarto

    @property
    def servicos_adicionais(self):
        return self.__servicos_adicionais

    @property
    def data_checkin(self):
        return self.__data_checkin

    @data_checkin.setter
    def data_checkin(self, data):
        self.__data_checkin = data

    @property
    def data_checkout(self):
        return self.__data_checkout

    @data_checkout.setter
    def data_checkout(self, data):
        self.__data_checkout = data

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, value):
        self.__ativa = value

    def adicionar_servico(self, servico):
        if not isinstance(servico, Servico):
            raise Exception("arg nao eh do tipo servico")
        self.__servicos_adicionais.append(servico)

    def remover_servico(self, servico):
        if servico in self.__servicos_adicionais:
            self.__servicos_adicionais.remove(servico)

    # for controller!
    def calcular_total(self):
        total_diaria = self.__quarto.preco_diaria * (self.__data_checkout - self.__data_checkin).days
        if len(self.__servicos_adicionais) > 0:
            total_servicos = sum(servico.preco for servico in self.__servicos_adicionais)
            return total_diaria + total_servicos

        return total_diaria

    def __str__(self):
        return (f"Quarto: {self.__quarto}"
                f"\nHospede: {self.__hospede}"
                f"\nServicos: {self.__servicos_adicionais}"
                f"\nCheckIn: {self.__data_checkin}"
                f"\nCheckOut: {self.__data_checkout}")
