import discord
from discord.ext import commands
from discord import app_commands
import imageTest

from dotenv import dotenv_values
import os

secrets = dotenv_values(".gitignore\key.env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        sync = await bot.tree.sync()
        print(f"Synced {len(sync)} commands")
    except Exception as e:
        print(e)
        bot.close()

@bot.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Hello")

@bot.tree.command(name="get")
@app_commands.describe(img = "place image")
async def recieve(interaction: discord.Integration, img : discord.Attachment):
    url = img

    read = imageTest.imageReader()
    text = read.extract_text(url)

    word_split = text.split()
    
    print(word_split)

    print(word_split[word_split.index("time") + 6], "-" , word_split[word_split.index("wpm") + 1], word_split[word_split.index("acc") + 1])

    await interaction.response.send_message(text)
    

bot.run(secrets["BOT_KEY"])