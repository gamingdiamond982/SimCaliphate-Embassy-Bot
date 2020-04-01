import discord
import json

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
    
    
