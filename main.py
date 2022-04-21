
import os
import discord
from discord.ext import commands
#from discord.ui import Button, View
#from keep_alive import keep_alive
from asyncio import sleep
import datetime
#import humanfriendly




pref = '@'
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



@bot.event
async def on_member_join(member):
	channel = bot.get_channel(881566918312595466)
	emb = discord.Embed(description=f"**Hey,{member.mention}\n<a:a8welcome:912175487189663754>  TO ATOMIC 8 \n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:bh2:955529320368066590>╎Read Rules in <#880431068942053406> \n<a:bh2:955529320368066590>╎Chat with Server Members in <#880423346200784916> \n<a:bh2:955529320368066590>╎Take Self Roles From <#881567235053858867>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━\n<a:heart_beat:955528805039104000> Thanks For Joining <a:heart_beat:955528805039104000>**", color=discord.Color.blurple())
	emb.set_image(url="https://github.com/Hunter87ff/a8esp/blob/main/assets/standard1.gif?raw=true")
	await channel.send(embed=emb)

  
##########################################################################################
#                                          USER AND SERVER COMMANDS
############################################################################################
@bot.command(aliases=['av'])
async def avatar(ctx, member: discord.Member = None):
	if member == None:
		 member = ctx.author
	await ctx.send(member.avatar_url)

'''@bot.command(aliases=['sav'])
async def server_avatar(ctx):
	guild = ctx.guild
	await ctx.send(guild.icon.url)'''



@bot.command(aliases=['bnr'])
async def banner(ctx, user:discord.Member = None ):
    if user == None:
        user = ctx.author
    req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif?size=1024"
    await ctx.send(f"{banner_url}")

@bot.command(pass_context=True)
async def tag(ctx):
  member = ctx.author
  nick = f'"   𝐀𝟖 |' + ctx.author.name
  await member.edit(nick=nick)
  await ctx.channel.purge(limit=1)
  await ctx.send("Done", delete_after=5)


@bot.command()
async def prefix(ctx):
	await ctx.channel.purge(limit=1)
	await ctx.send(f"** My prefix is `{pref}`**")
##########################################################################################
#                                          VOICE COMMANDS
############################################################################################







##########################################################################################
#                                          TEXT COMMANDS
############################################################################################

class Nhelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color = discord.Color.red())
#           emby.add_field(name='Support Server', value='[join](https://discord.gg/FXbRZHz3cG)', inline = False)
            await destination.send(embed=emby)
bot.help_command = Nhelp(no_category = 'Commands')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def em(ctx, url,* , msg):
  emb = discord.Embed(description=msg, color=discord.Color.red())
  emb.set_image(url=url)
  await ctx.channel.purge(limit=1)
  await ctx.send(embed=emb)


  
#embed command
@bot.command(aliases=['emb'])
async def embed(ctx, *, msg):
    embed = discord.Embed(description=msg, color=4 * 5555)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


#clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'**<:vf:910094232574894100>  Successfully cleared {amount} messages**',delete_after=5)





#react command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def react(ctx,message_id,* emojis):
  for emoji in emojis:
    channel = ctx.channel
    msg = await channel.fetch_message(message_id)
    await msg.add_reaction(emoji)
    await channel.purge(limit=1)




@bot.command()
@commands.has_role(956071928563630120)
@commands.cooldown(2, 10, commands.BucketType.user)
async def dm(ctx, member:discord.Member, *, message):
    embed = discord.Embed(description=message, color= discord.Color.blue())
    embed.set_footer(text=f'{ctx.author}',icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)



############################################################################################
#                                          ROLE COMMANDS
############################################################################################


#create role
@bot.command(aliases=['crole'],help="**Use this command to crate roles\nExample: &crole Family**")
@commands.has_permissions(manage_roles=True)
async def create_roles(ctx, *names):
    for name in names:
        guild = ctx.guild
        await guild.create_role(name=name)
        await ctx.send(f"**<:vf:910094232574894100>  Role `{name}` has been created**")


#delet role
@bot.command(aliases=['drole'])
@commands.has_permissions(manage_roles=True)
async def delete_roles(ctx, *roles: discord.Role):
    for role in roles:
        await ctx.send(f'**<:vf:910094232574894100>  Role {role.name} has been deleted**')
        await role.delete()
        await ctx.channel.purge(limit=2)


