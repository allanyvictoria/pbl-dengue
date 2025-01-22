# Autor: Allany Victória Santos Araújo
# Componente Curricular: MI Algoritmos
# Concluido em: 30/05/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
import datetime as dt
import string

print('=== DENGUE FREE FEIRA ===')


def menu(lista):  # Função para criar menu
    c = 1
    for i in lista:
        print(f"[{c}] - {i}")
        c += 1
    resposta = input('Digite sua opção: ').strip()
    return resposta


def inf():  # informações do sistema
    print("=" * 50)
    print('''
--- DENGUE FREE FEIRA --- 
    
A dengue é uma doença viral transmitida pelo mosquito Aedes aegypti.
A conscientização e o combate ao mosquito são essenciais para controlar
a propagação da doença e proteger a saúde pública. O sistema Dengue Free
Feira disponibiliza informações sobre os casos suspeitos, confirmados ou
negativos dos bairros de Feira de Santana, visando facilitar a obtenção
desses dados.''')
    loop = True
    while loop is True:
        x = input('\nClique ENTER para retornar ao menu inicial')
        if x == "":
            print("=" * 50)
            loop = False
        else:
            print("\033[91m"'\nInválido\n'"\033[0m")


def ler():  # Função conferir a leitura do arquivo
    d = True
    while d is True:
        try:
            arq = input('\nDigite o nome do arquivo: ').strip()
            with open(arq, 'r', encoding='utf-8') as arquivo:
                tamanho = len(arquivo.read())
                if tamanho == 0:
                    print("\033[91m"'\nO arquivo está vazio!\nAdicione um arquivo '
                          'csv que contenha dados'"\033[0m")
                else:
                    d = False
                    print("\033[32m"'\nArquivo lido com sucesso!\n'"\033[0m")
                    print("=" * 50)
        except FileNotFoundError:
            print("\033[91m"'\nArquivo não encontrado!'"\033[0m")
    return arq


def lista_de_dados(arquivo):  # Função para criar lista com os dados do arquivo
    dados_do_arquivo = []
    with open(arquivo, 'r', encoding='utf-8') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for i in leitor:
            dados_do_arquivo.append(i)
    return dados_do_arquivo


def busca_bairro():  # Função para a busca por bairro
    mostrar = []  # Lista apenas com o nome dos bairros
    c = 1
    for linha in dados_arquivo:
        if linha[1] not in mostrar and linha[1] != "Bairros" and linha[1] != "bairros":
            print(f'[{c}] - {linha[1]}')
            mostrar.append(linha[1])
            c += 1
    loop = True
    while loop is True:  # Busca selecionando o bairro e validação da escolha
        try:
            total = len(mostrar)
            escolha = int(input("\nDigite sua opção: "))
            if 1 <= escolha <= total:
                for elemento in dados_arquivo:
                    if mostrar[escolha - 1] in elemento:
                        print("=" * 50)
                        print(f'Data: {elemento[0]} \nBairro: {elemento[1]} '
                              f'\nHabitantes: {elemento[2]} \nCasos suspeitos: {elemento[3]}'
                              f'\nCasos negativos: {elemento[4]} \nCasos confirmados: {elemento[5]}')
                print("=" * 50)
                repetir = True
                while repetir is True:  # Escolha de repetir a busca ou voltar ao menu secundário
                    x = input('[1] - Buscar outro bairro\n[2] - Voltar ao menu'
                              '\nDigite sua opção: ')
                    if x == "2":
                        print("=" * 50)
                        loop = False
                        repetir = False
                    elif x == "1":
                        print("=" * 50)
                        busca_bairro()
                        repetir = False
                        loop = False
                    else:
                        print("\033[91m"'\nInválido\n'"\033[0m")
            else:
                print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")
        except ValueError:
            print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")


