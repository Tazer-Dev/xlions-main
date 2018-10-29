import Discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
bot = commands.Bots(command_prefix = '!')

@Client.event
async def on_ready():
    print("Welcome To " + bot.user.name + " Bot")

@Client.event
async def on_member_join(member):
    Welcome = get_channel("506482053810749450")
    await bot.send_message(Welcome, "Welcome " + member.mention)

bot.run("8t2NS66ru1AGF4DOdh2VDePAB2GzDDXE")