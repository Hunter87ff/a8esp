import discord
from discord.ext import commands


bot = commands.Bot(command_prefix= when_mentioned_or("@"))




ff = "Garena Free Fire Max is a battle royal game. Played by millions of people. Developed by 111 dots studio and published by Garena. React on the emoji to access this game!"

ffemb = discord.Embed(title="FREE FIRE", description=ff, color=discord.Color.blurple())







@bot.command()
async def grole(ctx):
  await ctx.send(embed=ffemb)