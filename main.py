import conf
import discord
from discord.ext import commands



# # Настройки INTENTS
# intense = discord.Intents.default()
# intense.members = True

# client = discord.Client(intents = intense)

# @client.event
# async def on_message(message):
# # <Message 
# # id=825338226058461184 
# # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539>
# # type=<MessageType.default: 0>
# # author=<Member id=459312368321691660 name='Twinkle | J4F' discriminator='2408' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
# # flags=<MessageFlags value=0>>

#     if message.author == client.user:
#         return

#     if message.author.bot:
#         return


#     if message.channel.id == 825339475810582651:
#         # отправляем сообщение с send
#         msg = None


#         ctx = message.content.split(" ",maxsplit = 1)

#             # 1
#         if message.content == "/hello":
#             msg = f'Hello, {message.author.name}. I am {client.user.name}'

#             # 2
#         elif message.content == "/about_me":
#             msg = f'Hello, {message.author.name}. Your id is {client.user.id}'

#             # 3
#         elif ctx[0] ==  "/repeat":
#             msg = ctx[1]

#             # 4
#         elif ctx[0] == "/get_member":
#             if message.author.guild.name == "Bots":
#                 for member in list(enumerate(message.author.guild.members)):
#                     if member.id == int(ctx[1]):
#                         msg += f'He is {member.name}'

#             # 5
#         elif message.content == "/get_members":
#             msg = "1"
#             if message.author.guild.name == "Bots":
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     # "1. name {nick} id"
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
#             # 6
#         elif message.content == "/get_channels":
#             msg = " "
#             if message.author.guild.name == "Bots":
#                 for idx, channel  in list(enumerate(message.author.guild.channels)):
#                     msg += f'{idx+1}. {channel.name} - {channel.id}\n'
#                     print(channel.name)
        
#             # 7
#         # elif 

#         if msg != None:
#             await message.channel.send(msg)


# client.run(conf.bot_token)





bot = commands.Bot(command_prefix = "!")


# args - tuple
@bot.command(name = "hello")
async def command_hello(ctx, *args):

    message = " ".join(args)
    if ctx.channel.id == 825339475810582651:
        msg = f'Hello to you! You said: "{message}"'
        await ctx.channel.send(msg)




bot.run(conf.bot_token)