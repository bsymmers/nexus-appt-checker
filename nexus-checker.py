import requests
import pandas as pd
import os
from dotenv import load_dotenv
import discord
import asyncio
import logging
import random
import datetime
from zoneinfo import ZoneInfo
import sys

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
        # if date.weekday() == 5 or date.weekday() == 6:
        ret_val.append('Nexus appointment available for ' + str(date.day_name()) + ", " + str(date.date()) + " at "
                            + str(date.time()))
    return ret_val
def getInfo():
    url = 'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId=5020&minimum=1'
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL = os.getenv('DISCORD_CHANNEL')
    client = discord.Client(intents=discord.Intents.default())

    # Create and configure logger
    logging.basicConfig(filename="nexus-logs.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    
    # Creating an object
    logger = logging.getLogger()
    
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    
    @client.event
    async def on_ready():
        while True:
            # response = requests.get(url).json()
            response = requests.get(url)
            try:
                response_json = response.json()
                decoded_response = decodeResponse(response=response_json)
            except:
                print(response.status_code)
                logger.debug("Issue decoding response from API")
                logger.debug(response.headers)
                logger.debug(response.text)
                channel = client.get_channel(int(CHANNEL))
                await sendMessage(to_send=["BRANDON FIX BOT"], channel=channel)
            if response.status_code == 200 and decoded_response != []:
                logger.debug("Sending " + str(response_json) )
                channel = client.get_channel(int(CHANNEL))
                await sendMessage(to_send=decoded_response, channel=channel)
                await asyncio.sleep(20)
            rand = random.randint(3, 5)
            print(f'Sleeping for {rand} seconds')
            await asyncio.sleep(rand)

            current_time = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))
            if current_time.hour >= 0 and current_time.hour < 7:
                print('Going to sleep')
                await asyncio.sleep(18000)

        
    client.connect()
    client.run(TOKEN)
   

getInfo()