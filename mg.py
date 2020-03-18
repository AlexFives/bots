import discord
import random
import re
import requests

botstream = discord.Streaming(name = 'Плевок: *spit @user', url = 'https://www.twitch.tv/alexfives')

pics = ['https://i.gifer.com/E5Wn.gif', 'https://i.gifer.com/5GHI.gif', 'https://i.gifer.com/1VkY.gif', 'https://i.gifer.com/8ksj.gif', 'https://i.gifer.com/7BtX.gif', 'https://i.gifer.com/7BtW.gif', 'https://i.gifer.com/Nfla.gif', 'https://i.gifer.com/79sV.gif', 'https://i.gifer.com/COyS.gifэб', 'https://i.gifer.com/Q55W.gif', 'https://i.gifer.com/fzsG.gif', 'https://i.gifer.com/KF6q.gif']

client = discord.Client()

pref = '*'

@client.event
async def on_ready():
    print('Lets go!')
    await client.change_presence(status=discord.Status.dnd, activity=botstream)

@client.event
async def on_message(message):

    msg = message.content
    ments = message.mentions

    if msg.startswith(pref + 'spit'):

        await message.delete()

        img = random.choice(range(len(pics)))

        color  = random.choice([discord.Color.dark_blue(), discord.Color.dark_gold(), discord.Color.dark_green(), discord.Color.dark_grey(), discord.Color.dark_magenta(), discord.Color.dark_orange(), discord.Color.dark_purple(), discord.Color.dark_red(), discord.Color.dark_teal()])

        emb = discord.Embed(
            description = '{} плюнул в {}'.format(message.author.mention, ments[0].mention),
            color = color
        )
        emb.set_image(url = '{}'.format(pics[int(img)]))
        
        await message.channel.send(embed = emb)

    if msg.startswith(pref+'say'):

        if message.author.guild_permissions.administrator or message.author.id = 400231667408699392:
            if 'Embed' in msg:
                msg = msg[5:]

                try:
                    say = eval(msg)
                    await message.channel.send(embed = say)
                except Exception:
                    print(Exception)

                    await message.channel.send('Используйте:\n!say discord.Embed(title = \'[text]\', description = \'[text]\', color = \'[hex]\')\n.set_image(url = \'[http(s)://(image)]\')\n.set_thumbnail(url = \'[http(s)://(image)]\')\n.set_footer(text = \'[text]\', icon_url = \'[http(s)://(image)]\')\n.set_author(name = \'[text]\', url = \'[http(s)://]\', icon_url = \'[http(s)://(image)]\')\n.add_field`можно писать несколько раз`(name = \'[text]\', value = \'[text]\', inline = [True/False])')

    if msg.startswith(pref+'writeas'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 2)
            await message.delete()
            webhooks = await message.channel.webhooks()
            try:
                web = webhooks[0]
                webid = web.id
                webtoken = web.token
            except:
                try:
                    web = await message.channel.create_webhook(name = 'tulen', avatar = message.guild.me.avatar_url)
                    webid = web.id
                    webtoken = web.token
                except:
                    await message.channel.send('Невозможно создать вебхук!', delete_after = 15)
                    return
            try:
                author = msg[1].replace('<', '')
                author = author.replace('>', '')
                author = author.replace('@', '')
                author = message.guild.get_member(int(author))
            except:
                await message.channel.send('Используйте: -writeas [author] [message]', delete_after = 15)
                return
            webhook = discord.Webhook.partial(
                id = webid,
                token = webtoken,
                adapter = discord.RequestsWebhookAdapter()
            )
            try:
                content = msg[2]
            except:
                await message.channel.send('Используйте: -writeas [author] [message]', delete_after = 15)
                return
            webhook.send(
                content = content,
                username = author.display_name,
                avatar_url = author.avatar_url,
            )




client.run('NTgzNjE4MDUyMjg1OTIzMzUx.Xm6dNg.w1QQzbk1ADP_ZRh6cybsdW9VadY')