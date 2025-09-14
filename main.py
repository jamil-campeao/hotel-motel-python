from Hotel import Hotel
from Motel import Motel
from Quarto import Quarto

def menu_hotel(hotel: Hotel):
    while True:
        print(f" --- Menu do Hotel {hotel.nome}---")
        print(" 1 - Fazer Check-in")
        print(" 2 - Fazer Check-out")
        print(" 3 - Listar Quartos")
        print(" 4 - Regredir ao menu principal")

        try: 
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                nome = input("Digite o nome do hóspede: ")
                cpf = input("Digite o cpf do hóspede: ")
                quarto = hotel.check_in(nome, cpf)

                if quarto:
                    print(f"Check-in realizado com sucesso! Hóspede {nome} alocado no quarto {quarto.numero}.")
                else:
                    print("Desculpe, não há quartos disponíveis no momento.")

            elif opcao == 2:
                try:
                    num_quarto = int(input("Digite o número do quarto para check_out: "))

                    resultado = hotel.check_out(numero_quarto=num_quarto)

                    if resultado.get('sucesso'):
                        print("\n--- Recibo do Check-out ---")
                        print(f"Quarto: {resultado['numero_quarto']}")
                        print(f"Data Check-in: {resultado['data_checkin']}")
                        print(f"Data Check-out: {resultado['data_checkout']}")
                        print(f"Valor a pagar: R$ {resultado['valor_a_pagar']:.2f}")
                        print("-----------------------------")
                    else:
                        print(f"Erro: {resultado['mensagem']}")
                except ValueError:
                    print("Número do quarto inválido. Tente novamente")

            elif opcao == 3:
                print("Status dos quartos")
                for quarto in hotel.quartos:
                    print(quarto)
            elif opcao == 4:
                break
            else:
                print('Opção inválida')
        
        except Exception as e:
            print(f'Erro: {str(e)}')

def menu_motel(motel: Motel):
    while True:
        print("\n--- Menu do Motel '{}' ---".format(motel.nome))
        print("1. Fazer Check-in")
        print("2. Fazer Check-out")
        print("3. Listar Quartos")
        print("4. Voltar ao Menu Principal")
        
        try:
            opcao = int(input("Escolha uma opção: "))


            if opcao == 1:
                quarto = motel.check_in()
                if quarto:
                    print(f"Check-in realizado com sucesso! Quarto {quarto.numero} está ocupado.")
                else:
                    print("Desculpe, não há quartos disponíveis no momento.")

            elif opcao == 2:
                try:
                    num_quarto = int(input("Digite o número do quarto para check-out: "))
                    resultado = motel.check_out(num_quarto)
                    if resultado["sucesso"]:
                        print("\n--- Recibo do Check-out ---")
                        print(f"Quarto: {resultado['numero_quarto']}")
                        print(f"Data Check-in: {resultado['data_checkin']}")
                        print(f"Data Check-out: {resultado['data_checkout']}")
                        print(f"Valor a pagar: R$ {resultado['valor_a_pagar']:.2f}")
                        print("-----------------------------")
                    else:
                        print(f"Erro: {resultado['mensagem']}")
                except ValueError:
                    print("Número do quarto inválido. Tente novamente.")
            
            elif opcao == 3:
                print("\n--- Status dos Quartos ---")
                for quarto in motel.quartos:
                    print(quarto)

            elif opcao == 4:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro: {str(e)}")


def main():
    # --- Configuração inicial do sistema ---
    quartos_hotel = [Quarto(101, 150.0), Quarto(102, 150.0), Quarto(201, 200.0), Quarto(202, 250.0)]
    meu_hotel = Hotel("Hotel Palace", quartos_hotel)

    quartos_motel = [Quarto(1, 40.0), Quarto(2, 40.0), Quarto(3, 55.0), Quarto(4, 55.0)]
    meu_motel = Motel("Motel Stardust", quartos_motel)

    while True:
        print("\n===== SISTEMA DE GERENCIAMENTO HOTELEIRO =====")
        print("1. Gerenciar Hotel")
        print("2. Gerenciar Motel")
        print("3. Sair")
        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            menu_hotel(meu_hotel)
        elif escolha == 2:
            menu_motel(meu_motel)
        elif escolha == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()