def busca_data():  # Função para a busca por data
    mostrar = []  # Lista apenas com as datas
    c = 1
    for linha in dados_arquivo:
        if linha[0] not in mostrar and linha[0] != "data" and linha[0] != "Data":
            print(f'[{c}] - {linha[0]}')
            mostrar.append(linha[0])
            c += 1
    loop = True
    while loop is True:  # Busca selecionando a data e validação da escolha
        try:
            total = len(mostrar)
            escolha = int(input("\nDigite sua opção: "))
            if 1 <= escolha <= total:
                for elemento in dados_arquivo:
                    if mostrar[escolha - 1] in elemento:
                        print("=" * 50)
                        print(f'Data: {elemento[0]} \nBairro: {elemento[1]} '
                              f'\nHabitantes: {elemento[2]} \nCasos suspeitos: {elemento[3]}'
                              f'\nCasos negativos: {elemento[4]} \nCasos confirmados: {elemento[5]}')
                print("=" * 50)
                repetir = True
                while repetir is True:  # Escolha de repetir a busca ou voltar ao menu secundário
                    x = input('[1] - Buscar  por outra data\n[2] - Voltar ao menu'
                              '\nDigite sua opção: ')
                    if x == "2":
                        print("=" * 50)
                        loop = False
                        repetir = False
                    elif x == "1":
                        print("=" * 50)
                        busca_data()
                        repetir = False
                        loop = False
                    else:
                        print("\033[91m"'\nInválido\n'"\033[0m")
            else:
                print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")
        except ValueError:
            print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")


def atualizar(arquivo):  # Função para atualizar dados do arquivo
    repetir = True
    while repetir is True:
        bairros_disponiveis = []
        nomes_bairro = []
        data_string = dados_arquivo[-1][0]
        data = dt.datetime.strptime(data_string, "%d/%m/%Y")
        nova_data = data + dt.timedelta(days=1)
        data_seguinte = dt.datetime.strftime(nova_data, "%d/%m/%Y")
        #  valida se a quantidade de bairros está cadastrada no arquivo:
        for linha in dados_arquivo:
            if linha[1] not in bairros_disponiveis and linha[1] != "Bairros" and linha[1] != "bairros":
                bairros_disponiveis.append(linha[1])
        repeticao = True
        while repeticao is True:
            n = valores_atualizar(f"Deseja atualizar informações do dia {data_seguinte} de quantos bairro: ")
            if n < int(len(bairros_disponiveis)) or n == int(len(bairros_disponiveis)):
                repeticao = False
            else:
                print(f'''\033[91m Existem apenas {int(len(bairros_disponiveis))} bairros disponíveis\033[0m''')
        for i in range(n):
            loop = True
            while loop is True:
                bairro = string.capwords(input("Digite o nome do bairro: "))  # Corrige letras minúsculas
                if bairro == 'Pedra De Descanso':
                    bairro = 'Pedra de Descanso'
                for elemento in dados_arquivo:  # Analisa se o bairro existe no arquivo
                    if bairro in elemento:
                        loop = False
                if loop:
                    print("\033[91m"'\nInválido\nVerifique se a ortografia está correta\n'"\033[0m")
                if bairro in nomes_bairro:  # Analisa se o bairro já foi atualizado
                    loop = True
                    print("\033[91m"'DADOS JÁ EXISTENTES'"\033[0m")
            nomes_bairro.append(bairro)
            loop2 = True
            while loop2 is True:
                habitantes = input('[1] - Alterar número de habitantes\n[2] - Manter número de habitantes'
                                   '\nDigite sua opção: ')
                if habitantes == "1":
                    habi = valores_atualizar("Digite a quantidade de habitantes: ")
                    habi = str(habi)
                    loop2 = False
                elif habitantes == "2":
                    habi = ultima_data(bairro)[2]
                    loop2 = False
                else:
                    print("\033[91m"'\nInválido\n'"\033[0m")
            loop3 = True
            while loop3 is True:  # Analisa se o novos casos estão de acordo com os ultimos suspeitos informados
                negativos = valores_atualizar("Digite a quantidade de NOVOS casos negativos: ")
                positivos = valores_atualizar("Digite a quantidade de NOVOS casos positivos: ")
                soma = negativos + positivos
                if soma <= int(ultima_data(bairro)[3]):
                    loop3 = False
                else:
                    print("\033[91m"'Dados não correspondem com a útilma '
                          'quantidade de casos suspeitos informada ({} casos).'
                          '\nConfira se os dados estão corretos'"\033"
                          "[0m".format(ultima_data(bairro)[3]))
            negativos += int(ultima_data(bairro)[4])
            negativos = str(negativos)
            positivos += int(ultima_data(bairro)[5])
            positivos = str(positivos)
            supeitos = valores_atualizar("Digite a quantidade de NOVOS casos suspeitos(se houver): ")
            supeitos += (int(ultima_data(bairro)[3]) - soma)
            supeitos = str(supeitos)
            atual = [data_seguinte, bairro, habi, supeitos, negativos, positivos]
            with open(arquivo, 'a', newline='', encoding='utf-8') as file:
                nv = csv.writer(file)
                nv.writerow(atual)
                file.close()
            print("\033[32m"'\nDados atualizados com sucessso!\n'"\033[0m")
        m = True
        while m is True:
            x = input('Clique ENTER para retornar ao menu')
            if x == "":
                print("=" * 50)
                m = False
                repetir = False
            else:
                print("\033[91m"'\nInválido\n'"\033[0m")


