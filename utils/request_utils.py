import requests
import os
from utils.env_utils import *
API_URL = readEnv('API_URL')
def createCard(cards):
    for c in cards:
        myCard = c.getCard()
        print({'texto':f'{myCard["texto"]}','tags':myCard["tags"]})
        r = requests.post(f"{API_URL}/v1/cards",json={'texto':f'{myCard["texto"]}','tags':myCard["tags"]})
        if r.status_code != 201:
            print("Ocorreu um erro ao inserir um card")
            return False