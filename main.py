
import os
import discord
from discord.ext import commands
#from discord.ui import Button, View
#from keep_alive import keep_alive
from asyncio import sleep
#import humanfriendly
import datetime , time
import json
from data import color


blurple = 0x7289da
greyple = 0x99aab5
d_grey = 0x546e7a
d_theme = 0x36393F
l_grey = 0x979c9f
d_red = 0x992d22
red = 0xe74c3c
d_orange = 0xa84300
orange= 0xe67e22
d_gold = 0xc27c0e
gold = 0xf1c40f
magenta = 0xe91e63
purple = 0x9b59b6
d_blue = 0x206694 
blue = 0x3498db
green = 0x2ecc71
d_green = 0x1f8b4c
teal = 0x1abc9c
d_teal = 0x11806a
yellow = 0xffff00


pref = ','
bot = commands.Bot(command_prefix=commands.when_mentioned_or(pref),intents=discord.Intents.all())




'''
custom_prefixes = {}
#You'd need to have some sort of persistance here,
#possibly using the json module to save and load
#or a database
default_prefixes = ['&']

async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes

bot = commands.Bot(command_prefix = determine_prefix)

@bot.command()
@commands.has_permissions(administrator=True)
#@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    #You'd obviously need to do some error checking here
    #All I'm doing here is if prefixes is not passed then
    #set it to default 
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send(f"Prefixes set to `{prefixes}` ")
'''


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ATOMIC 8'))
    print(f'{bot.user} is ready')



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")



@bot.event
async def on_member_join(member):
	wchannel = bot.get_channel(881566918312595466)
	greet = bot.get_channel(880423346200784916)
	emb = discord.Embed(description=f"**Hey,{member.mention}\n<a:a8_welcome:977877642416111667>  TO ATOMIC 8 \n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:bh2:955529320368066590>╎Read Rules in <#880431068942053406> \n<a:bh2:955529320368066590>╎Chat with Server Members in <#880423346200784916> \n<a:bh2:955529320368066590>╎Take Self Roles From <#881567235053858867>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:heart_beat:955528805039104000> Thanks For Joining <a:heart_beat:955528805039104000>**", color=discord.Color.blurple())
	emb.set_image(url="https://github.com/Hunter87ff/a8esp/blob/main/assets/standard1.gif?raw=true")
	
	gret = discord.Embed(description=f"**<a:bh2:955529320368066590> WELCOME TO ATOMIC 8 <a:bh2:955529320368066590> **\n━━━━━━━━━▣✦▣━━━━━━━━\n<a:arow:982521407223246888> TAKE SELF ROLES FROM  <#881567235053858867>\n<a:arow:982521407223246888> READ RULES HERE <#880431068942053406>\n<a:arow:982521407223246888> FOR ANY HELP  <#899898526455181352>\n━━━━━━━━━▣✦▣━━━━━━━━\n** <a:heart_beat:955528805039104000> THANKS FOR JOINING <a:heart_beat:955528805039104000> **", color=discord.Color.blurple())
	await wchannel.send(embed=emb)
	await greet.send(f"{member.mention}", embed=gret)






@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please enter required Arguments **')
    elif isinstance(error, commands.CommandOnCooldown):
        return await ctx.send('**Try again <t:{}:R>**'.format(int(time.time() + error.retry_after)))
        print(ctx.message.content)
      
    elif isinstance(error, commands.MissingPermissions):
        return await ctx.send("You don't have permission to use this command")
        print(ctx.message.content) 

    elif isinstance(error, commands.DisabledCommand):
        return await ctx.send("This command is currenlty disabled. Please try again later")
        print(ctx.message.content)

    elif isinstance(error, commands.CommandNotFound):
        return await ctx.send("**Command not found! please check the spelling carefully**")
        print(ctx.message.content)

    elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        return await ctx.send("You dont have the exact role to use this command")
        print(ctx.message.content)

    elif isinstance(error, commands.UserInputError):
        return await ctx.send("**Invalid input**")
        print(ctx.message.content)

    else:
        e = str(error)
        await ctx.send(f"```py\n{e}```")







class Nhelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color = discord.Color.red())
#           emby.add_field(name='Support Server', value='[join](https://discord.gg/FXbRZHz3cG)', inline = False)
            await destination.send(embed=emby)
bot.help_command = Nhelp(no_category = 'Commands')

############################################################################################
#                                      GAME ROLES 
############################################################################################
    
    
    
    
gborder = "https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/star_border.gif"

ffemb = discord.Embed(title="FREE FIRE", description="**Garena Free Fire is a battle royal game. Played by millions of people. Developed by 111 dots studio and published by Garena. React on the emoji to access this game!**", color=discord.Color.blurple())
ffemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/freefire.png")


