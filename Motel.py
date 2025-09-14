from Estabelecimento import Estabelecimento
from Quarto import Quarto
from Hospede import Hospede
from datetime import datetime
import math

class Motel(Estabelecimento):
    def __init__(self, nome: str, quartos: list[Quarto]):
        self.nome = nome
        self.quartos = quartos

    def check_in(self):
        quarto = self.procurar_quarto_disponivel()

        if quarto:
            quarto.ocupar(datetime.now())
            return quarto
        else:
            return None

    def calcular_valor(self, quarto: Quarto, data_checkout: datetime) -> float:
        delta_tempo = data_checkout - quarto.data_checkin

        horas = math.ceil(delta_tempo.total_seconds() / 3600)

        if horas == 0:
            horas = 1

        return horas * quarto.preco