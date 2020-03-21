import discord
import random
import re
import requests
import asyncio

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

    if message.author == client.user:
        return

    msglower = message.content.lower()
    ments = message.mentions

    if msglower.startswith(pref + 'spit'):

        await message.delete()

        img = random.choice(range(len(pics)))

        color  = random.choice([discord.Color.dark_blue(), discord.Color.dark_gold(), discord.Color.dark_green(), discord.Color.dark_grey(), discord.Color.dark_magenta(), discord.Color.dark_orange(), discord.Color.dark_purple(), discord.Color.dark_red(), discord.Color.dark_teal()])

        emb = discord.Embed(
            description = '{} плюнул в {}'.format(message.author.mention, ments[0].mention),
            color = color
        )
        emb.set_image(url = '{}'.format(pics[int(img)]))
        
        await message.channel.send(embed = emb)



    if msglower.startswith(pref+'purge') or msglower.startswith(pref+'clear'):
        if message.author.guild_permissions.manage_messages or message.author.id == 400231667408699392:
            param = message.content.split(' ', 2)
            quantity = int(param[1])
            await message.delete()
            if quantity <= 100:
                if len(param) < 2:
                    await message.channel.send('Искользуйте: *purge [количество сообщений(не более 100)]', delete_after = 15)
                else:
                    trash = discord.Embed(
                        description = 'Выполняется очистка...',
                        color = 0x246f58
                    )
                    trash.set_image(url = 'https://i.imgur.com/mMrEVUW.gif')
                    purge = discord.Embed(
                        description = ':white_check_mark: Успешно удалено последних сообщений: **{}**'.format(quantity),
                        color = 0x246f58
                    )
                    purge.set_thumbnail(url = 'https://i.imgur.com/pm0FS6X.png')
                    await message.channel.send(embed = trash, delete_after = 2)
                    await asyncio.sleep(3)
                    await message.channel.purge(limit = quantity)
                    await message.channel.send(embed = purge, delete_after = 15)   
            else:
                await message.delete()
                await message.channel.send('Количество сообщений превышает 100!', delete_after = 15)
        else:
            await message.delete()
            await message.channel.send('У вас недостаточно прав на выполнение данной команды!', delete_after = 15)

    if msglower.startswith(pref+'addreac'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ')
            
            msghistory = await message.channel.history(limit = 100).flatten()
            try:
                for m in msghistory:
                    if int(msg[1]) == m.id:
                        mes = m
                        break
                else:
                    await message.channel.send('Сообщение не найдено!', delete_after = 15)
            
            except IndexError:
                await message.channel.send('Используйте: *addreac [message_id] [reaction]', delete_after = 15)
                return
            
            myemojis = client.emojis
            try:
                for e in myemojis:
                    if e.name in msg[2]:
                        emoji = e
                        await mes.add_reaction(emoji)
                        break
                else:
                    try:
                        await mes.add_reaction(msg[2])
                    except:
                        await message.channel.send('Эмодзи не найдено!', delete_after = 15)
            except IndexError:
                await message.channel.send('Используйте: *addreac [message_id] [reaction]', delete_after = 15)
                return

    if msglower.startswith(pref+'removereac'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ')
            
            msghistory = await message.channel.history(limit = 100).flatten()
            try:
                for m in msghistory:
                    if int(msg[1]) == m.id:
                        mes = m
                        break
                else:
                    await message.channel.send('Сообщение не найдено!', delete_after = 15)
            
            except IndexError:
                await message.channel.send('Используйте: *removereac [message_id] [reaction]', delete_after = 15)
                return
            
            myemojis = client.emojis
            try:
                for e in myemojis:
                    if e.name in msg[2]:
                        emoji = e
                        await mes.remove_reaction(emoji, message.guild.me)
                        break
                else:
                    try:
                        await mes.remove_reaction(msg[2], message.guild.me)
                    except:
                        await message.channel.send('Эмодзи не найдено!', delete_after = 15)
            except IndexError:
                await message.channel.send('Используйте: *removereac [message_id] [reaction]', delete_after = 15)
                return

    if msglower.startswith(pref+'delreacts'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ')
            
            msghistory = message.channel.history(limit = 100).flatten()
            try:
                for m in msghistory:
                    if int(msg[1]) == m.id:
                        msg = m
                        await msg.clear_reactions()
                        break
                else:
                    await message.channel.send('Сообщение не найдено!', delete_after = 15)
            except IndexError:
                await message.channel.send('Используйте: *delreacts [message_id]', delete_after = 15)
                return

    if msglower.startswith(pref+'myemo'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            content = message.content.split(' ', 1)
            await message.delete()
            emojinames = []
            emojipics = []
            emojis = client.emojis
            emojilist = []
            global myemojismsg, embedlist, emojiindex
            myemojismsg = discord.Message
            embedlist = []
            emojiindex = 0
            name = ''
            msg = ''
            for i in range(len(emojis)):
                name = str(emojis[i]).split(':', 2)
                name = name[1]
                name = name.replace('*', '\*')
                name = name.replace('`', '\`')
                name = name.replace('_', '\_')
                name = name.replace('~', '\~')
                name = name.replace('|', '\|')
                name = name.replace('<', '\<')
                name = name.replace('>', '\>')
                emojinames.append(name)
                emojipics.append(emojis[i])
            for e in range(len(emojinames)):
                msg += '{} - {}\n'.format(emojinames[e], emojipics[e])
                if e % 20 == 0 and e != 0:
                    emojilist.append(msg)
                    msg = ''
                    continue
            if msg == '':
                pass
            else:   
                emojilist.append(msg)
            for i in range(len(emojilist)):
                emojiembed = discord.Embed(
                    name = 'Мои эмодзи: ',
                    description = emojilist[i],
                    color = 0x704b60
                )
                emojiembed.set_author(
                    name = 'Страница #{}'.format(i+1),
                    icon_url = 'https://i.imgur.com/EuR39pj.gif'
                )
                emojiembed.set_footer(
                    text = 'Всего {} эмодзи'.format(len(emojis)),
                    icon_url = client.user.avatar_url
                )
                embedlist.append(emojiembed)
            if len(content) == 2:
                if 'all' in content[1]:
                    for i in range(len(embedlist)):
                        await message.author.send(embed = embedlist[i])
                elif 'count' in content[1]:
                    count = len(client.emojis)
                    await message.channel.send('У меня имеется {} эмодзи!'.format(count), delete_after = 20)
                else:
                    await message.channel.send('Используйте: *myemo ([all/count])', delete_after = 15)
            else:
                for i in range(len(embedlist)):
                    await message.author.send(embed = embedlist[i])

    if msglower.startswith(pref+'say'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ', 1)
            myemojis = client.emojis
            try:
                for e in myemojis:
                    if e.name in msg[1]:
                        try:
                            check = re.search(r'<:' + e.name + r':\d*>', msg[1])
                            check = check.group(0)
                            check = check[1:]
                        except:
                            msg[1] = msg[1].replace(':{}:'.format(e.name), str(e))
            except:
                await message.channel.send('Используйте: *say [message]', delete_after = 15)
                return

            await message.channel.send(msg[1])

    if msglower.startswith(pref+'inv') or msglower.startswith(pref+'invite'):

        if message.author.id == 400231667408699392:

            await message.delete()

            invme = discord.Embed(description = '**Пригласи меня на свой сервер :B**\nhttps://discordapp.com/oauth2/authorize?&client_id=583618052285923351&scope=bot&permissions=8', color = discord.Color.blue())

            await message.author.send(embed = invme)

@client.event
async def on_reaction_add(reaction, user):

    if user == client.user:
        return

    if str(reaction.emoji) == '🚩' and user.id == 400231667408699392:
        await reaction.message.delete()




client.run('NTgzNjE4MDUyMjg1OTIzMzUx.Xm6dNg.w1QQzbk1ADP_ZRh6cybsdW9VadY')