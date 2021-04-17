import conf
import discord
from discord.ext import commands
import img_handler as imhl



# # Настройки INTENTS
intentse = discord.Intents.default()
intentse.members = True



bot = commands.Bot(command_prefix = "!", intents = intentse)


channel = 825328622654193675

@bot.command(name="get_member")
async def get_member(ctx, member:discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'


        if msg == None:
            msg = "error"
        
        await ctx.channel.send(msg)

@bot.command(name="mk")
async def get_member(ctx,f1:discord.Member=None,f2:discord.Member=bot.user):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            await imhl.vs_create(f1.avatar_url, f2.abatar_url)

            await ctx.channel.send(file =discord.file(os.path.join("./img/result.png"))


bot.run(conf.bot_token)