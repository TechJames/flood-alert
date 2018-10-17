import requests
from app import ENDPOINT


def get_floods():
    resp = requests.get(ENDPOINT, headers={'cache-control': "no-cache",'accept': "application/json"})
    return resp.json()