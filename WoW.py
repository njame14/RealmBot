from asyncio.windows_events import NULL
import os
from matplotlib.pyplot import connect
import requests
from dotenv import load_dotenv
#Community API Library for Blizzard
from blizzardapi import BlizzardApi


load_dotenv()
client_id = os.getenv('BLIZZ_ID')
client_secret = os.getenv('BLIZZ_SECRET')
api_client = BlizzardApi(client_id, client_secret)

realm_id = 1
realm_set = False

#Requests realm status data from WoW API
#Returns a str notifying realm's status

def SetRealm(user_input):
    global realm_id, realm_set

    user_input = user_input.replace(' ', '-').lower()
    realm_list = api_client.wow.game_data.get_realm("us","en_US",user_input)

    if ('Not Found' in realm_list.values()):
        response = "Realm does not exist, try again."
        return response
    else:
        realm_id = realm_list['id']
        realm_set = True
        response = "Realm is set!"
        print(realm_id)
        return response
    



def RealmStatus():
    if realm_set == False:
        response = "Realm not set!"
        return response
    
    connected_realms = api_client.wow.game_data.get_connected_realm("us", "en_US",realm_id)
    if ('Not Found' in connected_realms.values()):
        response = "Realm does not exist"
        print(realm_id)
        print(connected_realms)
        return response
    else:
        #Collects list of selected realm data
        realms = connected_realms['realms']
        #Extracts realm's data from dictionary
        realms = realms[0]
        #Extracts name of realm from dictionary
        realm_name = realms['name']

        #Prints status of realm
        if (connected_realms['status']['type'] == "UP"):
            response = f'{realm_name} is up!'
        elif (connected_realms['status']['type'] != "UP"):
            response = f'{realm_name} is down!'
        return response

