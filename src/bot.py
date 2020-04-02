import utils
import commands
import discord
import json

client = discord.Client()


class BotError(Exception):
    pass


def parseConfig():
    """reads the config.json file"""
    try:
        config = open('../config.json', 'r')
        configDict = json.load(config)
        config.close()
        token = configDict["token"]
        prefix = configDict["prefix"]
        colour = configDict["colour"]
        return token, prefix, colour
    except KeyError:
        raise BotError("Bad config.json file")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

"""Main message loop"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):

        # get the message content
        content = message.content

        # get rid of the prefix
        command_content = content[len(prefix):].lstrip()
        response = commands.parseMessage(command_content, message.author)

        chunks = utils.split_into_chunks(response.encode('utf-8'), 1024)
        embed = discord.Embed(color=colour)
        title = command_content.split()[0] if len(
            command_content.split()) > 0 else 'Empty Message'
        for i, chunk in enumerate(chunks):
            title = "(cont'd)" if i > 0 else title
            embed.add_field(name=title, value=chunk.decode(
                'utf-8'), inline=False)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text="Long live the Sultan")
            await message.channel.send(embed=embed)


if __name__ == '__main__':
    token, prefix, colour = parseConfig()
    client.run(token)
