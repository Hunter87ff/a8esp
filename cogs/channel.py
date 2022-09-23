import discord
from discord.ext import commands
from asyncio import sleep
cmd = commands

class Channel(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.counter = 0





	@cmd.command(aliases=['chm'])
	@commands.has_permissions(manage_channels=True)
	@commands.bot_has_permissions(manage_channels=True, send_messages=True, manage_messages=True)
	async def channel_make(self, ctx, *names):
		for name in names:
			await ctx.guild.create_text_channel(name)
			await ctx.send(f'**<:vf:947194381172084767>`{name}` has been created**',delete_after=5)
			await sleep(1)


	@cmd.command(aliases=['chd'])
	@commands.has_permissions(manage_channels=True, send_messages=True)
	@commands.bot_has_permissions(manage_channels=True, send_messages=True, manage_messages=True)
	async def channel_del(self, ctx, *channels: discord.TextChannel):
		for ch in channels:
			await ch.delete()
			await ctx.send(f'**<:vf:947194381172084767>`{ch.name}` has been deleted**',delete_after=5)
			await sleep(1)



	@cmd.command(aliases=['dc'])
	@commands.has_permissions(administrator=True)
	@commands.bot_has_permissions(manage_channels=True, send_messages=True, manage_messages=True)
	async def delete_category(self, ctx, category: discord.CategoryChannel):
		snd = await ctx.send("<a:loading:969894982024568856>**Processing...**")
		for channel in category.channels:
			await channel.delete(reason=f'Deleted by {ctx.author.name}')

			if len(category.channels) == 0:
				await category.delete()
				await snd.edit(content=f'**<:vf:947194381172084767>Successfully Deleted**')




	@cmd.command(aliases=['cch'])
	@commands.has_permissions(manage_channels=True)
	@commands.bot_has_permissions(manage_channels=True, send_messages=True)
	async def create_channel(self, ctx, category, *names):
	  for name in names:
	    category = await discord.utils.get(ctx.guild.categories, category)
	    await ctx.guild.create_text_channel(name, category=category, reason=f"{ctx.author} created")
	    await ctx.send("Done", delete_after=5)





async def setup(bot):
	await bot.add_cog(Channel(bot))
