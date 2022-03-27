import discord
from discord.ext import commands




pref = "@"


bot = commands.Bot(command_prefix= commands.when_mentioned_or(pref))




ff = "Garena Free Fire Max is a battle royal game. Played by millions of people. Developed by 111 dots studio and published by Garena. React on the emoji to access this game!"

ffemb = discord.Embed(title="FREE FIRE", description=ff, color=discord.Color.blurple())
ffemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/freefire.png")







@bot.command()
async def grole(ctx):
  await ctx.send(embed=ffemb)