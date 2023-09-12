import openpyxl

# Cria a nossa planilha
book = openpyxl.Workbook()

# Ativa o uso da nossa planilha
planilha = book.active

# ALterandoo nome da planilha
planilha.title = "Computadores"

data = [
    # Nome das colunas
    ['Eletronico', 'Memoria ram', 'Preco'],
    # Dados correspondentes as colunas
    ['Computador 1', '8gb Ram', 'R$2.500'],
    ['Computador 2', '16gb Ram', 'R$5.500'],
    ['Computador 4', '32gb Ram', 'R$8.500'],
    ['Computador 5', '8gb Ram', 'R$8.500'],
    ['Computador 6', '16gb Ram', 'R$8.500'],
    ['Computador 7', '32gb Ram', 'R$2.500'],
    ['Computador 8', '8gb Ram', 'R$3.500'],
    ['Computador 9', '16gb Ram', 'R$4.500'],
    ['Computador 10', '32gb Ram', 'R$6.500'],
    ['Computador 11', '16gb Ram', 'R$7.500'],
    ['Computador 12', '8gb Ram', 'R$5.500'],
]

# faz a inclusão dos valores na planilha
for valor in data:
    planilha.append(valor)

book.save("planilha_criada/Controle de Computadores.xlsx")
