from discord.ext.commands import Bot
import random

BOT_PREFIX = "$$"
TOKEN = 'NTA2ODQzMDUzMzE1ODUwMjUw.DroCGA.juXZJ8dCrk2xMNWHZyENZ0dJyhU'

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description='Answers a yes/no question',
                brief='brucc succs',
                aliases= ['8','y/n'],
                pass_context = True)
async def eight_ball(context):
    possible_responses = [
        'Possibly',
        'Yes',
        'No',
        'Too hard to tell',
        'Ask again later',
        'Ask Brucc'
    ]
    await client.say(random.choice(possible_responses) + ', ' + context.message.author.mention)
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + ' squared is ' + str(squared_value))
client.run('NTA2ODQzMDUzMzE1ODUwMjUw.DroCGA.juXZJ8dCrk2xMNWHZyENZ0dJyhU')
