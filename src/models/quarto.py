from src.utils.enums.quarto_tipo import QuartoTipo


class Quarto:
    def __init__(self, numero: int, tipo: QuartoTipo, preco_diaria: float, quantidade: float, ocupacao_maxima: float):
        if numero is None or tipo is None or preco_diaria is None:
            raise Exception

        if not isinstance(tipo, QuartoTipo):
            raise Exception

        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = True
        self.__quantidade = quantidade
        self.__ocupacao_maxima = ocupacao_maxima

    @property
    def numero(self):
        return self.__numero

    @property
    def tipo(self):
        return self.__tipo

    @property
    def disponivel(self):
        return self.__disponivel

    @property
    def preco_diaria(self):
        return self.__preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, preco_diaria):
        self.__preco_diaria = preco_diaria

    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def ocupacao_maxima(self):
        return self.__ocupacao_maxima


    def __str__(self):
        return (f"Numero: {self.__numero}\n"
                f"Tipo: {self.__tipo}\n"
                f"Preco: {self.__preco_diaria}\n"
                f"Disponivel: {self.__disponivel}\n"
                f"Quantidade: {self.__quantidade}\n")
