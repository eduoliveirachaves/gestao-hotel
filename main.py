from src.models.hospede import Hospede
from src.models.quarto import Quarto
from src.models.reserva import Reserva
from src.models.servico import Servico
from src.utils.enums.quarto_tipo import QuartoTipo
from src.utils.enums.servico_categoria import ServicoCategoria
from datetime import datetime

def main():
    hospede = Hospede(nome="John Doe", cpf="12345678900", telefone="(11) 98765-4321", email="john.doe@example.com")
    print(hospede.exibir_dados())

    quarto = Quarto(numero=101, tipo=QuartoTipo.LUXO, preco_diaria=300.0, quantidade=1, ocupacao_maxima=2)
    print(f"Quarto: {quarto.numero}, Tipo: {quarto.tipo}, Preço Diária: {quarto.preco_diaria}")

    servico1 = Servico(preco=50.0, categoria=ServicoCategoria.ALIMENTACAO)
    servico2 = Servico(preco=100.0, categoria=ServicoCategoria.LIMPEZA)
    print(servico1)
    print(servico2)

    data_checkin = datetime(2023, 10, 1)
    data_checkout = datetime(2023, 10, 5)
    reserva = Reserva(hospede=hospede, quarto=quarto, data_checkin=data_checkin, data_checkout=data_checkout)

    reserva.adicionar_servico(servico1)
    reserva.adicionar_servico(servico2)

    total = reserva.calcular_total()
    print(f"Total da reserva: {total}")

main()