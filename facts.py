import os
import random, requests
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.command(name='facts', help='Responds with a random fact about fish') #You may edit this, this was just what I did for my use case.
async def nine_nine(ctx): #Do NOT change the nine_nine definition. This project was forked and modified from another one, and it will NOT work without the nine_nine definition.
    fax = [ #The 'Test', 'Test 2', 'Test 3' are correctly formatted. You can edit that text and add as much as you want. If you want to change the fish_fax value on this line, make sure to change the value of "response = random.choice(fish_fax)", changing fish_fax to whatever you would like to change it to. 
        'Test',
        'Test 2',
        'Test 3'
    ]
    response = random.choice(fax)
    await ctx.send(response)
bot.run("TOKEN") #Change this value to the actual bot token and surround it with quotes. In other words, replace the TOKEN value with the actual bot token value.
