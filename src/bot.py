import utils
import discord
import json

client = discord.Client()

class BotError(Exception):
  pass


def parseConfig():
  try:
    config = open('config.json', 'r')
    configDict = json.load(config)
    config.close()
    token = configDict["token"]
    prefix = configDict["prefix"]
    return token, prefix
  except KeyError:
    raise BotError("Bad config.json file")
    
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #TODO: add command parsing
  
if __name__ == '__main__':
  token, prefix = parseConfig()
  client.run(token)
  
      

    
  