def valores_atualizar(pergunta):  # Função para validar entradas de números na atualização
    loop = True
    while loop is True:
        try:
            valor = int(input(pergunta))
            if valor >= 0:
                loop = False
                return valor
            else:
                print("\033[91m"'\nInválido\n'"\033[0m")
        except ValueError:
            print("\033[91m"'\nInválido\n'"\033[0m")


def ultima_data(bairro):  # Função para obter apenas os dados da última data de determinado bairro
    datas = []
    for elemento in dados_arquivo:
        if bairro in elemento:
            datas.append(elemento)
    ultima_dt = datas[-1]
    return ultima_dt


def intervalo():  # Função para analisar dados em um intervalo de datas
    mostrar = []
    c = 1
    for linha in dados_arquivo:
        if linha[0] not in mostrar and linha[0] != "data" and linha[0] != "Data":
            print(f'[{c}] - {linha[0]}')
            mostrar.append(linha[0])
            c += 1
    datas1 = []
    datas2 = []
    soma_neg = 0
    soma_pos = 0
    soma_neg2 = 0
    soma_pos2 = 0
    loop = True
    while loop is True:
        try:
            total = len(mostrar)
            data1 = int(input("\nDigite a primeira data: "))
            data2 = int(input("\nDigite a segunda data: "))
            if 1 <= data1 <= total and 1 <= data2 <= total:
                for elemento in dados_arquivo:  # Adiciona os dados das datas selecionadas em listas
                    if mostrar[data1 - 1] in elemento:
                        datas1.append(elemento)
                    if mostrar[data2 - 1] in elemento:
                        datas2.append(elemento)
                for i in datas1:
                    soma_neg += int(i[4])
                    soma_pos += int(i[5])
                for i in datas2:
                    soma_neg2 += int(i[4])
                    soma_pos2 += int(i[5])
                data_string1 = datas1[0][0]
                primeira_data = dt.datetime.strptime(data_string1, "%d/%m/%Y")
                data_string2 = datas2[0][0]
                segunda_data = dt.datetime.strptime(data_string2, "%d/%m/%Y")
                print("=" * 50)
                # Analisa qual a maior data para tirar a diferença do maior para o menor
                if primeira_data > segunda_data:
                    menor_data = datas2[0][0]
                    maior_data = datas1[0][0]
                    diferenca_neg = soma_neg - soma_neg2
                    diferenca_pos = soma_pos - soma_pos2
                else:
                    menor_data = datas1[0][0]
                    maior_data = datas2[0][0]
                    diferenca_neg = soma_neg2 - soma_neg
                    diferenca_pos = soma_pos2 - soma_pos
                print(f'Dia {datas1[0][0]}: {soma_pos} casos positivos e {soma_neg} casos negativos\n'
                      f'Dia {datas2[0][0]}: {soma_pos2} casos positivos e {soma_neg2} casos negativos\n'
                      f'\nEntre as datas {menor_data} e {maior_data}:\n'
                      f'-Existiu um aumento de {diferenca_pos} casos positivos\n'
                      f'*Aumento de {(diferenca_pos / soma_pos) * 100:.2f}%\n'
                      f'-Existiu um aumento de {diferenca_neg} casos negativos\n'
                      f'*Aumento de {(diferenca_neg / soma_neg) * 100:.2f}%')
                m = True
                while m is True:
                    x = input('\nClique ENTER para retornar ao menu')
                    if x == "":
                        print("=" * 50)
                        m = False
                        loop = False
                    else:
                        print("\033[91m"'\nInválido\n'"\033[0m")
            else:
                print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")
        except ValueError:
            print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")


