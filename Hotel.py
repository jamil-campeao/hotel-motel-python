from Estabelecimento import Estabelecimento
from Hospede import Hospede
from Quarto import Quarto
from datetime import datetime
import math

class Hotel(Estabelecimento):
    def __init__(self, nome, quartos: list[Quarto]):
        self.nome = nome
        self.quartos = quartos

    def check_in(self, nome_hospede: str, cpf_hospede: str):
        quarto = self.procurar_quarto_disponivel()

        if quarto:
            hospede = Hospede(nome=nome_hospede, cpf=cpf_hospede)
            quarto.ocupar(datetime.now(), hospede)
            return quarto
        else:
            return None

    def calcular_valor(self, quarto: Quarto, data_checkout: datetime) -> float:
        delta_tempo = data_checkout - quarto.data_checkin
        dias = delta_tempo.days

        # Se ficou menos de 24h, cobra 1 diária.
        if delta_tempo.total_seconds() > 0 and dias == 0:
            dias = 1
        # Se passou um pouco de uma diária, arredonda para cima.
        elif delta_tempo.total_seconds() % (24 * 3600) > 0:
            dias = math.ceil(delta_tempo.total_seconds() / (24 * 3600))

        return dias * quarto.preco