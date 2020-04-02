from bot import client
import asyncio


# def parseMessage(message, author):
#     content = message.split()  # splits message at spaces
#     # if the first word of the message is in Commands:
#     if content[0] in Commands:
#         # Gets the function for the command
#         return Commands[content[0]][len(Commands[content])-1](message, author)
#     else:
#         return 'Invalid Command'


def parseMessage(content, author):
    for cmd in Commands:
        command_name = Commands[cmd][0]
        command_desc = Commands[cmd][1]
        return command_name + " " + command_desc


Commands = {
    'reference': (
        'reference',
        'Prints a message containing all of the commands',
        parseMessage
    )
}