def porcentagem_bairro():  # Função para calcular a porcentagem por bairro
    mostrar = []  # Lista apenas com nomes dos bairros disponíveis
    c = 1
    for linha in dados_arquivo:
        if linha[1] not in mostrar and linha[1] != "Bairros" and linha[1] != "bairros":
            print(f'[{c}] - {linha[1]}')
            mostrar.append(linha[1])
            c += 1
    loop = True
    while loop is True:
        try:
            total = len(mostrar)
            escolha = int(input("\nDigite sua opção: "))
            if 1 <= escolha <= total:
                suspeitos = (int(ultima_data(mostrar[escolha - 1])[3]) * 100)/int(
                    ultima_data(mostrar[escolha - 1])[2])
                positivos = (int(ultima_data(mostrar[escolha - 1])[5]) * 100) / int(
                    ultima_data(mostrar[escolha - 1])[2])
                print(f'\n--- {mostrar[escolha - 1]} ---\nCasos suspeitos: {suspeitos:.2f}%\n'
                      f'Casos positivos: {positivos:.2f}%\n')
                m = True
                while m is True:
                    x = input('Clique ENTER para retornar ao menu')
                    if x == "":
                        print("=" * 50)
                        m = False
                        loop = False
                    else:
                        print("\033[91m"'\nInválido\n'"\033[0m")
            else:
                print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")
        except ValueError:
            print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")


def porcentagem_geral():  # Função para calcular a porcentagem geral
    bairros = []  # # Lista apenas com nomes dos bairros
    for linha in dados_arquivo:
        if linha[1] not in bairros and linha[1] != "Bairros" and linha[1] != "bairros":
            bairros.append(linha[1])
    casos_notificados = 0
    suspeitos = 0
    positivos = 0
    negativos = 0
    for elemento in bairros:
        casos_notificados += int(ultima_data(elemento)[3]) + int(ultima_data(
            elemento)[4]) + int(ultima_data(elemento)[5])
        suspeitos += int(ultima_data(elemento)[3])
        positivos += int(ultima_data(elemento)[5])
        negativos += int(ultima_data(elemento)[4])
    print(f'\n--- {casos_notificados} Casos notificados ---\n'
          f'Casos suspeitos: {(suspeitos * 100)/casos_notificados:.2f}%\n'
          f'Casos positivos: {(positivos * 100)/casos_notificados:.2f}%\n'
          f'Casos negativos: {(negativos * 100)/casos_notificados:.2f}% \n')
    m = True
    while m is True:
        x = input('Clique ENTER para retornar ao menu')
        if x == "":
            print("=" * 50)
            m = False
        else:
            print("\033[91m"'\nInválido\n'"\033[0m")


