import requests
import os
from utils.env_utils import *
API_URL = read_env('API_URL')
def createCard(cards):
    for c in cards:
        my_card = c.get_card()
        obj = {}
        if 'tags' in my_card:
            obj = {'texto':f'{my_card["texto"]}','tags':my_card["tags"]}
            print(obj)
        else:
            obj = {'texto':f'{my_card["texto"]}'}
            print(obj)
        r = requests.post(f"{API_URL}/cards",json=obj)
        if r.status_code != 201:
            print("Ocorreu um erro ao inserir um card")
            return False