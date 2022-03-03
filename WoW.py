from asyncio.windows_events import NULL
import os
#Community API Library for Blizzard
from blizzardapi import BlizzardApi
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('BLIZZ_ID')
client_secret = os.getenv('BLIZZ_SECRET')
api_client = BlizzardApi(client_id, client_secret)


#Requests realm status data from WoW API
#Returns a str notifying realm's status
def ServerStatus():
    connected_realms = api_client.wow.game_data.get_connected_realm("us", "en_US",11)
    realms = connected_realms['realms']
    realms = realms[0]
    realm_name = realms['name']
    if (connected_realms['status']['type'] == "UP"):
        response = f'{realm_name} is up!'
    elif (connected_realms['status']['type'] != "UP"):
        response = f'{realm_name} is down!'
    return response