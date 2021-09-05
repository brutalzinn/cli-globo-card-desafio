import csv
from models.models_card import Card
import sys

from utils.request_utils import *
cardList = []
args = sys.argv

if len(args) == 3 and '-csv' in args[1]:
    csvName = args[2]
elif len(args) == 2 and '-csv' in args[1]:
    csvName = None
    print("Nome de arquivo csv não forneceido. Utilizando cards.csv como padrão")
else:
    csvName = None
    print("Nenhum argumento fornecido. Utilizando cards.csv como padrão")
    print("Comando não reconhecido.")

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