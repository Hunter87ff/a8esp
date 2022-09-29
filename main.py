import os 
import discord
from discord.ext import commands
from asyncio import sleep
import datetime
from datetime import datetime, timedelta
import requests
from discord.ui import Button, View
import wavelink
import time



intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
intents.voice_states = True
pref = ","





bot = commands.Bot(command_prefix= commands.when_mentioned_or(pref), intents=intents ) 
#allowed_mentions = discord.AllowedMentions(roles=True, users=True, everyone=True),

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    await load_extensions()
    await node_connect()
    print(f"{bot.user} is Ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ATOMIC 8"))




@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"Node {node.identifier} is ready")

async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot = bot, host='lavalink.oops.wtf', port=443, password="www.freelavalink.ga", https=True)






    


   
   
	
@bot.event
async def on_member_join(member):
	wchannel = bot.get_channel(881566918312595466)
	greet = bot.get_channel(880423346200784916)
	emb = discord.Embed(description=f"**Hey,{member.mention}\nWELCOME TO ATOMIC 8 \n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:bh2:955529320368066590>╎Read Rules in <#880431068942053406> \n<a:bh2:955529320368066590>╎Chat with Server Members in <#880423346200784916> \n<a:bh2:955529320368066590>╎Take Self Roles From <#881567235053858867>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:heart_beat:955528805039104000> Thanks For Joining <a:heart_beat:955528805039104000>**", color=discord.Color.blurple())
	emb.set_image(url="https://github.com/Hunter87ff/a8esp/blob/main/assets/standard1.gif?raw=true")
	
	gret = discord.Embed(description=f"**<a:bh2:955529320368066590> WELCOME TO ATOMIC 8 <a:bh2:955529320368066590> **\n━━━━━━━━━▣✦▣━━━━━━━━\n<a:party:929019432150380555>  TAKE SELF ROLES FROM  <#881567235053858867>\n <a:party:929019432150380555>  READ RULES HERE <#880431068942053406>\n <a:party:929019432150380555>  FOR ANY HELP  <#899898526455181352>\n━━━━━━━━━▣✦▣━━━━━━━━\n** <a:heart_beat:955528805039104000> THANKS FOR JOINING <a:heart_beat:955528805039104000> **", color=discord.Color.blurple())
	await wchannel.send(embed=emb)
	await greet.send(f"{member.mention}", embed=gret)






	
##########################################################################################
#                                          TEXT COMMANDS
############################################################################################

class Nhelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color = discord.Color.blurple())
            await destination.send(embed=emby)
bot.help_command = Nhelp(no_category = 'Commands')




@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        err = discord.Embed(color=0xff0000, description="Missing Required Arguments")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.MissingPermissions):
        err = discord.Embed(color=0xff0000, description="You don't have Permissions To Use This Command")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.DisabledCommand):
        err = discord.Embed(color=0xff0000, description="This Command Is Currently Disabled! You Can Try Again Later")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.CommandNotFound):
        err = discord.Embed(color=0xff0000, description="Command Not Found! Please Check Spelling Carefully.")
        return await ctx.send(embed=err)


    elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        err = discord.Embed(color=0xff0000, description="You Do Not Have The Exact Role To Use This Command")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.UserInputError):
        err = discord.Embed(color=0xff0000, description="Please Enter Valid Arguments")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.EmojiNotFound):
        err = discord.Embed(color=0xff0000, description="Emoji Not Found")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.NotOwner):
        err = discord.Embed(color=0xff0000, description="This Is A Owner Only Command You Cant Use It")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.MessageNotFound):
        err = discord.Embed(color=0xff0000, description="Message Not Found Or Deleted")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.MemberNotFound):
        err = discord.Embed(color=0xff0000, description="Member Not Found")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.ChannelNotFound):
        err = discord.Embed(color=0xff0000, description="Channel Not Found")
        return await ctx.send(embed=err)
    elif isinstance(error, commands.GuildNotFound):
        return await ctx.send("**I'm Not In The Server! which You Want To See**", delete_after=19)

    elif isinstance(error, commands.ChannelNotReadable):
        err = discord.Embed(color=0xff0000, description="Can Not Read Messages Of The Channel")
        return await ctx.send(embed=err)

    elif isinstance(error, commands.CommandOnCooldown):
        e = str(error)
        err = discord.Embed(color=0xff0000, description=e)
        return await ctx.send(embed=err)

    elif "Manage Messages" in str(error):
        return await ctx.send(embed=discord.Embed(description="Missing `Manage Messages` Permission", color=0xff0000))

    elif "Unknown file format." in str(error):
        return await ctx.send(embed=discord.Embed(description="Invalid Input", color=0xff0000))

    elif "403 Forbidden (error code: 50013): Missing Permissions" in str(error):
        try:
            return await ctx.author.send(embed=discord.Embed(description=f"I don't have Permissions To Send message in this channel - {ctx.channel.mention}", color=0xff0000))
        except:
            return

    elif "This playlist type is unviewable." in str(error):
        return await ctx.send(embed=discord.Embed(description="This playlist type is unsupported!", color=0xff0000))

    elif "NotFound: 404 Not Found (error code: 10003): Unknown Channel" in str(error):
        try:
            return await ctx.send(embed=discord.Embed(description="Channel Deleted Or Invalid", color=0xff0000))
        except:
            return

    else:
        e = str(error)
        await ctx.send(f"```\n{e}\n```")







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
        smb = discord.Embed(title="A8 DAILY SCRIM", description=f"**MODE : SQUAD\nPRIZE POOL : 50INR\nIDP TIME : 7:00PM (CHANGABLE)\nSTART TIME : AFTER 7 MIN OF IDP\n\n[REGISTER LINK]({link})**", color=blurple)
        await ctx.channel.purge(limit=1)
        squad = await ctx.send("<@&960210472211206175>" , embed=smb)
        await squad.add_reaction("✅")


    else:
        return await ctx.send("**Please enter a valid type\nTypes: solo1, solo2 , squad**")
        









############################################################################################
#                                       INFO
############################################################################################
  

@bot.command()
@commands.cooldown(2, 20, commands.BucketType.user)
@commands.bot_has_permissions(manage_messages=True, send_messages=True)
async def ping(ctx):
    await ctx.send(f'**Current ping is {round(bot.latency*1000)} ms**')









@bot.command()
@commands.guild_only()
@commands.bot_has_permissions(manage_emojis=True)
@commands.has_permissions(manage_emojis=True)
async def addemoji(ctx, emoji: discord.PartialEmoji):
    if ctx.author.guild_permissions.manage_emojis:
        for g in bot.guilds:
            if g.id != ctx.guild.id:
                #emoji = discord.utils.get(g.emojis, name=name)
                return await ctx.send(f"{emoji} added", delete_after=10)
                emoji_bytes = await emoji.read()
                return await ctx.guild.create_custom_emoji(name=emoji.name, image=emoji_bytes, reason=f'Emoji Added By {ctx.author}')
    else:
        return await ctx.send("You Should Check Your Permission")




@bot.command(hidden=True)
async def sdm(ctx, member: discord.User, *, message):
    if ctx.author.id == 885193210455011369:
        await member.send(message)
    if ctx.author.id != 885193210455011369:
        return await ctx.send(embed=discord.Embed(description="Command not found! please check the spelling carefully", color=0xff0000))





bot.run(os.environ["TOKEN"])
