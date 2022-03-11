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

#Requests realm status data from WoW API
#Inputs a str of the realm's name
#Returns the realm id or -1 if not found
def getRealmID(user_input):
    user_input = user_input.replace(' ', '-').lower()
    realm_list = api_client.wow.game_data.get_realm("us","en_US",user_input)
    
    if ('Not Found' in realm_list.values()):
        response= "Realm could not be found, try again."
        return -1
    else:
        realm_id = realm_list['id']
        return realm_id

def TrackRealm(realm_id):
    print('Tracking!')
    if realm_id == -1:
        response = "Realm not set!"
        return response   
    else:
        connected_realms = api_client.wow.game_data.get_connected_realm("us", "en_US",realm_id)
        if ('Not Found' in connected_realms.values()):
            response = "Realm status could not be found."
            return response
        else:
            #Collects list of selected realm data
            realms = connected_realms['realms']
            #Extracts realm's data from dictionary
            realms = realms[0]
            #Extracts name of realm from dictionary
            realm_name = realms['name']
            prev = connected_realms['status']['type']
        while(True):
            print('tracking in progress')
            cur = connected_realms['status']['type']
            if(cur == "UP" and prev != "UP"):
                response = f'{realm_name} is back up!'
                break
            elif(cur != "UP" and prev == "UP"):
                response = f'{realm_name} has gone down!'
                break
        return response

    


        

def RealmStatus(realm_id):
    if realm_id == -1:
        response = "Realm not set!"
        return response
    
    connected_realms = api_client.wow.game_data.get_connected_realm("us", "en_US",realm_id)
    if ('Not Found' in connected_realms.values()):
        response = "Realm status could not be found."
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

