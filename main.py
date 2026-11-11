import os
os.system("cls")

# Loop principal: o menu é exibido até o usuário escolher sair
while True:
    print(f"""\nBem-vindo ao Smart Way - Sistema de Transporte Metropolitano de São Paulo
    1- Consultar linhas do metrô
    2- Consultar lotação das linhas
    3- Consultar lotação por vagão
    4- Consultar horários de menor movimento
    5- Consultar informações de acessibilidade
    6- Registrar uma ocorrência
    7- Sair do sistema
    """)

    # Lê a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # Executa a ação correspondente à opção escolhida
    match opcao:
        # Opção 1: mostra o status de funcionamento de cada linha
        case "1":
            print(f"""\n LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO

                METRÔ 
            Linha 1 - Azul: Aberta
            Linha 2 - Verde: Aberta
            Linha 3 - Vermelha: Em manutenção
            Linha 4 - Amarela: Aberta
            Linha 5 - Lilás: Fechada
            Linha 15 - Prata: Aberta
                TRENS
            Linha 7 - Rubi: Aberta
            Linha 8 - Diamante: Aberta
            Linha 9 - Esmeralda: Em manutenção
            Linha 10 - Turquesa: Aberta
            Linha 11 - Coral: Aberta
            Linha 12 - Safira: Fechada
            Linha 13 - Jade: Aberta\n
            """)
        # Opção 2: mostra a lotação geral da linha escolhida
        case "2":
            print(f"""\nLOTAÇÃO DAS LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO

            \n    METRÔ 
            Linha 1 - Azul")
            Linha 2 - Verde")
            Linha 3 - Vermelha")
            Linha 4 - Amarela")
            Linha 5 - Lilás")
            Linha 15 - Prata")

            \n   TRENS
            Linha 7 - Rubi
            Linha 8 - Diamante
            Linha 9 - Esmeralda
            Linha 10 - Turquesa
            Linha 11 - Coral
            Linha 12 - Safira
            Linha 13 - Jade\n
            """)

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
        # Opção 3: mostra a lotação de cada vagão da linha escolhida
        case "3":
            print(f"""\nLOTAÇÃO POR VAGÃO DAS LINHAS DO TRANSPORTE METROPOLITANO DE SÃO PAULO

            \n  METRÔ 
            Linha 1 - Azul
            Linha 2 - Verde
            Linha 3 - Vermelha
            Linha 4 - Amarela
            Linha 5 - Lilás
            Linha 15 - Prata

            \n TRENS
            Linha 7 - Rubi
            Linha 8 - Diamante
            Linha 9 - Esmeralda
            Linha 10 - Turquesa
            Linha 11 - Coral
            Linha 12 - Safira
            Linha 13 - Jade\n
            """)

            vagao = input("\nEscolha um linha: ")

            match vagao:
                case "1":
                    print(f"""\nLinha Azul:
                    Vagão 1: Superlotado
                    Vagão 2: Pouco movimentado
                    Vagão 3: Moderado
                    Vagão 4: Lotado
                    Vagão 5: Lotado
                    Vagão 6: Lotado
                    """)

                case "2":
                    (f"""\nLinha Verde:
                    Vagão 1: Lotado
                    Vagão 2: Moderado
                    Vagão 3: Pouco movimentado
                    Vagão 4: Superlotado
                    Vagão 5: Lotado
                    Vagão 6: Moderado
                    """)

                case "3":
                    print(f"""\nLinha Vermelha:
                    Vagão 1: Superlotado
                    Vagão 2: Lotado
                    Vagão 3: Lotado
                    Vagão 4: Moderado
                    Vagão 5: Superlotado
                    Vagão 6: Lotado
                    """)

                case "4":
                    print(f"""\nLinha Amarela:
                    Vagão 1: Pouco movimentado
                    Vagão 2: Moderado
                    Vagão 3: Lotado
                    Vagão 4: Moderado
                    Vagão 5: Pouco movimentado
                    Vagão 6: Lotado
                    """)

                case "5":
                    print(f"""\nLinha Lilás:
                    Vagão 1: Moderado")
                    Vagão 2: Lotado")
                    Vagão 3: Pouco movimentado
                    Vagão 4: Superlotado
                    Vagão 5: Lotado
                    Vagão 6: Moderado
                    """)

                case "15":
                    print(f"""\nLinha Prata:
                    Vagão 1: Lotado
                    Vagão 2: Moderado
                    Vagão 3: Pouco movimentado
                    Vagão 4: Lotado
                    Vagão 5: Moderado
                    Vagão 6: Lotado
                    Vagão 7: Pouco movimentado
                    """)

                case "7":
                    print(f"""\nLinha Rubi:
                    Vagão 1: Lotado
                    Vagão 2: Moderado
                    Vagão 3: Superlotado
                    Vagão 4: Lotado
                    Vagão 5: Pouco movimentado
                    Vagão 6: Moderado
                    Vagão 7: Lotado
                    Vagão 8: Moderado
                    """)

                case "8":
                    print(f"""\nLinha Diamante:
                    Vagão 1: Moderado
                    Vagão 2: Lotado
                    Vagão 3: Pouco movimentado
                    Vagão 4: Superlotado
                    Vagão 5: Moderado
                    Vagão 6: Lotado
                    Vagão 7: Pouco movimentado
                    Vagão 8: Lotado
                    """)
                    
                case "9":
                    print(f"""\nLinha Esmeralda:
                    Vagão 1: Pouco movimentado
                    Vagão 2: Moderado
                    Vagão 3: Lotado
                    Vagão 4: Superlotado
                    Vagão 5: Moderado
                    Vagão 6: Lotado
                    Vagão 7: Moderado
                    Vagão 8: Pouco movimentado
                    """)

                case "10":
                    print(f"""\nLinha Turquesa:
                    Vagão 1: Lotado
                    Vagão 2: Superlotado
                    Vagão 3: Moderado
                    Vagão 4: Pouco movimentado
                    Vagão 5: Lotado
                    Vagão 6: Moderado
                    Vagão 7: Lotado
                    Vagão 8: Pouco movimentado
                    """)

                case "11":
                    print(f"""\nLinha Coral:
                    Vagão 1: Moderado
                    Vagão 2: Pouco movimentado
                    Vagão 3: Lotado
                    Vagão 4: Superlotado
                    Vagão 5: Moderado
                    Vagão 6: Lotado
                    Vagão 7: Pouco movimentado
                    Vagão 8: Lotado
                    """)

                case "12":
                    print(f"""\nLinha Safira:
                    Vagão 1: Superlotado
                    Vagão 2: Lotado
                    Vagão 3: Moderado
                    Vagão 4: Pouco movimentado
                    Vagão 5: Lotado
                    Vagão 6: Moderado
                    Vagão 7: Lotado
                    Vagão 8: Pouco movimentado
                    """)

                case "13":
                    print(f"""\nLinha Jade:
                    Vagão 1: Pouco movimentado
                    Vagão 2: Moderado
                    Vagão 3: Lotado
                    Vagão 4: Superlotado
                    Vagão 5: Moderado
                    Vagão 6: Lotado
                    Vagão 7: Pouco movimentado
                    Vagão 8: Moderado
                    """)

                case _:
                    print("Linha inválida.")
        # Opção 4: mostra o melhor e o pior horário para viajar
        case "4":
            print("\nHORÁRIOS DE MENOR E MAIOR MOVIMENTO")

            print(f"""\n METRÔ
            Linha 1 - Azul
            Linha 2 - Verde
            Linha 3 - Vermelha
            Linha 4 - Amarela
            Linha 5 - Lilás
            Linha 15 - Prata
            """)

            print(f"""\n TRENS
            Linha 7 - Rubi
            Linha 8 - Diamante
            Linha 9 - Esmeralda
            Linha 10 - Turquesa
            Linha 11 - Coral
            Linha 12 - Safira
            Linha 13 - Jade
            """)

            horario = input("\nEscolha uma linha: ")

            match horario:
                case "1":
                    print(f"""\nLinha Azul:
                    Melhor horário: 14h às 15h
                    Pior horário: 6h às 7h
                    """)

                case "2":
                    print(f"""\nLinha Verde:
                    Melhor horário: 13h às 14h
                    Pior horário: 17h às 18h
                    """)

                case "3":
                    print(f"""\nLinha Vermelha:
                    Melhor horário: 14h às 15h
                    Pior horário: 7h às 8h
                    """)

                case "4":
                    print(f"""\nLinha Amarela:
                    Melhor horário: 11h às 12h
                    Pior horário: 18h às 19h
                    """)

                case "5":
                    print(f"""\nLinha Lilás:
                    Melhor horário: 13h às 14h
                    Pior horário: 7h às 8h
                    """)
                    
                case "15":
                    print(f"""\nLinha Prata:
                    Melhor horário: 14h às 15h
                    Pior horário: 17h às 18h
                    """)

                case "7":
                    print(f"""\nLinha Rubi:
                    Melhor horário: 10h às 11h
                    Pior horário: 6h às 7h
                    """)

                case "8":
                    print(f"""\nLinha Diamante:
                    Melhor horário: 13h às 14h
                    Pior horário: 17h às 18h
                    """)

                case "9":
                    print(f"""\nLinha Esmeralda:
                    Melhor horário: 14h às 15h
                    Pior horário: 7h às 8h
                    """)

                case "10":
                    print(f"""\nLinha Turquesa:
                    Melhor horário: 11h às 12h
                    Pior horário: 17h às 18h
                    """)

                case "11":
                    print(f"""\nLinha Coral:
                    Melhor horário: 13h às 14h
                    Pior horário: 6h às 7h
                    """)

                case "12":
                    print(f"""\nLinha Safira:
                    Melhor horário: 14h às 15h
                    Pior horário: 17h às 18h
                    """)

                case "13":
                    print(f"""\nLinha Jade:
                    Melhor horário: 10h às 11h
                    Pior horário: 7h às 8h
                    """)

                case _:
                    print("Linha inválida.")

        # Opção 5: mostra os recursos de acessibilidade da linha
        case "5":
            print(f"\nINFORMAÇÕES DE ACESSIBILIDADE")

            print(f"""\n METRÔ
            Linha 1 - Azul
            Linha 2 - Verde
            Linha 3 - Vermelha
            Linha 4 - Amarela
            Linha 5 - Lilás
            Linha 15 - Prata
            """)

            print(f"""\n TRENS
            Linha 7 - Rubi
            Linha 8 - Diamante
            Linha 9 - Esmeralda
            Linha 10 - Turquesa
            Linha 11 - Coral
            Linha 12 - Safira
            Linha 13 - Jade
            """)

            acessibilidade = input("\nEscolha uma linha: ")

            match acessibilidade:
                case "1":
                    print(f"""\nLinha Azul:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "2":
                    print(f"""\nLinha Verde:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "3":
                    print(f"""\nLinha Vermelha:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponíve
                    """)

                case "4":
                    print(f"""\nLinha Amarela:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "5":
                    print(f"""\nLinha Lilás:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "15":
                    print(f"""\nLinha Prata:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "7":
                    print(f"""\nLinha Rubi:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "8":
                    print(f"""\nLinha Diamante:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "9":
                    print(f"""\nLinha Esmeralda:")
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "10":
                    print(f"""\nLinha Turquesa:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "11":
                    print(f"""\nLinha Coral:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "12":
                    print(f"""\nLinha Safira:
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case "13":
                    print(f"""\nLinha Jade:
                    Elevadores: Disponíveis
                    Escadas rolantes: Disponíveis
                    Piso tátil: Disponível
                    Atendimento prioritário: Disponível
                    """)

                case _:
                    print("Linha inválida.")
        # Opção 6: registra uma ocorrência informada pelo usuário
        case "6":
            print("Por favor, forneça os detalhes da ocorrência que deseja registrar.")
            input("Digite a ocorrência: ")
            print("Ocorrência registrada com sucesso.")
        # Opção 7: encerra o programa saindo do loop
        case "7":
            print("Smart Way Encerrado.")
            break

        case _:
            print("Opção inválida.")