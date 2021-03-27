import conf
import discord

client = discord.Client()

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
        msg = f'Hello, {message.author.name}! - your message {message.content}'
        # отправляем сообщение с send
        msg = None




        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name}'
        elif message.content == "/about me":
            msg = f'Your id {message.id}, your nickname {client.user.name}'



        if msg != None:
            await message.channel.send(msg)



client.run(conf.bot_token)