import discord
from discord.ext import commands




pref = "@"


bot = commands.Bot(command_prefix= commands.when_mentioned_or(pref))



gborder = "https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/star_border.gif"

ffemb = discord.Embed(title="FREE FIRE", description="**Garena Free Fire is a battle royal game. Played by millions of people. Developed by 111 dots studio and published by Garena. React on the emoji to access this game!**", color=discord.Color.blurple())
ffemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/freefire.png")


bgmiemb = discord.Embed(title="BGMI", description="**Battlegrounds Mobile India(BGMI), Made for players in India. It is an online multiplayer battle royale game developed and published by Krafton. React on the emoji to access this game**", color=discord.Color.blurple())
bgmiemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/bgmi.png")


codemb = discord.Embed(title="CALL OF DUTY", description="**Call Of Duty is a multiplayer online battle royal game, developed by TiMi Studio Group and published by Activision.react on the emoji to access this game**", color=discord.Color.blurple())
codemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/codm.png")

valoemb = discord.Embed(title="VALORANT", description="**Valorant is a multiplayer online battle royal game made for pc, developed and published by Riot Games. react on the emoji to access this game.", color=discord.Color.blurple())
valoemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/valorant.png**")







@bot.command()
async def grole(ctx):
  await ctx.send(embed=ffemb)
