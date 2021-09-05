import csv
from models.models_card import Card
from utils.request_utils import *
cardList = []
print("O arquivo cards.csv será utilizado como padrão \ncaso nenhum nome de arquivo seja informado")
print("Escreva o nome do arquivo csv sem a extensão .csv")
csvName = input("Nome do arquivo csv: ")
if not csvName:
    csvName = "cards"
try:
    with open(f'{csvName}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=';')
        for row in spamreader:
            if len(row) > 1:
                newCard = Card(row[0], row[1])
            else:
                newCard = Card(row[0])
            cardList.append(newCard)
except(Exception):
    print("Erro: Arquivo não encontrado.")

createCard(cardList)