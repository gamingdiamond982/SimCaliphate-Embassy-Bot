from bot import client
import asyncio


	
	

def parseMessage(message, author):
	content = message.split() #splits message at spaces
	if content[0] in Commands: #if the first word of the message is in Commands:
		return Commands[content[0]][len(Commands[content])-1](message, author) #Gets the function for the command
	else:
		return 'Invalid Command'

def parse_reference(content, author):
	return
def reference(command, author):
	#TODO: implement reference command
	return

Commands = {
	'reference' = (
		'reference',
		'Prints a message containing all of the commands',
		parse_reference
  	)
}