bgmiemb = discord.Embed(title="BGMI", description="**Battlegrounds Mobile India(BGMI), Made for players in India. It is an online multiplayer battle royale game developed and published by Krafton. React on the emoji to access this game**", color=discord.Color.blurple())
bgmiemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/bgmi.png")


codemb = discord.Embed(title="CALL OF DUTY", description="**Call Of Duty is a multiplayer online battle royal game, developed by TiMi Studio Group and published by Activision.react on the emoji to access this game**", color=discord.Color.blurple())
codemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/codm.png")

valoemb = discord.Embed(title="VALORANT", description="Valorant is a multiplayer online battle royal game made for pc, developed and published by Riot Games. react on the emoji to access this game.", color=discord.Color.blurple())
valoemb.set_thumbnail(url="https://raw.githubusercontent.com/Hunter87ff/atomic-8/main/Game_roles/valorant.png")






@bot.command()
@commands.has_permissions(manage_messages=True)
async def grole(ctx):
  await ctx.send(embed=valoemb)
  await ctx.send(gborder)
  await ctx.send(embed=codemb)
  await ctx.send(gborder)
  await ctx.send(embed=bgmiemb)
  await ctx.send(gborder)
  await ctx.send(embed=ffemb)



@bot.command(help=f"types[ solo1, solo2, squad]")
@commands.has_permissions(manage_messages=True)
async def tf(ctx, link, type):
    if "solo1" in type:
        so1 = discord.Embed(title="A8 DAILY SCRIM", description=f"**MODE : SOLO\nPRIZE POOL : 50INR\nIDP TIME : 3PM (CHANGABLE)\nSTART TIME : AFTER 7 MIN OF IDP\n\n[REGISTER LINK]({link})**", color=blurple)
        await ctx.channel.purge(limit=1)
        solo1 = await ctx.send("<@&960210472211206175>", embed=so1)
        await solo1.add_reaction("✅")

        
        
    elif "solo2" in type:
        so2 = discord.Embed(title="A8 DAILY SCRIM", description=f"**MODE : SOLO\nPRIZE POOL : 50INR\nIDP TIME : 3:30PM (CHANGABLE)\nSTART TIME : AFTER 7 MIN OF IDP\n\n[REGISTER LINK]({link})**", color=blurple)
        await ctx.channel.purge(limit=1)
        solo2 =  await ctx.send("<@&960210472211206175>", embed=so2)
        await solo2.add_reaction("✅")
                
        
        
    elif "squad" in type:
        smb = discord.Embed(title="A8 DAILY SCRIM", description=f"**MODE : SQUAD\nPRIZE POOL : 50INR\nIDP TIME : 7:30PM (CHANGABLE)\nSTART TIME : AFTER 7 MIN OF IDP\n\n[REGISTER LINK]({link})**", color=blurple)
        await ctx.channel.purge(limit=1)
        squad = await ctx.send("<@&960210472211206175>" , embed=smb)
        await squad.add_reaction("✅")


    else:
        return await ctx.send("**Please enter a valid type\nTypes: solo1, solo2 , squad**")
        




#tournament setup (category and channels)
@bot.command(aliases=['ts','tsetup'])
@commands.has_permissions(manage_channels=True)
async def tourney_setup(ctx,front,*,category=None):
    reason= f'Created by {ctx.author.name}'
    category = await ctx.guild.create_category(category, reason=f"{ctx.author.name} created")
    await ctx.guild.create_text_channel(str(front)+"info", category=category, reason=reason)
    await ctx.guild.create_text_channel(str(front)+"updates", category=category,reason=reason)
    await ctx.guild.create_text_channel(str(front)+"roadmap", category=category,reason=reason)
    await ctx.guild.create_text_channel(str(front)+"how-to-register", category=category, reason=reason)
    await ctx.guild.create_text_channel(str(front)+"register-here", category=category, reason=reason)
    await ctx.guild.create_text_channel(str(front)+"confirmed-teams", category=category, reason=reason)
    await ctx.guild.create_text_channel(str(front)+"groups", category=category, reason=reason)
    await ctx.guild.create_text_channel(str(front)+"queries", category=category, reason=reason)
    await ctx.send(f'**<:vf:910094232574894100> Successfully Created**',delete_after=5)

		 

	
############################################################################################
#                                       INFO
############################################################################################
  
#check latency
@bot.command()
async def ping(ctx):
    await ctx.send(f'**Current ping is {round(bot.latency*1000)} ms**')

@bot.command()
async def bot_info(ctx):
    description = f"**My name is ATOMIC 8, \nOfficial Bot Of ATOMIC 8 \nMy developer is `Hunter87#8787` \n\n:heart: Thanks for using this command**"
    embed = discord.Embed(title='ABOUT ME', description=description, color = discord.Color.blue())
    await ctx.send(f'{ctx.author.mention}',embed=embed)


bot.run(os.environ['TOKEN'])