def todos_dados():  # Função para mostrar todos os dados (atualizados) de cada bairro e porcentagens
    bairros = []  # Lista apenas com nomes dos bairros
    for linha in dados_arquivo:
        if linha[1] not in bairros and linha[1] != "Bairros" and linha[1] != "bairros":
            bairros.append(linha[1])
    casos_notificados = 0
    suspeitos = 0
    positivos = 0
    negativos = 0
    for elemento in bairros:  # Calculo da porcentagem geral
        casos_notificados += int(ultima_data(elemento)[3]) + int(ultima_data(
            elemento)[4]) + int(ultima_data(elemento)[5])
        suspeitos += int(ultima_data(elemento)[3])
        positivos += int(ultima_data(elemento)[5])
        negativos += int(ultima_data(elemento)[4])
    print(f'\n--- {casos_notificados} Casos notificados ---\n'
          f'Casos suspeitos: {(suspeitos * 100) / casos_notificados:.2f}%\n'
          f'Casos positivos: {(positivos * 100) / casos_notificados:.2f}%\n'
          f'Casos negativos: {(negativos * 100) / casos_notificados:.2f}% \n')
    for elemento in bairros:  # imprime todos os dados e porcentagem de cada bairro
        suspeitos_bairro = (int(ultima_data(elemento)[3]) * 100) / int(ultima_data(elemento)[2])
        positivos_bairro = (int(ultima_data(elemento)[5]) * 100) / int(ultima_data(elemento)[2])
        negativos_bairro = (int(ultima_data(elemento)[4]) * 100) / int(ultima_data(elemento)[2])
        print("=" * 50)
        print(f'\n--- {ultima_data(elemento)[1]} ---\nData: {ultima_data(elemento)[0]}'
              f'\nHabitantes: {ultima_data(elemento)[2]} \nCasos suspeitos: {ultima_data(elemento)[3]} '
              f'({suspeitos_bairro:.2f}%)'
              f'\nCasos negativos: {ultima_data(elemento)[4]} ({negativos_bairro:.2f}%)'
              f'\nCasos confirmados: {ultima_data(elemento)[5]}'
              f' ({positivos_bairro:.2f}%)')
    m = True
    while m is True:
        x = input('\nClique ENTER para retornar ao menu')
        if x == "":
            print("=" * 50)
            m = False
        else:
            print("\033[91m"'\nInválido\n'"\033[0m")


# programa principal:
fim = False
while fim is False:
    inicio = menu(['Informações iniciais', 'Ler arquivo', 'Finalizar'])  # Menu inicial
    match inicio:
        case '1':
            inf()
        case '2':
            print("=" * 50)
            n_arq = ler()
            dados_arquivo = lista_de_dados(n_arq)
            f = True
            while f is True:
                opcoes2 = menu(['Buscar por data', 'Buscar por bairros',
                                'Intervalo entre datas', 'Atualizar dados', 'Porcentagem por bairro',
                                'Porcentagem total', 'Visualizar todos os dados (atualizados)',
                                'Voltar ao menu principal'])  # Menu secundário
                match opcoes2:
                    case '1':
                        print("=" * 50)
                        busca_data()
                    case '2':
                        print("=" * 50)
                        busca_bairro()
                    case '3':
                        print("=" * 50)
                        intervalo()
                    case '4':
                        print("=" * 50)
                        atualizar(n_arq)
                    case '5':
                        print("=" * 50)
                        porcentagem_bairro()
                    case '6':
                        print("=" * 50)
                        porcentagem_geral()
                    case '7':
                        print("=" * 50)
                        todos_dados()
                    case '8':
                        f = False
                        print("=" * 50)
                    case _:
                        print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")
        case '3':
            print("\33[35m"'\n>>>Sistema finalizado<<<'"\033[0m")
            fim = True
        case _:
            print("\033[91m"'\n***DIGITE UMA OPÇÃO VÁLIDA***\n'"\033[0m")