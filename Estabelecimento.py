from Quarto import Quarto
from abc import ABC, abstractmethod
from datetime import datetime

class Estabelecimento(ABC):
    def __init__(self, nome: str, quartos: list[Quarto]):
        self.nome = nome
        self.quartos = quartos

    def procurar_quarto_disponivel(self):
        for quarto in self.quartos:
            if not quarto.ocupado:
                return quarto
    

    def procurar_quarto_por_numero(self, numero: int):
        for quarto in self.quartos:
            if quarto.numero == numero:
                print('quarto encontrado!')
                return quarto
            
    def check_out(self, numero_quarto: int) -> dict:
        quarto = self.procurar_quarto_por_numero(numero_quarto)

        if quarto:

            data_checkout = datetime.now()
            valor_a_pagar = self.calcular_valor(quarto, data_checkout)

            info = {
                "sucesso": True,
                "numero_quarto": numero_quarto,
                "data_checkin": datetime.now(),
                "data_checkout": data_checkout,
                "valor_a_pagar": valor_a_pagar,
            }

            quarto.desocupar()

            return info
        else:
            return {
                "sucesso": False,
                "mensagem": "Quartão não encontrado ou já está vago",
            }
    @abstractmethod    
    def check_in(self):
        pass

    @abstractmethod
    def calcular_valor(self, quarto: Quarto, data_checkout: datetime) -> float:
        pass
            
    