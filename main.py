import conf
import discord

# Настройки INTENTS
intense = discord.Intents.default()
intense.members = True

client = discord.Client(intents = intense)

@client.event
async def on_message(message):
# <Message 
# id=825338226058461184 
# channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539>
# type=<MessageType.default: 0>
# author=<Member id=459312368321691660 name='Twinkle | J4F' discriminator='2408' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
# flags=<MessageFlags value=0>>

    if message.author == client.user:
        return

    if message.author.bot:
        return


    if message.channel.id == 825339475810582651:
        # отправляем сообщение с send
        msg = None


        ctx = message.content.split(" ",maxsplit = 1)

        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name}'

        elif message.content == "/about_me":
            msg = f'Hello, {message.author.name}. Your id is {client.user.id}'

        elif ctx[0] ==  "/repeat":
            msg = ctx[1]


        elif message.content == "/get_members":
            msg = "1"
            if message.author.guild.name == "Bots":
                for idx, member in list(enumerate(message.author.guild.members)):
                    # 1. name
                    msg += f'{idx+1}. {member.name}  { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'
        

        if msg != None:
            await message.channel.send(msg)



client.run(conf.bot_token)