#role give
@bot.command(aliases=['role'], pass_context=True,help="Use this command to give role to someone \nExample : &role  @family @hunter")
@commands.has_permissions(manage_roles=True)
async def give_role(ctx,role: discord.Role, user: discord.Member):
	if ctx.author.top_role < role:
		return await ctx.send("you don't have enough permission")
	if ctx.author.top_role > role:
		return await user.add_roles(role)



#role remove
@bot.command(aliases=['rrole'], pass_context=True,help="Use this command to remove role from someone \n \n Example : &rrole @role @hunter ")
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, role:discord.Role, user: discord.Member):
  if ctx.author.top_role > role:
    return await user.remove_roles(role)
  if ctx.author.top_role < role:
    return await ctx.send('**You can not do this**')
    
    
    
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



############################################################################################
#                                      CHANNEL COMMANDS
############################################################################################


#lock command
@bot.command(help=" Use this command to lock a channel")
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.channel.purge(limit=1)
    await ctx.send('**<:vf:910094232574894100>  Channel has been locked**', delete_after=5)
    


#unlock command
@bot.command(help=" Use this command to lock a channel")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
    await ctx.channel.purge(limit=1)
    await ctx.send('**<:vf:910094232574894100>  Channel has been unlocked**', delete_after=5)



#hide channel
@bot.command(help=" Use this command to hide a channel")
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=False)
    await ctx.channel.purge(limit=1)
    await ctx.send('**<:vf:910094232574894100> This channel is hidden from everyone**',delete_after=5)


#unhide channel
@bot.command(help=" Use this command to unhide a channel")
@commands.has_permissions(manage_channels=True)
async def unhide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=True)
    await ctx.channel.purge(limit=1)
    await ctx.send('**<:vf:910094232574894100> This channel is visible to everyone**', delete_after=5)


#channel create
@bot.command(aliases=['chm'])
@commands.has_permissions(manage_channels=True)
async def channel_create(ctx, *names):
    for name in names:
        await ctx.guild.create_text_channel(name)
        await ctx.send(f'**<:vf:910094232574894100> `{name}` has been created**',delete_after=5)
        await sleep(1)


#channel delete
@bot.command(aliases=['chd'])
@commands.has_permissions(manage_channels=True)
async def channel_del(ctx, *channels: discord.TextChannel):
    for ch in channels:
        await ch.delete()
        await ctx.send(f'**<:vf:910094232574894100> `{ch.name}` has been deleted**',delete_after=5)
        await sleep(1)



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



#delete category
@bot.command(aliases=['dc'])
@commands.has_permissions(administrator=True)
async def delete_category(ctx,category: discord.CategoryChannel):
	channels = category.channels
	for channel in channels:
		await channel.delete(reason=f'Deleted by {ctx.author.name}')
		await ctx.send(f'**<:vf:910094232574894100> Successfully deleted  by {ctx.author.name}**', delete_after=5)

	 
    
#create channel by category id
@bot.command(aliases=['cch'])
@commands.has_permissions(manage_channels=True)
async def create_channels(ctx,category,name):
	    category = await bot.fetch_channel(category)
	    await ctx.guild.create_text_channel(name, category=category, reason=f"{ctx.author} created")
		 


		 
############################################################################################
#                                       KICK / BAN / MUTE
############################################################################################
'''@bot.command()
async def mute(ctx,member:discord.Member, time,*, reason):
	time = humanfriendly.parse_time(time)
	await member.edit(timeout=discord.utils.utcnow()=datetime.timedelta(seconds=time))
  await ctx.send(f"Member Successfully Muted")'''

#kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, reason=None):
	if reason == None:
		reason = f"{user} kicked by {ctx.author}"
	if ctx.author.top_role < user.top_role:
		return await ctx.send('**You can not kick him**')
	if ctx.author.top_role > user.top_role:
		return await ctx.guild.kick(user, reason=reason)


#ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, reason=None):
	if reason == None:
		reason = f"{user} banned by {ctx.author}"
	if ctx.author.top_role < user.top_role:
		return await ctx.send('**You can not ban him**')
	if ctx.author.top_role > user.top_role:
		return await ctx.guild.ban(user, reason=reason)
	
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
