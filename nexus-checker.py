import requests
import pandas as pd
import os
from dotenv import load_dotenv
import discord
import asyncio

async def sendMessage(to_send, channel):
    for element in to_send:
        await channel.send(element)
    return

def decodeResponse(response) -> list:
    '''
    Decodes response and only sends push notification if appointment is on a weekend.
    '''
    ret_val = []
    for element in response:
        date = pd.to_datetime(element['startTimestamp'])
        # if not date.weekday():
        ret_val.append('Nexus appointment available for ' + str(date.day_name()) + ", " + str(date.date()))
    return ret_val
def getInfo():
    url = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId=5020&minimum=1'
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL = os.getenv('DISCORD_CHANNEL')
    client = discord.Client(intents=discord.Intents.default())
    
    @client.event
    async def on_ready():
        while True:
            response = requests.get(url).json()
            print(response)
            decoded_response = decodeResponse(response=response)
            if decoded_response != []:
                channel = client.get_channel(int(CHANNEL))
                await sendMessage(to_send=decoded_response, channel=channel)
                await asyncio.sleep(100)
            await asyncio.sleep(20)
       
        print("Ready!")
        
    client.connect()
    client.run(TOKEN)
   

getInfo()