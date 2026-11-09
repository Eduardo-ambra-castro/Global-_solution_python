
import os
os.system("cls")

while True:
    print("\nBem-vindo ao Smart Way - Sistema de Transporte Metropolitano de São Paulo")
    print("1- Consultar linhas do metrô")
    print("2- Consultar lotação das linhas")
    print("3- Consultar lotação por vagão")
    print("4- Consultar horários de menor movimento")
    print("5- Consultar informações de acessibilidade")
    print("6- Registrar uma ocorrência")
    print("7- Sair do sistema")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\n LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO ")

            print("\n       METRÔ ")
            print("Linha 1 - Azul: Aberta")
            print("Linha 2 - Verde: Aberta")
            print("Linha 3 - Vermelha: Em manutenção")
            print("Linha 4 - Amarela: Aberta")
            print("Linha 5 - Lilás: Fechada")
            print("Linha 15 - Prata: Aberta")

            print("\n       TRENS")
            print("Linha 7 - Rubi: Aberta")
            print("Linha 8 - Diamante: Aberta")
            print("Linha 9 - Esmeralda: Em manutenção")
            print("Linha 10 - Turquesa: Aberta")
            print("Linha 11 - Coral: Aberta")
            print("Linha 12 - Safira: Fechada")
            print("Linha 13 - Jade: Aberta\n")

        case "2":
            print("\nLOTAÇÃO DAS LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO")

            print("\n       METRÔ ")
            print("Linha 1 - Azul")
            print("Linha 2 - Verde")
            print("Linha 3 - Vermelha")
            print("Linha 4 - Amarela")
            print("Linha 5 - Lilás")
            print("Linha 15 - Prata")

            print("\n       TRENS")
            print("Linha 7 - Rubi")
            print("Linha 8 - Diamante")
            print("Linha 9 - Esmeralda")
            print("Linha 10 - Turquesa")
            print("Linha 11 - Coral")
            print("Linha 12 - Safira")
            print("Linha 13 - Jade\n")

            linha = input("\nEscolha uma linha: ")

            match linha:
                case "1":
                    print("Linha Azul: Superlotado")
                case "2":
                    print("Linha Verde: Pouco movimentado")
                case "3":
                    print("Linha Vermelha: Moderado")
                case "4":
                    print("Linha Amarela: Lotado")
                case "5":
                    print("Linha Lilás: Lotado")
                case "15":
                    print("Linha Prata: Pouco movimentado")
                case "7":
                    print("Linha Rubi: Lotado")
                case "8":
                    print("Linha Diamante: Superlotado")
                case "9":
                    print("Linha Esmeralda: Superlotado")
                case "10":
                    print("Linha Turquesa: Lotado")
                case "11":
                    print("Linha Coral: Moderado")
                case "12":
                    print("Linha Safira: Pouco movimentado")
                case "13":
                    print("Linha Jade: Moderado")
                case _:
                    print("Linha inválida.")

        case "3":
            print("\nLOTAÇÃO POR VAGÃO DAS LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO")

            print("\n       METRÔ ")
            print("Linha 1 - Azul")
            print("Linha 2 - Verde")
            print("Linha 3 - Vermelha")
            print("Linha 4 - Amarela")
            print("Linha 5 - Lilás")
            print("Linha 15 - Prata")

            print("\n       TRENS")
            print("Linha 7 - Rubi")
            print("Linha 8 - Diamante")
            print("Linha 9 - Esmeralda")
            print("Linha 10 - Turquesa")
            print("Linha 11 - Coral")
            print("Linha 12 - Safira")
            print("Linha 13 - Jade\n")

            vagao = input("\nEscolha um linha: ")

            match vagao:
                case "1":
                    print("\nLinha Azul:")
                    print("Vagão 1: Superlotado")
                    print("Vagão 2: Pouco movimentado")
                    print("Vagão 3: Moderado")
                    print("Vagão 4: Lotado")
                    print("Vagão 5: Lotado")
                    print("Vagão 6: Lotado")

                case "2":
                    print("\nLinha Verde:")
                    print("Vagão 1: Lotado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Pouco movimentado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Lotado")
                    print("Vagão 6: Moderado")

                case "3":
                    print("\nLinha Vermelha:")
                    print("Vagão 1: Superlotado")
                    print("Vagão 2: Lotado")
                    print("Vagão 3: Lotado")
                    print("Vagão 4: Moderado")
                    print("Vagão 5: Superlotado")
                    print("Vagão 6: Lotado")

                case "4":
                    print("\nLinha Amarela:")
                    print("Vagão 1: Pouco movimentado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Lotado")
                    print("Vagão 4: Moderado")
                    print("Vagão 5: Pouco movimentado")
                    print("Vagão 6: Lotado")

                case "5":
                    print("\nLinha Lilás:")
                    print("Vagão 1: Moderado")
                    print("Vagão 2: Lotado")
                    print("Vagão 3: Pouco movimentado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Lotado")
                    print("Vagão 6: Moderado")

                case "15":
                    print("\nLinha Prata:")
                    print("Vagão 1: Lotado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Pouco movimentado")
                    print("Vagão 4: Lotado")
                    print("Vagão 5: Moderado")
                    print("Vagão 6: Lotado")
                    print("Vagão 7: Pouco movimentado")

                case "7":
                    print("\nLinha Rubi:")
                    print("Vagão 1: Lotado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Superlotado")
                    print("Vagão 4: Lotado")
                    print("Vagão 5: Pouco movimentado")
                    print("Vagão 6: Moderado")
                    print("Vagão 7: Lotado")
                    print("Vagão 8: Moderado")

                case "8":
                    print("\nLinha Diamante:")
                    print("Vagão 1: Moderado")
                    print("Vagão 2: Lotado")
                    print("Vagão 3: Pouco movimentado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Moderado")
                    print("Vagão 6: Lotado")
                    print("Vagão 7: Pouco movimentado")
                    print("Vagão 8: Lotado")

                case "9":
                    print("\nLinha Esmeralda:")
                    print("Vagão 1: Pouco movimentado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Lotado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Moderado")
                    print("Vagão 6: Lotado")
                    print("Vagão 7: Moderado")
                    print("Vagão 8: Pouco movimentado")

                case "10":
                    print("\nLinha Turquesa:")
                    print("Vagão 1: Lotado")
                    print("Vagão 2: Superlotado")
                    print("Vagão 3: Moderado")
                    print("Vagão 4: Pouco movimentado")
                    print("Vagão 5: Lotado")
                    print("Vagão 6: Moderado")
                    print("Vagão 7: Lotado")
                    print("Vagão 8: Pouco movimentado")

                case "11":
                    print("\nLinha Coral:")
                    print("Vagão 1: Moderado")
                    print("Vagão 2: Pouco movimentado")
                    print("Vagão 3: Lotado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Moderado")
                    print("Vagão 6: Lotado")
                    print("Vagão 7: Pouco movimentado")
                    print("Vagão 8: Lotado")

                case "12":
                    print("\nLinha Safira:")
                    print("Vagão 1: Superlotado")
                    print("Vagão 2: Lotado")
                    print("Vagão 3: Moderado")
                    print("Vagão 4: Pouco movimentado")
                    print("Vagão 5: Lotado")
                    print("Vagão 6: Moderado")
                    print("Vagão 7: Lotado")
                    print("Vagão 8: Pouco movimentado")

                case "13":
                    print("\nLinha Jade:")
                    print("Vagão 1: Pouco movimentado")
                    print("Vagão 2: Moderado")
                    print("Vagão 3: Lotado")
                    print("Vagão 4: Superlotado")
                    print("Vagão 5: Moderado")
                    print("Vagão 6: Lotado")
                    print("Vagão 7: Pouco movimentado")
                    print("Vagão 8: Moderado")

                case _:
                    print("Linha inválida.")

        case "4":
            print("\nHORÁRIOS DE MENOR E MAIOR MOVIMENTO")

            print("\n       METRÔ")
            print("Linha 1 - Azul")
            print("Linha 2 - Verde")
            print("Linha 3 - Vermelha")
            print("Linha 4 - Amarela")
            print("Linha 5 - Lilás")
            print("Linha 15 - Prata")

            print("\n       TRENS")
            print("Linha 7 - Rubi")
            print("Linha 8 - Diamante")
            print("Linha 9 - Esmeralda")
            print("Linha 10 - Turquesa")
            print("Linha 11 - Coral")
            print("Linha 12 - Safira")
            print("Linha 13 - Jade")

            horario = input("\nEscolha uma linha: ")

            match horario:
                case "1":
                    print("\nLinha Azul:")
                    print("Melhor horário: 14h às 15h")
                    print("Pior horário: 6h às 7h")

                case "2":
                    print("\nLinha Verde:")
                    print("Melhor horário: 13h às 14h")
                    print("Pior horário: 17h às 18h")

                case "3":
                    print("\nLinha Vermelha:")
                    print("Melhor horário: 14h às 15h")
                    print("Pior horário: 7h às 8h")

                case "4":
                    print("\nLinha Amarela:")
                    print("Melhor horário: 11h às 12h")
                    print("Pior horário: 18h às 19h")

                case "5":
                    print("\nLinha Lilás:")
                    print("Melhor horário: 13h às 14h")
                    print("Pior horário: 7h às 8h")

                case "15":
                    print("\nLinha Prata:")
                    print("Melhor horário: 14h às 15h")
                    print("Pior horário: 17h às 18h")

                case "7":
                    print("\nLinha Rubi:")
                    print("Melhor horário: 10h às 11h")
                    print("Pior horário: 6h às 7h")

                case "8":
                    print("\nLinha Diamante:")
                    print("Melhor horário: 13h às 14h")
                    print("Pior horário: 17h às 18h")

                case "9":
                    print("\nLinha Esmeralda:")
                    print("Melhor horário: 14h às 15h")
                    print("Pior horário: 7h às 8h")

                case "10":
                    print("\nLinha Turquesa:")
                    print("Melhor horário: 11h às 12h")
                    print("Pior horário: 17h às 18h")

                case "11":
                    print("\nLinha Coral:")
                    print("Melhor horário: 13h às 14h")
                    print("Pior horário: 6h às 7h")

                case "12":
                    print("\nLinha Safira:")
                    print("Melhor horário: 14h às 15h")
                    print("Pior horário: 17h às 18h")

                case "13":
                    print("\nLinha Jade:")
                    print("Melhor horário: 10h às 11h")
                    print("Pior horário: 7h às 8h")

                case _:
                    print("Linha inválida.")


        case "5":
            print("\nINFORMAÇÕES DE ACESSIBILIDADE")

            print("\n       METRÔ")
            print("Linha 1 - Azul")
            print("Linha 2 - Verde")
            print("Linha 3 - Vermelha")
            print("Linha 4 - Amarela")
            print("Linha 5 - Lilás")
            print("Linha 15 - Prata")

            print("\n       TRENS")
            print("Linha 7 - Rubi")
            print("Linha 8 - Diamante")
            print("Linha 9 - Esmeralda")
            print("Linha 10 - Turquesa")
            print("Linha 11 - Coral")
            print("Linha 12 - Safira")
            print("Linha 13 - Jade")

            acessibilidade = input("\nEscolha uma linha: ")

            match acessibilidade:
                case "1":
                    print("\nLinha Azul:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "2":
                    print("\nLinha Verde:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "3":
                    print("\nLinha Vermelha:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "4":
                    print("\nLinha Amarela:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "5":
                    print("\nLinha Lilás:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "15":
                    print("\nLinha Prata:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "7":
                    print("\nLinha Rubi:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "8":
                    print("\nLinha Diamante:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "9":
                    print("\nLinha Esmeralda:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "10":
                    print("\nLinha Turquesa:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "11":
                    print("\nLinha Coral:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "12":
                    print("\nLinha Safira:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case "13":
                    print("\nLinha Jade:")
                    print("Elevadores: Disponíveis")
                    print("Escadas rolantes: Disponíveis")
                    print("Piso tátil: Disponível")
                    print("Atendimento prioritário: Disponível")

                case _:
                    print("Linha inválida.")

        case "6":
            print("Por favor, forneça os detalhes da ocorrência que deseja registrar.")
            input("Digite a ocorrência: ")
            print("Ocorrência registrada com sucesso.")

        case "7":
            print("Smart Way Encerrado.")
            break

        case _:
            print("Opção inválida.")
