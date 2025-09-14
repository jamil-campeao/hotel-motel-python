from Hospede import Hospede
from datetime import datetime

class Quarto():
    def __init__(self, numero: int, preco: float):
        self.numero = numero
        self.preco = preco
        self.ocupado = False
        self.hospede = None
        self.data_checkin = None

    def ocupar(self, data_checkin: datetime, hospede: Hospede):
        self.data_checkin = data_checkin
        self.ocupado = True
        self.hospede = hospede

    def desocupar(self):
        self.ocupado = False
        self.data_checkin = None
        self.hospede = None

    def __str__(self):
        status = "Ocupado" if self.ocupado else "Livre"

        if self.hospede:
            hospede_info = f""" Dados hóspede: {self.hospede.nome} : [{self.hospede.cpf}]"""
        else:
            hospede_info = ""

        return f""" Quarto número: {self.numero} 
                    Status: {status}
                    {hospede_info} """