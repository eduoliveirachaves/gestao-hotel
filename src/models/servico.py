from src.utils.enums.servico_categoria import ServicoCategoria


class Servico:
    def __init__(self, preco: float, categoria: ServicoCategoria):
        self.__preco = preco
        self.__categoria = categoria

    @property
    def preco(self):
        return self.__preco

    @property
    def categoria(self):
        return self.__categoria

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria


    def __str__(self):
        return (f"Categoria: {self.__categoria} "
                f"Preco {self.__preco}")
