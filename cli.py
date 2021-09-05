import csv
from models.models_card import Card
from utils.request_utils import *
cardList = []
print("O arquivo cards.csv será utilizado como padrão \ncaso nenhum nome de arquivo seja informado")

csvName = input("Nome do arquivo csv: ")
if not csvName:
    csvName = "cards"
try:
    with open(f'{csvName}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=';')
        for row in spamreader:
            newCard = Card(row[0], row[1])
            cardList.append(newCard)
except:
    print("Erro: Arquivo não encontrado.")

createCard(cardList)