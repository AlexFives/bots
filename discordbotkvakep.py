import discord
import random
import re
import asyncio
import time
import datetime
import os
import math
import colormap



botstream = discord.Streaming(name = 'Say: -help', url = 'https://www.twitch.tv/alexfives')

topfact1 = 'Всегда ищите Starmie с природой Adamant. Это  лучшее, что может быть для него.:thumbsup:'
topfact2 = 'Против фей очень эффективно ставить драконов, так как фея, тип атаки которой схож с её типом (STAB-эффект), ничего не сделает Вашему покемону, а вот дракон наоборот нанесёт двойной урон.:ok_hand:'
topfact3 = 'Всегда пытайтесь найти Staraptor\'a с природой Modest. Ничего не может быть лучше!:thumbsup:'
topfact4 = 'Если против Вас стоит Primal Kyogre или Primal Groudon, то нет ничего лучше, кроме как бежать, ибо они не контрятся!:frowning2: '
topfact5 = 'Если Вы увидели у противника Donphan\'a 25lvl, то уходите из боя, ведь он, будьте уверены, багнут и в любом случае выживет с 1 хп, когда Ваш любимец погибнет!:crying_cat_face: '
topfact6 = 'Каждому известно, что нельзя стоять под деревом во время грозы, ведь, если молния ударит в дерево, оно мало того, что загорится:fire:, так ещё и окружающая его земля также получит заряд, который способен причинить Вам вред. Так к чему это я... Эффективно бить атакой электрического типа земляных покемонов.:warning: Это подтверждают законы физики!:heavy_check_mark: '
topfact7 = ''
topfact8 = ''
topfact9 = ''
topfact10 = ''








client = discord.Client()






"""
 xxxxxx   xxx   xxx  xxxxxxxx   xxxxxx   xxx   xxx      ################
xxx    x  xxx   xxx  xxxx      xxx    x  xxx  xxx       ################
xxx       xxxxxxxxx  xxxxxxxx  xxx       xxxxxxx        ################
xxx    x  xxx   xxx  xxxx      xxx    x  xxx  xxx       ################
 xxxxxx   xxx   xxx  xxxxxxxx   xxxxxx   xxx   xxx      ################
"""
async def checks():
    while True:
        with open('kvakepmutedmembers.txt', 'r') as fin:
            with open('kvakepmutedmembersnew.txt', 'w') as fout:
                for line in fin:
                    try:
                        Y = re.search(r'Время: \d{4}-', line)
                        Y = Y.group(0)
                        Y = Y[7:]
                        Y = Y.replace('-', '')
                        Y = int(Y)
                        M = re.search(r'Время: \d{4}-\d{2}-', line)
                        M = M.group(0)
                        M = M[12:]
                        M = M.replace('-', '')
                        M = int(M)
                        D = re.search(r'Время: \d{4}-\d{2}-\d{2} ', line)
                        D = D.group(0)
                        D = D[15:]
                        D = D.replace(' ', '')
                        D = int(D)
                        h = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:', line)
                        h = h.group(0)
                        h = h[18:]
                        h = h.replace(':', '')
                        h = int(h)
                        m = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:', line)
                        m = m.group(0)
                        m = m[21:]
                        m = m.replace(':', '')
                        m = int(m)
                        s = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                        s = s.group(0)
                        s = s[24:]
                        s = int(s)

                        if datetime.datetime.today() > datetime.datetime(Y, M, D, h, m, s):
                            
                            guild = re.search(r'Сервер: \d{1,20};', line)
                            guild = guild.group(0)
                            guild = guild[8:]
                            guild = guild.replace(';', '')
                            guild = client.get_guild(int(guild))

                            member = re.search(r'Пользователь: \d{1,20};', line)
                            member = member.group(0)
                            member = member[14:]
                            member = member.replace(';', '')
                            member = guild.get_member(int(member))

                            for r in guild.roles:
                                if int(r.permissions.value) == 1049600:
                                    muterole = r
                                    break
                            else:
                                muterole = await guild.create_role(
                                    name = 'Muted',
                                    permissions = discord.Permissions(permissions = 1049600),
                                    color = discord.Color.dark_grey(),
                                    reason = 'Роль для мутов'
                                )
                            
                            for cat in guild.categories:
                                if cat.name == 'kvakep-logs':
                                    kvakeplogs = cat
                                    break
                            else:
                                kvakeplogs = await guild.create_category_channel(
                                    name = 'kvakep-logs',
                                    overwrites = overwrites,
                                    reason = 'Category for kvakep\'s logs'
                                )
                            for chan in kvakeplogs.channels:
                                if chan.name == 'mutes':
                                    muteslog = chan
                                    break
                            else:
                                muteslog = await kvakeplogs.create_text_channel(
                                    name = 'mutes',
                                    overwrites = overwrites,
                                    reason = 'Channel for kvakep\'s mutes'
                                )
                            
                            timenow = datetime.datetime.today()
                            year = timenow.year
                            month = timenow.month
                            if month == 1:
                                month = 'января'
                            elif month == 2:
                                month = 'февраля'
                            elif month == 3:
                                month = 'марта'
                            elif month == 4:
                                month = 'апреля'
                            elif month == 5:
                                month = 'мая'
                            elif month == 6:
                                month = 'июня'
                            elif month == 7:
                                month = 'июля'
                            elif month == 8:
                                month = 'августа'
                            elif month == 9:
                                month = 'сентября'
                            elif month == 10:
                                month = 'октября'
                            elif month == 11:
                                month = 'ноября'
                            elif month == 12:
                                month = 'декабря'
                            day = timenow.day
                            hour = timenow.hour
                            if hour == 1:
                                hour = '01'
                            elif hour == 2:
                                hour = '02'
                            elif hour == 3:
                                hour = '03'
                            elif hour == 4:
                                hour = '04'
                            elif hour == 5:
                                hour = '05'
                            elif hour == 6:
                                hour = '06'
                            elif hour == 7:
                                hour = '07'
                            elif hour == 8:
                                hour = '08'
                            elif hour == 9:
                                hour = '09'
                            elif hour == 0:
                                hour = '00'
                            minute = timenow.minute
                            if minute == 0:
                                minute = '00'
                            elif minute == 1:
                                minute == '01'
                            elif minute == 2:
                                minute == '02'
                            elif minute == 3:
                                minute == '03'
                            elif minute == 4:
                                minute == '04'
                            elif minute == 5:
                                minute == '05'
                            elif minute == 6:
                                minute == '06'
                            elif minute == 7:
                                minute == '07'
                            elif minute == 8:
                                minute == '08'
                            elif minute == 9:
                                minute == '09'
                            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

                            funnydogemoji = client.get_emoji(596690644467187723)
                            unmutetolog = discord.Embed(
                                description = 'С пользователя {} был снят мут!\n{}'.format(member.mention, funnydogemoji),
                                color = discord.Color.dark_green()
                            )
                            unmutetolog.set_footer(
                                text = timenow
                            )
                            unmutetomember = discord.Embed(
                                title = 'Хорошая новость!',
                                description = 'С Вас был снят мут!',
                                color = discord.Color.gold()
                            )
                            unmutetomember.set_footer(
                                text = timenow
                            )

                            await muteslog.send(embed = unmutetolog)
                            await member.remove_roles(muterole, reason = 'Unmute')
                            await member.send(embed = unmutetomember)
                        else:
                            fout.write(line)
                    except:
                        pass
                fout.close()
            fin.close()
        try:
            os.remove('kvakepmutedmembers.txt')
            os.renames('kvakepmutedmembersnew.txt', 'kvakepmutedmembers.txt')
        except:
            pass
        
        with open('kvakepbannedmembers.txt', 'r') as fin:
            with open('kvakepbannedmembersnew.txt', 'w') as fout:
                for line in fin:
                    try:
                        Y = re.search(r'Время: \d{4}-', line)
                        Y = Y.group(0)
                        Y = Y[7:]
                        Y = Y.replace('-', '')
                        Y = int(Y)
                        M = re.search(r'Время: \d{4}-\d{2}-', line)
                        M = M.group(0)
                        M = M[12:]
                        M = M.replace('-', '')
                        M = int(M)
                        D = re.search(r'Время: \d{4}-\d{2}-\d{2} ', line)
                        D = D.group(0)
                        D = D[15:]
                        D = D.replace(' ', '')
                        D = int(D)
                        h = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:', line)
                        h = h.group(0)
                        h = h[18:]
                        h = h.replace(':', '')
                        h = int(h)
                        m = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:', line)
                        m = m.group(0)
                        m = m[21:]
                        m = m.replace(':', '')
                        m = int(m)
                        s = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                        s = s.group(0)
                        s = s[24:]
                        s = int(s)

                        if datetime.datetime.today() > datetime.datetime(Y, M, D, h, m, s):
                            
                            guild = re.search(r'Сервер: \d{1,20};', line)
                            guild = guild.group(0)
                            guild = guild[8:]
                            guild = guild.replace(';', '')
                            guild = client.get_guild(int(guild))

                            member = re.search(r'Пользователь: \d{1,20};', line)
                            member = member.group(0)
                            member = member[14:]
                            member = member.replace(';', '')
                            member = guild.get_member(int(member))

                            for r in guild.roles:
                                if int(r.permissions.value) == 512:
                                    banrole = r
                                    break
                            else:
                                banrole = await guild.create_role(
                                    name = 'Banned',
                                    permissions = discord.Permissions(permissions = 512),
                                    color = discord.Color.dark_grey(),
                                    reason = 'Роль для банов'
                                )
                            
                            for cat in guild.categories:
                                if cat.name == 'kvakep-logs':
                                    kvakeplogs = cat
                                    break
                            else:
                                kvakeplogs = await guild.create_category_channel(
                                    name = 'kvakep-logs',
                                    overwrites = overwrites,
                                    reason = 'Category for kvakep\'s logs'
                                )
                            for chan in kvakeplogs.channels:
                                if chan.name == 'bans':
                                    banslog = chan
                                    break
                            else:
                                banslog = await kvakeplogs.create_text_channel(
                                    name = 'bans',
                                    overwrites = overwrites,
                                    reason = 'Channel for kvakep\'s bans'
                                )

                            timenow = datetime.datetime.today()
                            year = timenow.year
                            month = timenow.month
                            if month == 1:
                                month = 'января'
                            elif month == 2:
                                month = 'февраля'
                            elif month == 3:
                                month = 'марта'
                            elif month == 4:
                                month = 'апреля'
                            elif month == 5:
                                month = 'мая'
                            elif month == 6:
                                month = 'июня'
                            elif month == 7:
                                month = 'июля'
                            elif month == 8:
                                month = 'августа'
                            elif month == 9:
                                month = 'сентября'
                            elif month == 10:
                                month = 'октября'
                            elif month == 11:
                                month = 'ноября'
                            elif month == 12:
                                month = 'декабря'
                            day = timenow.day
                            hour = timenow.hour
                            if hour == 1:
                                hour = '01'
                            elif hour == 2:
                                hour = '02'
                            elif hour == 3:
                                hour = '03'
                            elif hour == 4:
                                hour = '04'
                            elif hour == 5:
                                hour = '05'
                            elif hour == 6:
                                hour = '06'
                            elif hour == 7:
                                hour = '07'
                            elif hour == 8:
                                hour = '08'
                            elif hour == 9:
                                hour = '09'
                            elif hour == 0:
                                hour = '00'
                            minute = timenow.minute
                            if minute == 0:
                                minute = '00'
                            elif minute == 1:
                                minute == '01'
                            elif minute == 2:
                                minute == '02'
                            elif minute == 3:
                                minute == '03'
                            elif minute == 4:
                                minute == '04'
                            elif minute == 5:
                                minute == '05'
                            elif minute == 6:
                                minute == '06'
                            elif minute == 7:
                                minute == '07'
                            elif minute == 8:
                                minute == '08'
                            elif minute == 9:
                                minute == '09'
                            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

                            funnydogemoji = client.get_emoji(596690644467187723)
                            unbanembed = discord.Embed(
                                description = 'С пользователя {} был снят бан!\n{}'.format(member.mention, funnydogemoji),
                                color = discord.Color.dark_green()
                            )
                            unbanembed.set_footer(
                                text = timenow
                            )
                            unban = discord.Embed(
                                title = 'Хорошая новость!',
                                description = 'С Вас был снят бан!',
                                color = discord.Color.gold()
                            )
                            unban.set_footer(
                                text = timenow
                            )

                            await banslog.send(embed = unbanembed)
                            await member.remove_roles(banrole, reason = 'Unban')
                            await member.send(embed = unban)
                        else:
                            fout.write(line)
                    except:
                        pass
                fout.close()
            fin.close()
        try:
            os.remove('kvakepbannedmembers.txt')
            os.renames('kvakepbannedmembersnew.txt', 'kvakepbannedmembers.txt')
        except:
            pass

        claninvites = open('claninvites.txt', 'r')
        lines = claninvites.readlines()
        claninvites.close()

        for line in lines:
            try:
                channel = re.search(r'ChannelId: \d*', line)
                channel = channel.group(0)
                channel = channel[11:]
                channel = client.get_channel(int(channel))

                msgid = re.search(r'MessageId: \d*;', line)
                msgid = msgid.group(0)
                msgid = msgid[11:]
                msgid = msgid.replace(';', '')
                msgid = int(msgid)

                channelhistory = await channel.history().flatten()
                for c in channelhistory:
                    if c.id == msgid:
                        msgid = c
                        break

                guild = re.search(r'Guild: \d*;', line)
                guild = guild.group(0)
                guild = guild[7:]
                guild = guild.replace(';', '')
                guild = client.get_guild(int(guild))

                member = re.search(r'Member: \d*;', line)
                member = member.group(0)
                member = member[8:]
                member = member.replace(';', '')
                member = guild.get_member(int(member))

                author = re.search(r'Author: \d*;', line)
                author = author.group(0)
                author = author[8:]
                author = author.replace(';', '')
                author = guild.get_member(int(author))

                clanrole = re.search(r'Clan: \d*;', line)
                clanrole = clanrole.group(0)
                clanrole = clanrole[6:]
                clanrole = clanrole.replace(';', '')
                clanrole = guild.get_role(int(clanrole))
                clanname = clanrole.name
                clanname = clanname[7:]

            except:
                pass
            
            try:
                reactions = msgid.reactions
                for r in reactions:
                    if str(r.emoji) == '👍' and r.count == 2:
                        usrs = await r.users().flatten()
                        for u in usrs:
                            if member == u:
                                await msgid.edit(content = 'Вы вступили в клан {}'.format(clanname), embed = None)
                                lines.remove(line)
                                break
                        else:
                            return

                    elif str(r.emoji) == '👎' and r.count == 2:
                        usrs = await r.users().flatten()
                        for u in usrs:
                            if member == u:
                                await msgid.delete()
                                lines.remove(line)
                                break
                        else:
                            return

                textname = clanname.replace(' ', '-')
                textname = textname.replace('!', '')
                textname = textname.replace('@', '')
                textname = textname.replace('#', '')
                textname = textname.replace('$', '')
                textname = textname.replace('%', '')
                textname = textname.replace('^', '')
                textname = textname.replace('&', '')
                textname = textname.replace('*', '')
                textname = textname.replace('(', '')
                textname = textname.replace(')', '')
                textname = textname.replace('~', '-')
                textname = textname.replace(';', '')
                textname = textname.replace(':', '')
                textname = textname.replace('\'', '')
                textname = textname.replace('"', '')
                textname = textname.replace('/', '')
                textname = textname.replace('\\', '')
                textname = textname.replace('|', '')
                textname = textname.replace('+', '')
                textname = textname.replace('?', '')
                textname = textname.replace(',', '')
                textname = textname.replace('№', '')
                textname = textname.replace('`', '')
                textname = textname.replace('', '')
                textname = textname.lower()

                deadpool = client.get_emoji(596695098205405185)
                joinembed = discord.Embed(
                    title = 'ClanInfo: ',
                    description = 'Пользователь {} вступил в клан!\nДобро пожаловать!\n{}'.format(member.mention, deadpool),
                    color = clanrole.color
                )
                joinembed.set_footer(
                    text = 'Пригласил {}'.format(author),
                    icon_url = author.avatar_url
                )

                for t in guild.text_channels:
                    if t.name == textname:
                        await t.send(embed = joinembed)
                        break

                await member.add_roles(clanrole)

            except:
                pass
            
            claninvitesnew = open('claninvitesnew.txt', 'w')
            claninvitesnew.writelines(lines)
            claninvitesnew.close()

            try:
                os.remove('claninvites.txt')
                os.renames('claninvitesnew.txt', 'claninvites.txt')
            except:
                pass

        await asyncio.sleep(10)



"""
 xxxxxxx   xxxxx    xxx      xxxxxxx    xxxxxxxx    xxxxxx  xxxxxxx   xx   xx      ################
xxx   xxx  xxx xx   xxx      xxx   xx   xxxx       xx   xx  xxx   xx  xx   xx      ################
xxx   xxx  xxx  xx  xxx      xxxxxxx    xxxxxxxx  xxxxxxxx  xxx   xx   xxxxxx      ################
xxx   xxx  xxx   xx xxx      xxx   xx   xxxx      xx    xx  xxx   xx       xx      ################
 xxxxxxx   xxx    xxxxx      xxx    xx  xxxxxxxx  xx    xx  xxxxxxx    xxxxx       ################
"""
@client.event
async def on_ready():
    print('{0.user} is ready!'.format(client))
    print('----------')
    await client.change_presence(status=discord.Status.dnd, activity=botstream)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(checks())

"""
 xxxxxxx   xxxxx    xxx      xxxxx     xxxxx  xxxxxxx   xxxxxxxxxx      ################
xxx   xxx  xxx xx   xxx      xxx xx   xx xxx  xxx      xx        x      ################
xxx   xxx  xxx  xx  xxx      xxx  xx xx  xxx  xxxxxxx  xx  xxxxx        ################
xxx   xxx  xxx   xx xxx      xxx   xxx   xxx      xxx  xx  xx  xx       ################
 xxxxxxx   xxx    xxxxx      xxx         xxx  xxxxxxx   xxxxxxxxx       ################
"""
@client.event
async def on_message(message):

    msglower = message.content.lower()

    if message.author == client.user:
        return

#000   000  00000000  000       000000
#000   000  0000      000       000  00
#000000000  00000000  000       000000
#000   000  0000      0000      000
#000   000  00000000  00000000  000
    if msglower.startswith('-help'):
        await message.delete()
        embed=discord.Embed(title="**Help:**", description="Здесь Вы можете просмотреть список моих команд.", color=0x00ff80)
        embed.add_field(
            name='***-evs [имя покемона на английском]\nили\n-evs [номер покемона в покедексе]***',
            value='Показывает ЕВс, которые даёт покемон после убийства.',
            inline=True
        )
        embed.add_field(
            name='***-evs [стат]***',
            value='Показывает покемонов, которые дают данный стат после убийства.\nCписок статов: Хп - hp, Атака - atk, Защита - def, Специальная атака - spa, Специальная защита - spd, Скорость - spe.',
            inline=True
        )
        embed.add_field(
            name='***-flip***',
            value='Случайное подбрасывание монетки.',
            inline=True
        )
        embed.add_field(
            name='***-lovelist*** или ***-ll***',
            value='Выводит список любимых игроков по мнению kvakep\'a. `(roflan)`',
            inline=True
        )
        embed.add_field(
            name='***-topfact*** или ***-tf***',
            value='kvakep рассказывает "топовый" факт, к которому лучше не прислушиваться. `(roflan)`',
            inline=True
        )
        embed.add_field(
            name='***-avatar*** или ***-ava***',
            value='Показывает аватарку пользователя.',
            inline=True
        )
        embed.add_field(
            name = '***-calc [выражение]***',
            value = 'Встроенный калькулятор, подробнее: -calc',
            inline = True
        )
        embed.set_footer(
            text="made by Alex5555"
        )
        embed.set_thumbnail(
            url='https://i.imgur.com/PkP3JUE.png'
        )
        await message.channel.send(embed=embed)

#000       000
#000       000
#000       000
#0000      0000
#00000000  00000000
    if msglower.startswith('-lovelist') or msglower.startswith('-ll'):
        await message.delete()
        embed=discord.Embed(title='***___Список любимых игроков сервера:___***', color=0x0a4a76)
        embed.add_field(
            name='wwwnekit',
            value='MaryFranc',
            inline=True
        )
        embed.add_field(
            name='fihid',
            value='Mephislofel',
            inline=True
        )
        embed.add_field(    
            name='Radells',
            value='Wwweter',
            inline=True
        )
        embed.add_field(
            name='kvakep',
            value='Be3yH4uK',
            inline=True
        )
        embed.add_field(
            name='hyper_44',
            value='Deepsy9',
            inline=True
        )
        embed.add_field(
            name='Hoochuu',
            value='BrOnYaShANyasha',
            inline=True
        )
        embed.set_footer(
            text='made by {}'.format(client.get_user(499284863686279201))
        )
        await message.channel.send(embed=embed)

#0000000000  000       0000  000000
#000         000        00   000  00
#0000000     000        00   000000
#000         0000       00   000
#000         00000000  0000  000
    if msglower.startswith('-flip'):
        await message.delete()
        orel1 = client.get_emoji(596784734571593748)
        reshka1 = client.get_emoji(596784735758319619)
        orel = 'https://i.imgur.com/lKRzOJT.png'
        reshka = 'https://i.imgur.com/RLrFINV.png'
        color = discord.Color.teal()
        flip = random.choice([orel, reshka])
        if flip == orel:
            msg = 'Орёл'
            emoji = orel1
        else:
            msg = 'Решка'
            emoji = reshka1
        flp = discord.Embed(
            description = 'Выбор монеты: **{}**!'.format(msg),
            color = color
        )
        flp.set_thumbnail(url = flip)
        m = await message.channel.send(embed = flp)
        await m.add_reaction(emoji)

#00000000  00   00  0000000
#0000      00   00  000
#00000000  00   00  0000000
#0000       00 00       000
#00000000    000    0000000
    if msglower.startswith('-evs'):
        await message.delete()
        msg = message.content.split(' ')
        
        try:
            pokorstat = msg[1].lower()
        except IndexError:
            await message.channel.send('Используйте: -evs [pokemon/stat]', delete_after = 15)
            return

        pokemoninfo = open('pokemoninfo.txt', 'r')
        lines = pokemoninfo.readlines()
        pokemoninfo.close()

        pok = 'Pokemon: {};'.format(pokorstat)
        num = 'Number: {};'.format(pokorstat)
        gstat = 'Stat: {};'.format(pokorstat)

        for line in lines:
            
            if pok in line:

                pokemon = re.search(r'Pokemon: .*; G', line)
                pokemon = pokemon.group(0)
                pokemon = pokemon[9:]
                pokemon = pokemon.replace(';', '')
                pokemon = pokemon.replace(' ', '')
                pokemon = pokemon.replace('G', '')
                pokemon = pokemon.title()

                number = re.search(r'Number: \d*;', line)
                number = number.group(0)
                number = number[8:]
                number = number.replace(';', '')

                givingevs = re.search(r'Give: .{1,30};', line)
                givingevs = givingevs.group(0)
                givingevs = givingevs[6:]
                givingevs = givingevs.replace(';', '')

                photo = re.search(r'Photo: .*;', line)
                photo = photo.group(0)
                photo = photo[7:]
                photo = photo.replace(';', '')
                break

            elif num in line:

                number = re.search(r'Number: \d*;', line)
                number = number.group(0)
                number = number[8:]
                number = number.replace(';', '')

                pokemon = re.search(r'Pokemon: .*; G', line)
                pokemon = pokemon.group(0)
                pokemon = pokemon[9:]
                pokemon = pokemon.replace(';', '')
                pokemon = pokemon.replace(' ', '')
                pokemon = pokemon.replace('G', '')
                pokemon = pokemon.title()

                givingevs = re.search(r'Give: .{1,30};', line)
                givingevs = givingevs.group(0)
                givingevs = givingevs[6:]
                givingevs = givingevs.replace(';', '')

                photo = re.search(r'Photo: .*;', line)
                photo = photo.group(0)
                photo = photo[7:]
                photo = photo.replace(';', '')
                break

            elif gstat in line:

                stat = re.search(r'Stat: \w*;', line)
                stat = stat.group(0)
                stat = stat[6:]
                stat = stat.replace(';', '')
                if stat == 'hp':
                    stat = 'Здоровье'
                elif stat == 'atk':
                    stat = 'Атака'
                elif stat == 'def':
                    stat = 'Защита'
                elif stat == 'spa':
                    stat = 'Специальная атака'
                elif stat == 'spd':
                    stat = 'Специальная защита'
                elif stat == 'spe':
                    stat = 'Скорость'

                gives = re.search(r'Pokemons: .*;', line)
                gives = gives.group(0)
                gives = gives[10:]
                gives = gives.replace(';', '')
                break
        else:

            plak = client.get_emoji(594173858085470208)
            fail = discord.Embed(
                description = 'К сожалению, ничего не найдено {}'.format(plak),
                color = discord.Color.dark_magenta()
            )
            await message.channel.send(embed = fail, delete_after = 15)
            return

        poketime = datetime.datetime.today()
        year = poketime.year
        month = poketime.month
        if month == 1:
            month = 'января'
        elif month == 2:
            month = 'февраля'
        elif month == 3:
            month = 'марта'
        elif month == 4:
            month = 'апреля'
        elif month == 5:
            month = 'мая'
        elif month == 6:
            month = 'июня'
        elif month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'
        elif month == 9:
            month = 'сентября'
        elif month == 10:
            month = 'октября'
        elif month == 11:
            month = 'ноября'
        elif month == 12:
            month = 'декабря'
        day = poketime.day
        hour = poketime.hour
        if hour == 1:
            hour = '01'
        elif hour == 2:
            hour = '02'
        elif hour == 3:
            hour = '03'
        elif hour == 4:
            hour = '04'
        elif hour == 5:
            hour = '05'
        elif hour == 6:
            hour = '06'
        elif hour == 7:
            hour = '07'
        elif hour == 8:
            hour = '08'
        elif hour == 9:
            hour = '09'
        elif hour == 0:
            hour = '00'
        minute = poketime.minute
        if minute == 0:
            minute = '00'
        elif minute == 1:
            minute == '01'
        elif minute == 2:
            minute == '02'
        elif minute == 3:
            minute == '03'
        elif minute == 4:
            minute == '04'
        elif minute == 5:
            minute == '05'
        elif minute == 6:
            minute == '06'
        elif minute == 7:
            minute == '07'
        elif minute == 8:
            minute == '08'
        elif minute == 9:
            minute == '09'
        poketime = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

        color = random.choice([discord.Color.dark_blue(), discord.Color.dark_gold(), discord.Color.dark_green(), discord.Color.dark_grey(), discord.Color.dark_magenta(), discord.Color.dark_orange(), discord.Color.dark_purple(), discord.Color.dark_red(), discord.Color.dark_teal()])
            
        try:
            pokeinfo = discord.Embed(
                description = '__**Покемон:**__ ***{}***\n__**Даёт:**__ ***{}***\n__**Номер в покедексе:**__ ***{}***'.format(pokemon.title(), givingevs, number),
                color = color
            )
            pokeinfo.set_thumbnail(
                url = photo
            )
            pokeinfo.set_footer(
                text = 'Cпросил {} {}'.format(message.author, poketime),
                icon_url = message.author.avatar_url
            )
            pokeinfo.set_author(
                name = 'Pokemon Info:',
                icon_url = 'https://i.imgur.com/iQqhe6y.gif'
            )
            await message.channel.send(embed = pokeinfo)
        
        except:
            try:
                pokeinfo = discord.Embed(
                    description = '__**Характеристика:**__ ***{}***\n__**Дают:**__ ***{}***'.format(stat, gives),
                    color = color
                )
                pokeinfo.set_thumbnail(
                    url = 'https://media1.giphy.com/media/NS7gPxeumewkWDOIxi/giphy.gif?cid=790b76115cefcfce634a33554df6fcf5&rid=giphy.gif'
                )
                pokeinfo.set_footer(
                    text = 'Запросил {}    {}'.format(message.author, poketime),
                    icon_url = message.author.avatar_url
                )
                pokeinfo.set_author(
                    name = 'Pokemon Info:',
                    icon_url = 'https://i.imgur.com/iQqhe6y.gif'
                )
                await message.channel.send(embed = pokeinfo)
            except:
                print(Exception)


#0000000000  0000000000
#0   00   0  000
#    00      0000000
#    00      000
#    00      000
    if msglower.startswith('-topfact') or msglower.startswith('-tf'):
        colour = random.choice([0xff0000, 0xff8000, 0xffff00, 0x00ff00, 0x00ffff, 0x032ef8, 0x800080])
        topfact = random.choice([topfact1, topfact2, topfact3, topfact4, topfact5, topfact6])
        topemb=discord.Embed(
            title='"Топ" факт!:thinking::thumbsup::ok_hand:',
            description=topfact,
            color=colour
        )
        topemb.set_footer(
            text='Подтверждено kvakep\'ом ✔'
        )
        await message.delete()
        await message.channel.send(embed=topemb)

#0000000    000000  00   00
#000       00   00  00   00
#0000000  00000000   000000
#    000  00    00       00
#0000000  00    00   00000
    if msglower.startswith('-say'):
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
                await message.channel.send('Используйте: -say [message]', delete_after = 15)
                return

            semb = discord.Embed(
                description = msg[1],
                color = discord.Color.dark_teal()
            )
            await message.channel.send(embed = semb)

#00             00  000    000  0000  0000000  000000   00000000  0000000
# 00           00   000    000   00   000      000  00  0000      000   00
#  00   000   00    0000000000   00   0000000  000000   00000000  0000000
#   00 00 00 00     000    000   00       000  000      0000      000   00
#    000   000      000    000  0000  0000000  000      00000000  000    00
    if msglower.startswith('-whisper'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('>', '')
                member = member.replace('@', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -whisper [@member/member_id] [message]', delete_after = 15)
            
            try:
                for e in client.emojis:
                    if e.name in msg[2]:
                        try:
                            check = re.search(r'<:' + e.name + r':\d*>', msg[2])
                            check = check.group(0)
                            check = check[1:]
                        except:
                            msg[2] = msg.replace(':{}:'.format(e.name), str(e))
            except IndexError:
                await message.channel.send('Используйте: -whisper [@member/member_id] [message]', delete_after = 15)

            whisper = discord.Embed(
                description = msg[2],
                color = discord.Color.dark_orange()
            )

            await member.send(embed = whisper)

#  000000  00   00    000000
# 00   00  00   00   00   00
#00000000  00   00  00000000
#00    00   00 00   00    00
#00    00    000    00    00
    if msglower.startswith('-ava'):
        colour = random.choice([0xff0000, 0xff8000, 0xffff00, 0x00ff00, 0x00ffff, 0x032ef8, 0x800080])
        msg = message.content.split(' ')
        await message.delete()
        try:
            msg[1] = msg[1].replace('<', '')
            msg[1] = msg[1].replace('>', '')
            msg[1] = msg[1].replace('@', '')
            member = message.guild.get_member(int(msg[1]))
        except:
            await message.channel.send('Используйте: -ava [@member/member_id]', delete_after = 15)
            return

        img = member.avatar_url
        ava = discord.Embed(
            description = '***Аватар пользователя {0.name}***'.format(member),
            color = colour
        )
        ava.set_image(url = img)
        ava.set_footer(text = 'Requested by {}'.format(message.author),
            icon_url = 'https://i.imgur.com/Ojia4Ni.png'
        )
        await message.channel.send(embed = ava)

#000   000  0000   000000   000   000
#000  000    00   000    0  000  000
#0000000     00   000       0000000
#000  000    00   000    0  000  000
#000   000  0000   000000   000   000
    if msglower.startswith('-kick'):
        if message.author.guild_permissions.kick_members or message.author.id == 400231667408699392:
            await message.delete()
            try:
                msg = message.content.split(' ')

                try:
                    member = msg[1]
                    member = member.replace('', '')
                    member = member.replace('', '')
                    member = member.replace('', '')
                    member = int(member)
                    member = message.guild.get_member(member)
                except:
                    await message.channel.send('Используйте: -kick [@member/member_id] ([reason])', delete_after = 15)
                    return
                
                try:
                    reason = msg[2]
                except:
                    reason = ''
                
                kvakeplogs = discord.CategoryChannel
                overwrites = {
                    message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                    message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
                }
                for cat in message.guild.categories:
                    if cat.name == 'kvakep-logs':
                        kvakeplogs = cat
                        break
                else:
                    kvakeplogs = await message.guild.create_category_channel(
                        name = 'kvakep-logs',
                        overwrites = overwrites,
                        reason = 'Category for kvakep\'s logs'
                    )
                for chan in kvakeplogs.channels:
                    if chan.name == 'kicks':
                        kickslog = chan
                        break
                else:
                    kickslog = await kvakeplogs.create_text_channel(
                        name = 'kicks',
                        overwrites = overwrites,
                        reason = 'Channel for kvakep\'s kicks'
                    )

                if message.author.guild_permissions.administrator:
                    kickauthor = 'администратором'
                else:
                    kickauthor = 'модератором'

                timenow = datetime.datetime.today()
                year = timenow.year
                month = timenow.month
                if month == 1:
                    month = 'января'
                elif month == 2:
                    month = 'февраля'
                elif month == 3:
                    month = 'марта'
                elif month == 4:
                    month = 'апреля'
                elif month == 5:
                    month = 'мая'
                elif month == 6:
                    month = 'июня'
                elif month == 7:
                    month = 'июля'
                elif month == 8:
                    month = 'августа'
                elif month == 9:
                    month = 'сентября'
                elif month == 10:
                    month = 'октября'
                elif month == 11:
                    month = 'ноября'
                elif month == 12:
                    month = 'декабря'
                day = timenow.day
                hour = timenow.hour
                if hour == 1:
                    hour = '01'
                elif hour == 2:
                    hour = '02'
                elif hour == 3:
                    hour = '03'
                elif hour == 4:
                    hour = '04'
                elif hour == 5:
                    hour = '05'
                elif hour == 6:
                    hour = '06'
                elif hour == 7:
                    hour = '07'
                elif hour == 8:
                    hour = '08'
                elif hour == 9:
                    hour = '09'
                elif hour == 0:
                    hour = '00'
                minute = timenow.minute
                if minute == 0:
                    minute = '00'
                elif minute == 1:
                    minute == '01'
                elif minute == 2:
                    minute == '02'
                elif minute == 3:
                    minute == '03'
                elif minute == 4:
                    minute == '04'
                elif minute == 5:
                    minute == '05'
                elif minute == 6:
                    minute == '06'
                elif minute == 7:
                    minute == '07'
                elif minute == 8:
                    minute == '08'
                elif minute == 9:
                    minute == '09'
                timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

                if reason != '':
                    tologs = discord.Embed(
                        description = 'Пользователь {} был исключён {} {}.\nПричина: {}'.format(member, kickauthor, message.author, reason),
                        color = discord.Color.dark_grey()
                    )
                    tologs.set_footer(
                        text = timenow
                    )
                    tomember = discord.Embed(
                        description = 'Вы были исключены {} {}.\nПричина: {}'.format(kickauthor, message.author, reason)
                    )
                    await message.guild.kick(member, reason = 'Исключён: {} {}\nПричина: {}'.format(kickauthor, message.author, reason))
                else:
                    tologs = discord.Embed(
                        description = 'Пользователь {} был исключён {} {}.'.format(member, kickauthor, message.author),
                        color = discord.Color.dark_grey()
                    )
                    tologs.set_footer(
                        text = timenow
                    )
                    tomember = discord.Embed(
                        description = 'Вы были исключены {} {}.'.format(kickauthor, message.author)
                    )
                    await message.guild.kick(member, reason = 'Исключён: {} {}'.format(kickauthor, message.author))
                
                invitation = await message.channel.create_invite(max_uses = 1, reason = 'After kick')
                
                await message.channel.send('Пользователь {} был успешно исключён! :white_check_mark:'.format(member), delete_after = 15)
                await kickslog.send(embed = tologs)
                await member.send(content = invitation.url, embed = tomember)
            except:
                await message.channel.send('Вы не можете исключить данного пользователя!', delete_after = 15)
        else:
            await message.channel.send('У Вас недостаточно прав на выполнение данной команды!', delete_after = 15)

#000000   000    000  0000000     0000000000  00000000
#000  00  000    000  000   00   00        0  0000
#000000   000    000  0000000    00  00000    00000000
#000       000000000  000   00   00  00  00   0000
#000        00000000  000    00   000000000   00000000
    if msglower.startswith('-purge') or msglower.startswith('-clear'):
        if message.author.guild_permissions.manage_messages or message.author.id == 400231667408699392:
            param = message.content.split(' ', 2)
            quantity = int(param[1])
            await message.delete()
            if quantity <= 100:
                if len(param) < 2:
                    await message.channel.send('Искользуйте: -purge [количество сообщений(не более 100)]', delete_after = 15)
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

#0000000     0000000   000       00000000  0000000
#000   00   000   000  000       0000      000
#0000000    000   000  000       00000000  0000000
#000   00   000   000  0000      0000          000
#000    00   0000000   00000000  00000000  0000000
    if msglower.startswith('-roles'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            roles = message.guild.roles
            msg = ''
            for role in roles:
                msg += '{}\n'.format(role)
            await message.delete()
            await message.author.send('{}:\n{}'.format(message.guild, msg))

# 0000000000  000    000  0000  000       0000000   0000000
#00        0  000    000   00   000       000   00  000
#00  00000    000    000   00   000       000   00  0000000
#00  00  00    000000000   00   0000      000   00      000
# 000000000      0000000  0000  00000000  0000000   0000000
    if msglower.startswith('-guilds'):
        if message.author.id == 400231667408699392:
            await message.delete()
            guilds = client.guilds
            msg = ''
            for g in guilds:
                msg += '{}\n'.format(g)
            await message.author.send('Список серверов:\n{}'.format(msg))
        else:
            pass

# 0000000000      0000000     0000000   000       00000000  0000000
#00        0      000   00   000   000  000       0000      000
#00  00000        0000000    000   000  000       00000000  0000000
#00  00  00       000   00   000   000  0000      0000          000
# 000000000       000    00   0000000   00000000  00000000  0000000
    if msglower.startswith('-groles'):
        if message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ')
            try:
                guild = msg[1]
                guild = client.get_guild(int(guild))
            except IndexError:
                await  message.channel.send('Используйте: -groles [guild_id]', delete_after = 15)
            msg = ''
            roles = guild.roles
            for r in roles:
                msg += '{}\n'.format(r.name)
            await message.author.send('{}\n{}'.format(guild.name, msg))

#0000000  00000000  0000000    00   00  00000000  0000000        0000  00000    000  00000000000   0000000
#000      0000      000   00   00   00  0000      000   00        00   000 00   000  000          000   000
#0000000  00000000  0000000    00   00  00000000  0000000         00   000  00  000  00000000     000   000
#    000  0000      000   00    00 00   00000     000   00        00   000   00 000  000          000   000
#0000000  00000000  000    00    000    00000000  000    00      0000  000    00000  000           0000000
    if msglower.startswith('-serverinfo'):
        await message.delete()

        name = message.guild

        large = message.guild.member_count

        owner = message.guild.owner

        created = message.guild.created_at.date()
        year = created.year
        month = created.month
        if month == 1:
            month = 'января'
        elif month == 2:
            month = 'февраля'
        elif month == 3:
            month = 'марта'
        elif month == 4:
            month = 'апреля'
        elif month == 5:
            month = 'мая'
        elif month == 6:
            month = 'июня'
        elif month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'
        elif month == 9:
            month = 'сентября'
        elif month == 10:
            month = 'октября'
        elif month == 11:
            month = 'ноября'
        elif month == 12:
            month = 'декабря'
        day = created.day

        roles = len(message.guild.roles)

        icon = message.guild.icon_url

        text_channels = len(message.guild.text_channels)
        voice_channels = len(message.guild.voice_channels)
        channels = text_channels + voice_channels
        nsfw = 0
        news = 0
        for t in range(len(message.guild.text_channels)):
            if message.guild.text_channels[t].is_nsfw():
                nsfw += 1
            if message.guild.text_channels[t].is_news():
                news += 1

        emojis = len(message.guild.emojis)
        animated_emojis = 0
        for e in range(len(message.guild.emojis)):
            if message.guild.emojis[e].animated:
                animated_emojis += 1
        common_emojis = emojis - animated_emojis

        region = str(message.guild.region).title()

        verification = message.guild.verification_level
        if str(verification) == 'none':
            verification = 'Отсутствует'
        elif str(verification) == 'low':
            verification = 'Низкий'
        elif str(verification) == 'medium':
            verification  = 'Средний'
        elif str(verification) == 'high':
            verification = 'Высокий'
        elif str(verification) == 'extreme':
            verification = 'Высочайший'

        online_member = client.get_emoji(596453205341241355)
        idle_member = client.get_emoji(596453234227413031)
        dnd_member = client.get_emoji(596453249712652308)
        offline_member = client.get_emoji(596453263927279729)
        bot_member = client.get_emoji(596680939401117707)
        membersonguild = ''
        online = 0
        idle = 0
        dnd = 0
        offline = 0
        bot = 0
        for m in range(len(message.guild.members)):
            if message.guild.members[m].status == discord.Status.online:
                online += 1
            elif message.guild.members[m].status == discord.Status.idle:
                idle += 1
            elif message.guild.members[m].status == discord.Status.dnd:
                dnd += 1
            elif message.guild.members[m].status == discord.Status.offline:
                offline += 1
            if message.guild.members[m].bot:
                bot += 1

        info = discord.Embed(
            description = 'Информация о сервере: ',
            color = 0xfcb803
        )
        info.add_field(
            name = '**Название:**',
            value = name
        )
        info.add_field(
            name = '**Регион: **',
            value = region
        )
        info.add_field(
            name = '**Создатель: **',
            value = owner.mention
        )
        info.add_field(
            name = '**Создан: **',
            value = '{} {} {}'.format(day, month, year)
        )
        info.add_field(
            name = '**Каналов: **',
            value = 'Всего: {}\nТекстовых: {}\n  NSFW: {}\n  News: {}\nГолосовых: {}'.format(channels, text_channels, nsfw, news, voice_channels)
        )
        info.add_field(
            name = '**Участников: **',
            value = 'Всего: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}'.format(large, online_member, online, idle_member, idle, dnd_member, dnd, offline_member, offline, bot_member, bot)
        )
        info.add_field(
            name = '**Количество ролей: **',
            value = roles
        )
        info.add_field(
            name = '**Эмодзи: **',
            value = 'Всего: {}\nОбычных: {}\nАнимированных: {}'.format(emojis, common_emojis, animated_emojis)
        )
        info.add_field(
            name = '**Уровень проверки: **',
            value = verification
        )
        info.set_thumbnail(url = icon)
        await message.channel.send(embed = info)

#  000000  0000000   0000000       0000000    00000000    000000   000000
# 00   00  000   00  000   00      000   00   0000       00   00  000    0
#00000000  000   00  000   00      0000000    00000000  00000000  000
#00    00  000   00  000   00      000   00   0000      00    00  000    0
#00    00  0000000   0000000       000    00  00000000  00    00   000000
    if msglower.startswith('-addreac') and message.author.id == 400231667408699392:
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
            await message.channel.send('Используйте: -addreac [message_id] [reaction]', delete_after = 15)
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
            await message.channel.send('Используйте: -addreac [message_id] [reaction]', delete_after = 15)
            return

    if msglower.startswith('-removereac') and message.author.id == 400231667408699392:
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
            await message.channel.send('Используйте: -removereac [message_id] [reaction]', delete_after = 15)
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
            await message.channel.send('Используйте: -removereac [message_id] [reaction]', delete_after = 15)
            return

#0000000   00000000  000           0000000    00000000    000000   000000
#000   00  0000      000           000   00   0000       00   00  000    0
#000   00  00000000  000           0000000    00000000  00000000  000
#000   00  0000      0000          000   00   0000      00    00  000    0
#0000000   00000000  00000000      000    00  00000000  00    00   000000
    if msglower.startswith('-delreacts') and message.author.id == 400231667408699392:
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
            await message.channel.send('Используйте: -delreacts [message_id]', delete_after = 15)
            return

#0000000    00000000  0000000  00000000  00000    000  0000000
#000   00   0000      000      0000      000 00   000  000   00
#0000000    00000000  0000000  00000000  000  00  000  000   00
#000   00   0000          000  0000      000   00 000  000   00
#000    00  00000000  0000000  00000000  000    00000  0000000
    if msglower.startswith('-resend'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            mes = message.content.split(' ', 2)
            index = mes[1]
            await message.delete()
            if len(mes) < 2:
                await message.channel.send('Используйте: -resend [message_id] ([comment])', delete_after = 15)
            else:
                msg = discord.Message
                msghistory = await message.channel.history(limit = 1000).flatten()
                for m in range(len(msghistory)):
                    if int(index) == msghistory[m].id:
                        msg = msghistory[m]
                        break
                else:
                    await message.channel.send('Сообщение не найдено!', delete_after = 15)
                    return
                year = msg.created_at.year
                month = msg.created_at.month
                if month == 1:
                    month = 'января'
                elif month == 2:
                    month = 'февраля'
                elif month == 3:
                    month = 'марта'
                elif month == 4:
                    month = 'апреля'
                elif month == 5:
                    month = 'мая'
                elif month == 6:
                    month = 'июня'
                elif month == 7:
                    month = 'июля'
                elif month == 8:
                    month = 'августа'
                elif month == 9:
                    month = 'сентября'
                elif month == 10:
                    month = 'октября'
                elif month == 11:
                    month = 'ноября'
                elif month == 12:
                    month = 'декабря'
                day = msg.created_at.day
                hour = msg.created_at.hour + 3
                if hour > 23:
                    hour -= 24
                if hour == 0:
                    hour = '00'
                elif hour == 1:
                    hour = '01'
                elif hour == 2:
                    hour = '02'
                elif hour == 3:
                    hour = '03'
                elif hour == 4:
                    hour = '04'
                elif hour == 5:
                    hour = '05'
                elif hour == 6:
                    hour = '06'
                elif hour == 7:
                    hour = '07'
                elif hour == 8:
                    hour = '08'
                elif hour == 9:
                    hour = '09'
                minute = msg.created_at.minute
                if minute == 0:
                    minute = '00'
                elif minute == 1:
                    minute = '01'
                elif minute == 2:
                    minute = '02'
                elif minute == 3:
                    minute = '03'
                elif minute == 4:
                    minute = '04'
                elif minute == 5:
                    minute = '05'
                elif minute == 6:
                    minute = '06'
                elif minute == 7:
                    minute = '07'
                elif minute == 8:
                    minute = '08'
                elif minute == 9:
                    minute = '09'
                created = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)
                embed = message.embeds
                if len(embed) != 0:
                    embed = embed[0].copy()
                    await message.channel.send(content = '{}\n{}'.format(msg.author, created),embed = embed)
                else:
                    if len(mes) > 2:
                        resend = discord.Embed(
                            description = msg.content,
                            color = 0x800080
                        )
                        resend.set_author(
                            name = '{}        {}'.format(msg.author, created),
                            icon_url = msg.author.avatar_url,
                            url = msg.jump_url
                        )
                        await message.channel.send(embed = resend, content = mes[2])
                    else:
                        resend = discord.Embed(
                            description = msg.content,
                            color = 0x800080
                        )
                        resend.set_author(
                            name = '{}        {}'.format(msg.author, created),
                            icon_url = msg.author.avatar_url,
                            url = msg.jump_url
                        )
                        await message.channel.send(embed = resend)

#00000     00000  00   00      00000000  00000     00000   0000000
#000000   000000  00   00      0000      000000   000000  000   000
#000 000 000 000   000000      00000000  000 000 000 000  000   000
#000   000   000       00      0000      000   000   000  000   000
#000         000   00000       00000000  000         000   0000000
    if msglower.startswith('-myemo') and message.author.id == 400231667408699392:
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
                await message.channel.send('Используйте: -myemo ([all/count])', delete_after = 15)
        else:
            myemojismsg = await message.channel.send(embed = embedlist[0])
            await myemojismsg.add_reaction('◀')
            await myemojismsg.add_reaction('▶')

# 0000000000  0000  00    00  00000000      0000000     0000000   000       00000000
#00        0   00   00    00  0000          000   00   000   000  000       0000
#00  00000     00   00    00  00000000      0000000    000   000  000       00000000
#00  00  00    00    00  00   0000          000   00   000   000  0000      0000
# 000000000   0000    0000    00000000      000    00   0000000   00000000  00000000
    if msglower.startswith('-giverole'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 2)
            await message.delete()
            try:
                role = msg[2]
                role = role.replace('@', '')
                role = role.replace('&', '')
                role = role.replace('>', '')
                role = role.replace('<', '')
            except:
                await message.channel.send('Используйте: -giverole [@member/member_id] [@role/role_id]', delete_after = 15)
                return
            member = msg[1]
            member = member.replace('<', '')
            member = member.replace('>', '')
            member = member.replace('@', '')
            for r in range(len(message.guild.roles)):
                if role == str(message.guild.roles[r]):
                    role = message.guild.roles[r]
                    break
            else:
                for r in range(len(message.guild.roles)):
                    if int(role) == message.guild.roles[r].id:
                        role = message.guild.roles[r]
                        break
                else:
                    await message.channel.send('Роль не найдена!', delete_after = 15)
                    return
            try:
                member = message.guild.get_member(int(member))
                await member.add_roles(role, reason = message.content)
                await message.channel.send('Роль {} успешно добавлена пользователю {}!'.format(role, member), delete_after = 15)
            except:
                await message.channel.send('Пользователь не найден!', delete_after = 15)

#0000000   00000000  000           0000000     0000000   000       00000000
#000   00  0000      000           000   00   000   000  000       0000
#000   00  00000000  000           0000000    000   000  000       00000000
#000   00  0000      0000          000   00   000   000  0000      0000
#0000000   00000000  00000000      000    00   0000000   00000000  00000000
    if msglower.startswith('-delrole'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 2)
            await message.delete()
            try:
                role = msg[2]
                role = role.replace('@', '')
                role = role.replace('&', '')
                role = role.replace('>', '')
                role = role.replace('<', '')
            except:
                await message.channel.send('Используйте: -delrole [@member/member_id] [@role/role_id]', delete_after = 15)
                return
            member = msg[1]
            member = member.replace('<', '')
            member = member.replace('>', '')
            member = member.replace('@', '')
            for r in range(len(message.guild.roles)):
                if role == str(message.guild.roles[r]):
                    role = message.guild.roles[r]
                    break
            else:
                await message.channel.send('Роль не найдена!', delete_after = 15)
                return
            try:
                member = message.guild.get_member(int(member))
                await member.remove_roles(role, reason = message.content)
                await message.channel.send('Роль {} успешно снята с пользователя {}!'.format(role, memberid), delete_after = 15)
            except:
                await message.channel.send('Пользователь не найден!', delete_after = 15)

#000000   00000000  0000000    00000     00000  0000000
#000  00  0000      000   00   000000   000000  000
#00000    00000000  0000000    000 000 000 000  0000000
#000      0000      000   00   000   000   000      000
#000      00000000  000    00  000         000  0000000
    if msglower.startswith('-perms') and message.author.id == 400231667408699392:
        msg = message.content.split(' ')
        await message.delete()
        member = message.guild.get_member(int(msg[1]))
        perms = []
        perms.append(member)
        if member.guild_permissions.administrator:
            perms.append('administrator')
            msg = 'administrator'
        else:
            if member.guild_permissions.create_instant_invite:
                perms.append('create_instant_invite')
            if member.guild_permissions.kick_members:
                perms.append('kick_members')
            if member.guild_permissions.ban_members:
                perms.append('ban_members')
            if member.guild_permissions.manage_channels:
                perms.append('manage_channels')
            if member.guild_permissions.manage_guild:
                perms.append('manage_guild')
            if member.guild_permissions.add_reactions:
                perms.append('add_reactions')
            if member.guild_permissions.view_audit_log:
                perms.append('view_audit_log')
            if member.guild_permissions.priority_speaker:
                perms.append('priority_speaker')
            if member.guild_permissions.stream:
                perms.append('stream')
            if member.guild_permissions.read_messages:
                perms.append('read_messages')
            if member.guild_permissions.send_messages:
                perms.append('send_messages')
            if member.guild_permissions.send_tts_messages:
                perms.append('send_tts_messages')
            if member.guild_permissions.manage_messages:
                perms.append('manage_messages')
            if member.guild_permissions.embed_links:
                perms.append('embed_links')
            if member.guild_permissions.attach_files:
                perms.append('attach_files')
            if member.guild_permissions.read_message_history:
                perms.append('read_message_history')
            if member.guild_permissions.mention_everyone:
                perms.append('mention_everyone')
            if member.guild_permissions.external_emojis:
                perms.append('external_emojis')
            if member.guild_permissions.connect:
                perms.append('connect')
            if member.guild_permissions.speak:
                perms.append('speak')
            if member.guild_permissions.mute_members:
                perms.append('mute_members')
            if member.guild_permissions.deafen_members:
                perms.append('deafen_members')
            if member.guild_permissions.move_members:
                perms.append('move_members')
            if member.guild_permissions.use_voice_activation:
                perms.append('use_voice_activation')
            if member.guild_permissions.change_nickname:
                perms.append('change_nickname')
            if member.guild_permissions.manage_nicknames:
                perms.append('manage_nicknames')
            if member.guild_permissions.manage_roles:
                perms.append('manage_roles')
            if member.guild_permissions.manage_webhooks:
                perms.append('manage_webhooks')
            if member.guild_permissions.manage_emojis:
                perms.append('manage_emojis')
            msg = ''
            for i in range(1, len(perms)):
                msg += '{}\n'.format(perms[i])
        permissions = discord.Embed(
            title = '{}\'s perms:'.format(member),
            description = msg,
            color = discord.Color.dark_magenta()
        )
        await message.channel.send(embed = permissions, delete_after = 120)

#00             00  0000000    0000  0000000000  00000000        000000  0000000
# 00           00   000   00    00   0   00   0  0000           00   00  000
#  00   000   00    0000000     00       00      00000000      00000000  0000000
#   00 00 00 00     000   00    00       00      0000          00    00      000
#    000   000      000    00  0000      00      00000000      00    00  0000000
    if msglower.startswith('-writeas') and message.author.id == 400231667408699392:
        msg = message.content.split(' ', 2)
        await message.delete()
        webhooks = await message.channel.webhooks()
        try:
            web = webhooks[0]
            webid = web.id
            webtoken = web.token
        except:
            try:
                web = await message.channel.create_webhook(name = 'kvakep', avatar = message.guild.me.avatar_url)
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

#000000   0000  00000    000   0000000000
#000  00   00   000 00   000  00        0
#000000    00   000  00  000  00  00000
#000       00   000   00 000  00  00  00
#000      0000  000    00000   000000000
    if msglower.startswith('-ping'):
        await message.delete()
        msg = await message.channel.send('Считаю...')
        ping = int((msg.created_at.microsecond - message.created_at.microsecond) / 10000)
        pingemoji = client.get_emoji(596025886537678869)
        await msg.edit(content = 'Задержка: **{}** ms! {}'.format(ping, pingemoji), delete_after = 15)

#00000     00000  000    000  0000000000  00000000
#000000   000000  000    000  0   00   0  0000
#000 000 000 000  000    000      00      00000000
#000   000   000   000000000      00      0000
#000         000     0000000      00      00000000
    if msglower.startswith('-mute'):
        if message.author.guild_permissions.mute_members or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 3)
            await message.delete()

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('>', '')
                member = member.replace('@', '')
                member = int(member)
                member = message.guild.get_member(member)
            except:
                await message.channel.send('Используйте: -mute [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            try:
                time = msg[2]
                days = re.search(r'\d{1,2}d', time)
                hours = re.search(r'\d{1,2}h', time)
                minutes = re.search(r'\d{1,2}m', time)
                seconds = re.search(r'\d{1,2}s', time)
                try:
                    days = days.group(0)
                    days = days.replace('d', '')
                    days = int(days)
                except:
                    days = 0
                try:
                    hours = hours.group(0)
                    hours = hours.replace('h', '')
                    hours = int(hours)
                except:
                    hours = 0
                try:
                    minutes = minutes.group(0)
                    minutes = minutes.replace('m', '')
                    minutes = int(minutes)
                except:
                    minutes = 0
                try:
                    seconds = seconds.group(0)
                    seconds = seconds.replace('s', '')
                    seconds = int(seconds)
                except:
                    seconds = 0
                time = datetime.datetime.now() + datetime.timedelta(days = days, hours = hours, minutes = minutes, seconds  = seconds)
                msgtime = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', str(time))
                msgtime = msgtime.group(0)
            except:
                await message.channel.send('Используйте: -mute [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            silence = client.get_emoji(597389163096178688)
            panic = client.get_emoji(594496061989584897)

            try:
                reason = msg[3]
            except:
                reason = ''

            muteauthor = ''
            if message.author.guild_permissions.administrator:
                muteauthor = 'администратором'
            else:
                muteauthor = 'модератором'

            muted = open('kvakepmutedmembers.txt', 'r')
            lines = muted.readlines()
            muted.close()
            for l in range(len(lines)):
                if 'Пользователь: {}'.format(member.id) in lines[l]:
                    lines[l] = 'Сервер: {}; Пользователь: {}; Время: {}; Замучен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason)
                    m = open('kvakepmutedmembers.txt', 'w')
                    m.writelines(lines)
                    m.close()
                    break
            else:
                muted = open('kvakepmutedmembers.txt', 'a')
                muted.write('Сервер: {}; Пользователь: {}; Время: {}; Замучен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason))
                muted.close()

            muterole = discord.Role
            for r in message.guild.roles:
                if int(r.permissions.value) == 1049600:
                    muterole = r
                    break
            else:
                muterole = await message.guild.create_role(
                    name = 'Muted',
                    permissions = discord.Permissions(permissions = 1049600),
                    color = discord.Color.dark_grey(),
                    reason = 'Роль для мутов'
                )

            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
            }
            for cat in message.guild.categories:
                if cat.name == 'kvakep-logs':
                    kvakeplogs = cat
                    break
            else:
                kvakeplogs = await message.guild.create_category_channel(
                    name = 'kvakep-logs',
                    overwrites = overwrites,
                    reason = 'Category for kvakep\'s logs'
                )
            for chan in kvakeplogs.channels:
                if chan.name == 'mutes':
                    muteslog = chan
                    break
            else:
                muteslog = await kvakeplogs.create_text_channel(
                    name = 'mutes',
                    overwrites = overwrites,
                    reason = 'Channel for kvakep\'s mutes'
                )

            timenow = datetime.datetime.today()
            year = timenow.year
            month = timenow.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            day = timenow.day
            hour = timenow.hour
            if hour == 1:
                hour = '01'
            elif hour == 2:
                hour = '02'
            elif hour == 3:
                hour = '03'
            elif hour == 4:
                hour = '04'
            elif hour == 5:
                hour = '05'
            elif hour == 6:
                hour = '06'
            elif hour == 7:
                hour = '07'
            elif hour == 8:
                hour = '08'
            elif hour == 9:
                hour = '09'
            elif hour == 0:
                hour = '00'
            minute = timenow.minute
            if minute == 0:
                minute = '00'
            elif minute == 1:
                minute == '01'
            elif minute == 2:
                minute == '02'
            elif minute == 3:
                minute == '03'
            elif minute == 4:
                minute == '04'
            elif minute == 5:
                minute == '05'
            elif minute == 6:
                minute == '06'
            elif minute == 7:
                minute == '07'
            elif minute == 8:
                minute == '08'
            elif minute == 9:
                minute == '09'
            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

            if reason != '':
                tomember = discord.Embed(
                    description = 'Вы были заглушены {} {} до {}.\nПричина: {}\n{}'.format(muteauthor, message.author, msgtime, reason, panic),
                    color = discord.Color.dark_red()
                )
                tomember.set_footer(
                    text = timenow
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был заглушён {} {} до {}.\nПричина: {}\n{}'.format(member.mention, muteauthor, message.author.mention, msgtime, reason, silence),
                    color = discord.Color.dark_grey()
                )
                tolog.set_footer(
                    text = timenow
                )
                await member.addroles(muterole, reason = 'Заглушён {} {}\nПричина: {}'.format(muteauthor, message.author, reason))
            else:
                tomember = discord.Embed(
                    description = 'Вы были заглушены {} {} до {}.\n{}'.format(muteauthor, message.author, msgtime, panic),
                    color = discord.Color.dark_red()
                )
                tomember.set_footer(
                    text = timenow
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был заглушён {} {} до {}.\n{}'.format(member.mention, muteauthor, message.author.mention, msgtime, silence),
                    color = discord.Color.dark_grey()
                )
                tolog.set_footer(
                    text = timenow
                )
                await member.add_roles(muterole, reason = 'Заглушён {} {}'.format(muteauthor, message.author))
            
            await muteslog.send(embed = tolog)
            await member.send(embed = tomember)
        else:
            await message.channel.send('У Вас недостаточно прав на выполнение данной команды!', delete_after = 15)

#000    000  00000    000  00000     00000  000    000  0000000000  00000000
#000    000  000 00   000  000000   000000  000    000  0   00   0  0000
#000    000  000  00  000  000 000 000 000  000    000      00      00000000
# 000000000  000   00 000  000   000   000   000000000      00      0000
#   0000000  000    00000  000         000     0000000      00      00000000
    if msglower.startswith('-unmute'):
        await message.delete()
        if message.author.guild_permissions.mute_members:
            msg = message.content.split(' ', 2)

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member  = message.guild.get_member(int(member))
            except:
                await message.channel.send('Используйте: -unmute [@member/member/id] ([reason])', delete_after = 15)
                return
            
            try:
                reason = msg[2]
            except:
                reason = ''
            
            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
            }
            for cat in message.guild.categories:
                if cat.name == 'kvakep-logs':
                    kvakeplogs = cat
                    break
            else:
                kvakeplogs = await message.guild.create_category_channel(
                    name = 'kvakep-logs',
                    overwrites = overwrites,
                    reason = 'Category for kvakep\'s logs'
                )
            for chan in kvakeplogs.channels:
                if chan.name == 'mutes':
                    muteslog = chan
                    break
            else:
                muteslog = await kvakeplogs.create_text_channel(
                    name = 'mutes',
                    overwrites = overwrites,
                    reason = 'Channel for kvakep\'s mutes'
                )

            muterole = discord.Role
            for r in message.guild.roles:
                if int(r.permissions.value) == 1049600:
                    muterole = r
                    break
            else:
                muterole = await message.guild.create_role(
                    name = 'Muted',
                    permissions = discord.Permissions(permissions = 1049600),
                    color = discord.Color.dark_grey(),
                    reason = 'Роль для мутов'
                )
            
            muted = open('kvakepmutedmembers.txt', 'r')
            lines = muted.readlines()
            muted.close()
            for l in range(len(lines)):
                if 'Пользователь: {}'.format(member.id) in lines[l]:
                    del lines[l]
                    m = open('kvakepmutedmembers.txt', 'w')
                    m.writelines(lines)
                    m.close()
                    break
            else:
                await message.channel.send('Не найдено!', delete_after = 15)
                return
            
            unmuteauthor = ''
            if message.author.guild_permissions.administrator:
                unmuteauthor = 'администратором'
            else:
                unmuteauthor = 'модератором'

            timenow = datetime.datetime.today()
            year = timenow.year
            month = timenow.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            day = timenow.day
            hour = timenow.hour
            if hour == 1:
                hour = '01'
            elif hour == 2:
                hour = '02'
            elif hour == 3:
                hour = '03'
            elif hour == 4:
                hour = '04'
            elif hour == 5:
                hour = '05'
            elif hour == 6:
                hour = '06'
            elif hour == 7:
                hour = '07'
            elif hour == 8:
                hour = '08'
            elif hour == 9:
                hour = '09'
            elif hour == 0:
                hour = '00'
            minute = timenow.minute
            if minute == 0:
                minute = '00'
            elif minute == 1:
                minute == '01'
            elif minute == 2:
                minute == '02'
            elif minute == 3:
                minute == '03'
            elif minute == 4:
                minute == '04'
            elif minute == 5:
                minute == '05'
            elif minute == 6:
                minute == '06'
            elif minute == 7:
                minute == '07'
            elif minute == 8:
                minute == '08'
            elif minute == 9:
                minute == '09'
            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

            funnydogemoji = client.get_emoji(596690644467187723)
            if reason != '':
                tolog = discord.Embed(
                    description = 'С пользователя {} был снят мут {} {}\nПричина: {}'.format(member.mention, unmuteauthor, message.author.mention, reason),
                    color = discord.Color.dark_blue()
                )
                tolog.set_footer(
                    text = timenow
                )
                tomember = discord.Embed(
                    description = 'С Вас был снят мут {} {}\nПричина: {}\n{}'.format(unmuteauthor, message.author, reason, funnydogemoji),
                    color = discord.Color.dark_green()
                )
                tomember.set_footer(
                    text = timenow
                )
                await member.remove_roles(muterole, reason = 'Мут снят {} {}\nПричина: {}'.format(unmuteauthor, message.author, reason))
            else:
                tolog = discord.Embed(
                    description = 'С пользователя {} был снят мут {} {}'.format(member.mention, unmuteauthor, message.author.mention),
                    color = discord.Color.dark_blue()
                )
                tolog.set_footer(
                    text = timenow
                )
                tomember = discord.Embed(
                    description = 'С Вас был снят мут {} {}\n {}'.format(unmuteauthor, message.author, funnydogemoji),
                    color = discord.Color.dark_green()
                )
                tomember.setfooter(
                    text = timenow
                )
                await member.remove_roles(muterole, reason = 'Мут снят {} {}'.format(unmuteauthor, message.author))
            
            await muteslog.send(embed = tolog)
            await message.channel.send('С пользователя {} успешно снят мут! :white_check_mark:'.format(member), delete_after = 15)
            await member.send(embed = tomember)
        else:
            await message.channel.send('У Вас недостаточно прав на выполнение данной команды!', delete_after = 15)

#000000     000000  00000    000
#000  00   00   00  000 00   000
#000000   00000000  000  00  000
#000  00  00    00  000   00 000
#000000   00    00  000    00000
    if msglower.startswith('-ban'):
        if message.author.guild_permissions.kick_members or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 3)
            await message.delete()

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('>', '')
                member = member.replace('@', '')
                member = int(member)
                member = message.guild.get_member(member)
            except:
                await message.channel.send('Используйте: -ban [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            try:
                time = msg[2]
                days = re.search(r'\d{1,2}d', time)
                hours = re.search(r'\d{1,2}h', time)
                minutes = re.search(r'\d{1,2}m', time)
                seconds = re.search(r'\d{1,2}s', time)
                try:
                    days = days.group(0)
                    days = days.replace('d', '')
                    days = int(days)
                except:
                    days = 0
                try:
                    hours = hours.group(0)
                    hours = hours.replace('h', '')
                    hours = int(hours)
                except:
                    hours = 0
                try:
                    minutes = minutes.group(0)
                    minutes = minutes.replace('m', '')
                    minutes = int(minutes)
                except:
                    minutes = 0
                try:
                    seconds = seconds.group(0)
                    seconds = seconds.replace('s', '')
                    seconds = int(seconds)
                except:
                    seconds = 0
                time = datetime.datetime.now() + datetime.timedelta(days = days, hours = hours, minutes = minutes, seconds  = seconds)
                msgtime = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', str(time))
                msgtime = msgtime.group(0)
            except:
                await message.channel.send('Используйте: -ban [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            banhammer = client.get_emoji(597496822474342547)
            panic = client.get_emoji(594496061989584897)

            try:
                reason = msg[3]
            except:
                reason = ''

            banauthor = ''
            if message.author.guild_permissions.administrator:
                banauthor = 'администратором'
            else:
                banauthor = 'модератором'

            banned = open('kvakepbannedmembers.txt', 'r')
            lines = banned.readlines()
            banned.close()
            for l in range(len(lines)):
                if 'Пользователь: {}'.format(member.id) in lines[l]:
                    lines[l] = 'Сервер: {}; Пользователь: {}; Время: {}; Забанен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason)
                    m = open('kvakepbannedmembers.txt', 'w')
                    m.writelines(lines)
                    m.close()
                    break
            else:
                banned = open('kvakepbannedmembers.txt', 'a')
                banned.write('Сервер: {}; Пользователь: {}; Время: {}; Забанен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason))
                banned.close()

            banrole = discord.Role
            for r in message.guild.roles:
                if int(r.permissions.value) == 512:
                    banrole = r
                    break
            else:
                banrole = await message.guild.create_role(
                    name = 'Banned',
                    permissions = discord.Permissions(permissions = 512),
                    color = discord.Color.dark_grey(),
                    reason = 'Роль для банов'
                )

            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
            }
            for cat in message.guild.categories:
                if cat.name == 'kvakep-logs':
                    kvakeplogs = cat
                    break
            else:
                kvakeplogs = await message.guild.create_category_channel(
                    name = 'kvakep-logs',
                    overwrites = overwrites,
                    reason = 'Category for kvakep\'s logs'
                )
            for chan in kvakeplogs.channels:
                if chan.name == 'bans':
                    banslog = chan
                    break
            else:
                banslog = await kvakeplogs.create_text_channel(
                    name = 'bans',
                    overwrites = overwrites,
                    reason = 'Channel for kvakep\'s bans'
                )

            timenow = datetime.datetime.today()
            year = timenow.year
            month = timenow.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            day = timenow.day
            hour = timenow.hour
            if hour == 1:
                hour = '01'
            elif hour == 2:
                hour = '02'
            elif hour == 3:
                hour = '03'
            elif hour == 4:
                hour = '04'
            elif hour == 5:
                hour = '05'
            elif hour == 6:
                hour = '06'
            elif hour == 7:
                hour = '07'
            elif hour == 8:
                hour = '08'
            elif hour == 9:
                hour = '09'
            elif hour == 0:
                hour = '00'
            minute = timenow.minute
            if minute == 0:
                minute = '00'
            elif minute == 1:
                minute == '01'
            elif minute == 2:
                minute == '02'
            elif minute == 3:
                minute == '03'
            elif minute == 4:
                minute == '04'
            elif minute == 5:
                minute == '05'
            elif minute == 6:
                minute == '06'
            elif minute == 7:
                minute == '07'
            elif minute == 8:
                minute == '08'
            elif minute == 9:
                minute == '09'
            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

            if reason != '':
                tomember = discord.Embed(
                    description = 'Вы были забанены {} {} до {}.\nПричина: {}\n{}'.format(banauthor, message.author, msgtime, reason, panic),
                    color = discord.Color.dark_red()
                )
                tomember.set_footer(
                    text = timenow
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был забанен {} {} до {}.\nПричина: {}\n{}'.format(member.mention, banauthor, message.author.mention, msgtime, reason, banhammer),
                    color = discord.Color.dark_grey()
                )
                tolog.set_footer(
                    text = timenow
                )
                await member.add_roles(banrole, reason = 'Забанен {} {}\nПричина: {}'.format(banauthor, message.author, reason))
            else:
                tomember = discord.Embed(
                    description = 'Вы были забанены {} {} до {}.\n{}'.format(banauthor, message.author, msgtime, panic),
                    color = discord.Color.dark_red()
                )
                tomember.set_footer(
                    text = timenow
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был забанен {} {} до {}.\n{}'.format(member.mention, banauthor, message.author.mention, msgtime, banhammer),
                    color = discord.Color.dark_grey()
                )
                tolog.set_footer(
                    text = timenow
                )
                await member.add_roles(banrole, reason = 'Забанен {} {}'.format(banauthor, message.author))
            
            await message.channel.send('Пользователь {} был успешно забанен! :white_check_mark:'.format(member), delete_after = 15)
            await banslog.send(embed = tolog)
            await member.send(embed = tomember)
        else:
            await message.channel.send('У Вас недостаточно прав на выполнение данной команды!', delete_after = 15)

#000    000  00000    000  000000     000000  00000    000
#000    000  000 00   000  000  00   00   00  000 00   000
#000    000  000  00  000  000000   00000000  000  00  000
# 000000000  000   00 000  000  00  00    00  000   00 000
#   0000000  000    00000  000000   00    00  000    00000
    if msglower.startswith('-unban'):
        await message.delete()
        if message.author.guild_permissions.kick_members:
            msg = message.content.split(' ', 2)

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member  = message.guild.get_member(int(member))
            except:
                await message.channel.send('Используйте: -unban [@member/member/id] ([reason])', delete_after = 15)
                return
            
            try:
                reason = msg[2]
            except:
                reason = ''
            
            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
            }
            for cat in message.guild.categories:
                if cat.name == 'kvakep-logs':
                    kvakeplogs = cat
                    break
            else:
                kvakeplogs = await message.guild.create_category_channel(
                    name = 'kvakep-logs',
                    overwrites = overwrites,
                    reason = 'Category for kvakep\'s logs'
                )
            for chan in kvakeplogs.channels:
                if chan.name == 'bans':
                    banslog = chan
                    break
            else:
                banslog = await kvakeplogs.create_text_channel(
                    name = 'bans',
                    overwrites = overwrites,
                    reason = 'Channel for kvakep\'s bans'
                )

            banrole = discord.Role
            for r in message.guild.roles:
                if int(r.permissions.value) == 512:
                    banrole = r
                    break
            else:
                banrole = await message.guild.create_role(
                    name = 'Banned',
                    permissions = discord.Permissions(permissions = 512),
                    color = discord.Color.dark_grey(),
                    reason = 'Роль для банов'
                )
            
            banned = open('kvakepbannedmembers.txt', 'r')
            lines = banned.readlines()
            banned.close()
            for l in range(len(lines)):
                if 'Пользователь: {}'.format(member.id) in lines[l]:
                    del lines[l]
                    m = open('kvakepbannedmembers.txt', 'w')
                    m.writelines(lines)
                    m.close()
                    break
            else:
                await message.channel.send('Не найдено!', delete_after = 15)
                return
            
            unbanauthor = ''
            if message.author.guild_permissions.administrator:
                unbanauthor = 'администратором'
            else:
                unbanauthor = 'модератором'

            timenow = datetime.datetime.today()
            year = timenow.year
            month = timenow.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            day = timenow.day
            hour = timenow.hour
            if hour == 1:
                hour = '01'
            elif hour == 2:
                hour = '02'
            elif hour == 3:
                hour = '03'
            elif hour == 4:
                hour = '04'
            elif hour == 5:
                hour = '05'
            elif hour == 6:
                hour = '06'
            elif hour == 7:
                hour = '07'
            elif hour == 8:
                hour = '08'
            elif hour == 9:
                hour = '09'
            elif hour == 0:
                hour = '00'
            minute = timenow.minute
            if minute == 0:
                minute = '00'
            elif minute == 1:
                minute == '01'
            elif minute == 2:
                minute == '02'
            elif minute == 3:
                minute == '03'
            elif minute == 4:
                minute == '04'
            elif minute == 5:
                minute == '05'
            elif minute == 6:
                minute == '06'
            elif minute == 7:
                minute == '07'
            elif minute == 8:
                minute == '08'
            elif minute == 9:
                minute == '09'
            timenow = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)

            funnydogemoji = client.get_emoji(596690644467187723)
            if reason != '':
                tolog = discord.Embed(
                    description = 'С пользователя {} был снят бан {} {}\nПричина: {}'.format(member.mention, unbanauthor, message.author.mention, reason),
                    color = discord.Color.dark_blue()
                )
                tolog.set_footer(
                    text = timenow
                )
                tomember = discord.Embed(
                    description = 'С Вас был снят бан {} {}\nПричина: {}\n{}'.format(unbanauthor, message.author, reason, funnydogemoji),
                    color = discord.Color.dark_green()
                )
                tomember.set_ffoter(
                    text = timenow
                )
                await member.remove_roles(banrole, reason = 'Бан снят {} {}\nПричина: {}'.format(unbanauthor, message.author, reason))
            else:
                tolog = discord.Embed(
                    description = 'С пользователя {} был снят бан {} {}'.format(member.mention, unbanauthor, message.author.mention),
                    color = discord.Color.dark_blue()
                )
                tolog.set_footer(
                    text = timenow
                )
                tomember = discord.Embed(
                    description = 'С Вас был снят бан {} {}\n {}'.format(unbanauthor, message.author, funnydogemoji),
                    color = discord.Color.dark_green()
                )
                tomember.set_footer(
                    text = timenow
                )
                await member.remove_roles(banrole, reason = 'Бан снят {} {}'.format(unbanauthor, message.author))
            
            await banslog.send(embed = tolog)
            await message.channel.send('С пользователя {} успешно снят бан! :white_check_mark:'.format(member), delete_after = 15)
            await member.send(embed = tomember)
        else:
            await message.channel.send('У Вас недостаточно прав на выполнение данной команды!', delete_after = 15)

# 000000   000         000000  00000    000  0000000
#000    0  000        00   00  000 00   000  000
#000       000       00000000  000  00  000  0000000
#000    0  0000      00    00  000   00 000      000
# 000000   00000000  00    00  000    00000  0000000
    if msglower.startswith('-clan'):

        if msglower.startswith('-clan create'):
            await message.delete()
            msg = message.content.split(' ', 3)

            try:
                clancolor = msg[2]
                clancolor = colormap.hex2rgb(clancolor)
            except IndexError:
                await message.channel.send('Используйте: -clan create [#цвет(hex)] [название]', delete_after = 15)
                return
            except ValueError:
                await message.channel.send('Неизвестный цвет. Используйте hex код (#123abc)!', delete_after = 15)
                return
            try:
                clanname = msg[3]
            except IndexError:
                await message.channel.send('Используйте: -clan create [#цвет(hex)] [название]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    await message.channel.send('Вы уже состоите в клане!', delete_after = 15)
                    return

            for r in message.guild.roles:
                if r.name[7:].lower() == clanname.lower():
                    await message.channel.send('Такой клан уже создан! Используйте другой тэг!', delete_after = 15)
                    return

            for r in message.guild.roles:
                if r.name == '[Кланы] Leader':
                    leaderrole = r
                    break
            else:
                leaderrole = await message.guild.create_role(name = '[Кланы] Leader', color = discord.Color.default())
            
            pos = leaderrole.position

            try:
                clanrole = await message.guild.create_role(name = '[Клан] {}'.format(clanname), color = discord.Color.from_rgb(clancolor[0], clancolor[1], clancolor[2]), mentionable = True, hoist = True)
            except:
                await message.channel.send('Неизвестный цвет!', delete_after = 15)
                return

            await clanrole.edit(position = pos)

            perms = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False, send_messages = False, connect = False),
                clanrole: discord.PermissionOverwrite(read_messages = True, send_messages = True, speak = True, connect = True)
            }

            clapping = client.get_emoji(596690598023528449)
            createembed = discord.Embed(
                title = 'ClanInfo: ',
                description = 'Клан создан!\n{}'.format(clapping),
                color = clanrole.color
            )
            for c in message.guild.categories:
                if c.name == '[Кланы]':
                    cat = c
                    clantext = await cat.create_text_channel(name = clanname, overwrites = perms)
                    await cat.create_voice_channel(name = clanname, overwrites = perms)
                    await clantext.send(clanrole.mention)
                    await clantext.send(embed = createembed)
                    break
            else:
                cat = await message.guild.create_category_channel(name = '[Кланы]')
                clantext = await cat.create_text_channel(name = clanname, overwrites = perms)
                await cat.create_voice_channel(name = clanname, overwrites = perms)
                await clantext.send(clanrole.mention)
                await clantext.send(embed = createembed)
                

            await message.author.add_roles(clanrole)
            await message.author.add_roles(leaderrole)

        elif msglower.startswith('-clan invite'):
            await message.delete()
            msg = message.content.split(' ', 2)
            try:
                member = msg[2]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -clan invite [@member/member_id]', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader' or r.name == '[Кланы] Officer':
                    break
            else:
                await message.channel.send('У Вас недостаточно прав!', delete_after = 15)
                return

            for r in member.roles:
                if '[Клан] ' in r.name:
                    await message.channel.send('Пользователь уже состоит в клане!', delete_after = 15)
                    return
            
            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanname = r.name[7:]
                    clanrole = r
                    clancolor = r.color
                    break
            else:
                await  message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return
            
            invitationletter = discord.Embed(
                title = 'ClanInfo: ',
                description = 'Пользователь {} пригласил Вас в клан {}.\nЧтобы принять приглашение, нажмите :thumbsup:, если же хотите отклонить его, нажмите :thumbsdown:'.format(message.author, clanname),
                color = clancolor
            )

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            funnyblock = client.get_emoji(596690597092524033)
            inviteembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} пригласил в клан {}!\n{}'.format(message.author.mention, member.mention, funnyblock),
                color = clanrole.color
            )

            for t in message.guild.text_channels:
                if t.name == textname:
                    await t.send(embed = inviteembed)
                    break

            invitation = await member.send(embed = invitationletter)
            await invitation.add_reaction('👍')
            await invitation.add_reaction('👎')

            invites = open('claninvites.txt', 'a')
            invites.write('Guild: {}; Author: {}; Clan: {}; Member: {}; MessageId: {}; ChannelId: {}\n'.format(message.guild.id, message.author.id, clanrole.id, member.id, invitation.id, invitation.channel.id))
            invites.close()

        elif msglower.startswith('-clan promote'):
            await message.delete()
            msg = message.content.split(' ', 2)
            
            try:
                member = msg[2]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -clan promote [@member/member_id]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан]' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('У Вас нет клана!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name ==  '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            for r in message.guild.roles:
                if r.name == '[Кланы] Officer':
                    officerrole = r
                    break
            else:
                officerrole = await message.guild.create_role(name = '[Кланы] Officer')

            for r in member.roles:
                if r == clanrole:
                    await member.add_roles(officerrole)
                    break
            else:
                await message.channel.send('Пользователь не состоит в Вашем клане!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            dog = client.get_emoji(596690644467187723)
            promoteembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} назначил {} на должность офицера клана!\n{}'.format(message.author.mention, member.mention, dog),
                color = clanrole.color
            )

            tomember = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} назначил Вас на должность офицера клана {}!\n{}'.format(message.author, clanname, dog),
                color = clanrole.color
            )

            for t in message.guild.text_channels:
                if t.name == textname:
                    await t.send(embed = promoteembed)
                    break

            await member.send(embed = tomember)

        elif msglower.startswith('-clan demote'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                member = msg[2]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -clan demote [@member/member_id]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан]' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            for r in message.guild.roles:
                if r.name == '[Кланы] Officer':
                    officerrole = r
                    break
            else:
                officerrole = await message.guild.create_role(name = '[Кланы] Officer')

            for r in member.roles:
                if r.name == '[Кланы] Leader':
                    await message.channel.send('Пользователь является лидером клана!', delete_after = 15)
                    return

            for r in member.roles:
                if r == officerrole:
                    break
            else:
                await message.channel.send('Пользователь не является офицером клана!', delete_after = 15)
                return

            for r in member.roles:
                if r == clanrole:
                    await member.remove_roles(officerrole)
                    break
            else:
                await message.channel.send('Пользователь не состоит в Вашем клане!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            fingerwave = client.get_emoji(596697124654022668)
            demoteembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} снял {} с должности офицера клана!\n{}'.format(message.author.mention, member.mention, fingerwave),
                color = clanrole.color
            )

            tomember = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} снял Вас с должности офицера клана {}!\n{}'.format(message.author, clanname, fingerwave),
                color = clanrole.color
            )

            for t in message.guild.text_channels:
                if t.name == textname:
                    await t.send(embed = demoteembed)
                    break

            await member.send(embed = tomember)

        elif msglower.startswith('-clan kick'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                member = msg[2]
                member = member.replace('>', '')
                member = member.replace('@', '')
                member = member.replace('<', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -clan kick [@member/member_id]', delete_after = 15)
                return
            
            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return
            
            for r in message.guild.roles:
                if r.name == '[Кланы] Officer':
                    officerrole = r
                    break

            for r in message.author.roles:
                if r.name == '[Кланы] Leader' or r.name == '[Кланы] Officer':
                    role = r
                    break
            else:
                await message.channel.send('Вы не являетесь лидером или офицером клана!', delete_after = 15)
                return

            for r in member.roles:
                if r == clanrole:
                    break
            else:
                await message.channel.send('Пользователь не состоит в Вашем клане!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for t in message.guild.text_channels:
                if t.name == textname:
                    textname = t
                    break

            byebye = client.get_emoji(594523484529491988)
            ckickembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} исключил из клана {}!\n{}'.format(message.author.mention, member.mention, byebye),
                color = clanrole.color
            )

            tomember = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} исключил Вас из клана {}.\n{}'.format(message.author, clanname, byebye),
                color = clanrole.color
            )

            for r in member.roles:
                if r.name == '[Кланы] Leader':
                    await message.channel.send('Вы не можете исключить лидера клана!', delete_after = 15)
                    return
                elif r.name == '[Кланы] Officer':
                    if role.name == '[Кланы] Officer':
                        await message.channel.send('Вы не можете исключить офицера клана!', delete_after = 15)
                        return
                    elif role.name == '[Кланы] Leader':
                        await member.remove_roles(clanrole)
                        await member.remove_roles(officerrole)
                        await textname.send(embed = ckickembed)
                        await member.send(embed = tomember)
                        return
                elif r == clanrole:
                    await member.remove_roles(clanrole)
                    await member.remove_roles(officerrole)
                    await textname.send(embed = ckickembed)
                    await member.send(embed = tomember)
                    return

        elif msglower.startswith('-clan leader'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                member = msg[2]
                member = member.replace('<', '')
                member = member.replace('@', '')
                member = member.replace('>', '')
                member = message.guild.get_member(int(member))
            except IndexError:
                await message.channel.send('Используйте: -clan leader [@member/member_id]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            for r in member.roles:
                if r == clanrole:
                    break
            else:
                await message.channel.send('Пользователь не состоит в Вашем клане!', delete_after = 15)
                return

            for r in message.guild.roles:
                if r.name == '[Кланы] Leader':
                    leaderrole = r
                if r.name == '[Кланы] Officer':
                    officerrole = r

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for t in message.guild.text_channels:
                if t.name == textname:
                    textname = t
                    break

            lilsharky = client.get_emoji(596690338970599424)
            leaderembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} передал {} право на управление кланом. {}'.format(message.author.mention, member.mention, lilsharky),
                color = clanrole.color
            )

            tomember = discord.Embed(
                title = 'ClanInfo: ',
                description = 'Пользователь {} назначил Вас лидером клана {}!\n{}'.format(message.author, clanname, lilsharky),
                color = clanrole.color
            )

            await member.remove_roles(officerrole)
            await member.add_roles(leaderrole)
            await message.author.remove_roles(leaderrole)
            await message.author.add_roles(officerrole)
            await textname.send(embed = leaderembed)
            await member.send(embed = tomember)

        elif msglower.startswith('-clan leave'):
            await message.delete()
            
            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    await message.channel.send('Вы не можете покинуть клан, являясь лидером!', delete_after = 15)
                    return
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.guild.roles:
                if r.name == '[Кланы] Officer':
                    officerrole = r
                    break
            
            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for t in message.guild.text_channels:
                if t.name == textname:
                    textname = t
                    break

            plak = client.get_emoji(594173858085470208)
            leaveembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} покинул наш клан! {}'.format(message.author.mention, plak),
                color = clanrole.color
            )

            await textname.send(embed = leaveembed)
            await message.author.remove_roles(officerrole)
            await message.author.remove_roles(clanrole)

        elif msglower.startswith('-clan color'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                color = msg[2]
                color = colormap.hex2rgb(color)
            except IndexError:
                await message.channel.send('Используйте: -clan color [#цвет]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for t in message.guild.text_channels:
                if t.name == textname:
                    textname = t
                    break

            await clanrole.edit(color = discord.Color.from_rgb(color[0], color[1], color[2]))

            rainbowfrog = client.get_emoji(596776228522819596)
            colorembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} изменил цвет клана!\n{}'.format(message.author.mention, rainbowfrog),
                color = clanrole.color
            )

            await textname.send(embed = colorembed)

        elif msglower.startswith('-clan delete'):
            await message.delete()
            
            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            for r in message.guild.roles:
                if r.name == '[Кланы] Leader':
                    leaderrole = r
                if r.name == '[Кланы] Officer':
                    officerrole = r

            withclanrole = []
            for m in message.guild.members:
                for r in m.roles:
                    if r == clanrole:
                        withclanrole.append(m)

            hnik = client.get_emoji(590810923820777473)
            deleteembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} удалил клан {}!\n{}'.format(message.author, clanname, hnik),
                color = clanrole.color
            )

            for m in withclanrole:
                for r in m.roles:
                    if r.name == '[Кланы] Officer':
                        await m.remove_roles(officerrole)
                        await m.send(embed = deleteembed)
                        break
            
            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for t in message.guild.text_channels:
                if t.name == textname:
                    await t.delete()
                    break

            for t in message.guild.voice_channels:
                if t.name == clanname:
                    await t.delete()
                    break            

            await clanrole.delete()
            await message.author.remove_roles(leaderrole)

        elif msglower.startswith('-clan name'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                newname = msg[2]
            except IndexError:
                await message.channel.send('Используйте: -clan name [name]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            for c in message.guild.categories:
                if c.name == '[Кланы]':
                    cat = c
                    break

            for t in cat.text_channels:
                if t.name == textname:
                    text = t
                    await t.edit(name = newname)
                    break

            for v in cat.voice_channels:
                if v.name == clanname:
                    await v.edit(name = newname)
                    break

            pikachu = client.get_emoji(596690633431842822)
            nameembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} изменил название клана на {}!\n{}'.format(message.author.mention, newname, pikachu),
                color = clanrole.color
            )

            await clanrole.edit(name = '[Клан] {}'.format(newname))
            await text.send(embed = nameembed)

        elif msglower.startswith('-clan desc'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                desc = msg[2]
            except IndexError:
                await message.channel.send('Используйте: -clan desc [описание]', delete_after = 15)
                return

            for r in message.author.roles:
                if '[Клан] ' in r.name:
                    clanrole = r
                    clanname = r.name
                    clanname = clanname[7:]
                    break
            else:
                await message.channel.send('Вы не состоите в клане!', delete_after = 15)
                return

            for r in message.author.roles:
                if r.name == '[Кланы] Leader':
                    break
            else:
                await message.channel.send('Вы не являетесь лидером клана!', delete_after = 15)
                return

            textname = clanname.replace(' ', '-')
            textname = textname.replace('!', '')
            textname = textname.replace('@', '')
            textname = textname.replace('#', '')
            textname = textname.replace('$', '')
            textname = textname.replace('%', '')
            textname = textname.replace('^', '')
            textname = textname.replace('&', '')
            textname = textname.replace('*', '')
            textname = textname.replace('(', '')
            textname = textname.replace(')', '')
            textname = textname.replace('~', '-')
            textname = textname.replace(';', '')
            textname = textname.replace(':', '')
            textname = textname.replace('\'', '')
            textname = textname.replace('"', '')
            textname = textname.replace('/', '')
            textname = textname.replace('\\', '')
            textname = textname.replace('|', '')
            textname = textname.replace('+', '')
            textname = textname.replace('?', '')
            textname = textname.replace(',', '')
            textname = textname.replace('№', '')
            textname = textname.replace('`', '')
            textname = textname.replace('', '')
            textname = textname.lower()

            hack = client.get_emoji(594522221683277825)
            descembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} изменил описание клана на {}\n{}'.format(message.author.mention, desc, hack),
                color = clanrole.color
            )
            descdelembed = discord.Embed(
                title = 'ClanInfo: ',
                description = '{} убрал описание клана.\n{}'.format(message.author.mention, hack),
                color = clanrole.color
            )

            for t in message.guild.text_channels:
                if t.name == textname:
                    if desc != 'delete':
                        await t.edit(topic = desc)
                        await t.send(embed = descembed)
                    else:
                        await t.edit(topic = None)
                        await t.send(embed = descdelembed)
                    break

        elif msglower.startswith('-clan info'):
            await message.delete()
            msg = message.content.split(' ', 2)

            try:
                clan = msg[2]
                clan = clan.replace('<', '')
                clan = clan.replace('@', '')
                clan = clan.replace('&', '')
                clan = clan.replace('>', '')
                clan = message.guild.get_role(int(clan))
                clanname = clan.name
                clanname = clanname[7:]
            except IndexError:
                await message.channel.send('Используйте: -clan info [@clanrole/role_id]', delete_after = 15)
                return

            created = clan.created_at.date()
            year = created.year
            month = created.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            day = created.day

            members = []
            officers = []
            online = 0

            for m in message.guild.members:
                for r in m.roles:
                    if r == clan:
                        members.append(m)

            for m in members:
                for r in m.roles:
                    if r.name == '[Кланы] Leader':
                        leader = m
                        break
                    if r.name == '[Кланы] Officer':
                        officers.append(m)
                        break
                if m.status != discord.Status.offline:
                    online += 1

            mem = ''
            for m in officers:
                mem += m.mention + '\n'

            info = discord.Embed(
                description =  'Информация о клане {}:'.format(clanname),
                color = clan.color
            )
            info.add_field(
                name = 'Роль: ',
                value = '{}'.format(clan.mention),
                inline = True
            )
            info.add_field(
                name = 'Лидер: ',
                value = '{}'.format(leader.mention),
                inline = True
            )
            info.add_field(
                name = 'Создан: ',
                value = '{} {} {}'.format(day, month, year),
                inline = True
            )
            info.add_field(
                name = 'Участников: ',
                value = '{}'.format(len(members)),
                inline = True
            )
            info.add_field(
                name = 'Участников онлайн: ',
                value = '{}'.format(online),
                inline = True
            )
            info.add_field(
                name = 'Офицеры: ',
                value = '{}'.format(mem),
                inline = True
            )

            await message.channel.send(embed = info)

        elif msglower.startswith('-clan list') or msglower.startswith('-clans'):
            await message.delete()

            roles = []
            leaders = []
            clans = {}

            for r in message.guild.roles:
                if '[Клан] ' in r.name:
                    roles.append(r)

            for m in message.guild.members:
                for r in m.roles:
                    if r.name == '[Кланы] Leader':
                        leaders.append(m)
                        break

            for m in leaders:
                for r in m.roles:
                    for e in roles:
                        if r == e:
                            clans[m] = e

            clan = ''
            for a in clans.values():
                clan += a.mention + '\n'

            lead = ''
            for b in clans.keys():
                lead += b.mention + '\n'

                
            listembed = discord.Embed(
                description = 'Список кланов сервера {}: '.format(message.guild.name),
                color = discord.Color.blue()
            )
            listembed.add_field(
                name = 'Кланы: ',
                value = clan
            )
            listembed.add_field(
                name = 'Лидеры: ',
                value = lead
            )

            await message.channel.send(embed = listembed)

        elif msglower.startswith('-clan'):
            await message.delete()
            failembed = discord.Embed(
                description = '***Параметры команды -clan: ***\ncreate [#цвет] [название] - создать клан\ninvite [@member/member_id] - пригласить пользователя в клан\npromote [@member/member_if] - назначить участника клана на должность офицера\ndemote [@member/member_id] - убрать с участника должность офицера клана\nleader [@member/member_id] - назначить участника клана на должность лидера\nkick [@member/member_id] - исключить пользователя из клана\ninfo [название клана] - показывает информацию о клане',
                color = discord.Color.dark_orange()
            )
            await message.channel.send(embed = failembed, delete_after = 60)

# 000000     000000  000        000000
#000    0   00   00  000       000    0
#000       00000000  000       000
#000    0  00    00  0000      000    0
# 000000   00    00  00000000   000000
    if msglower.startswith('-calc'):
        await message.delete()

        webhooks = await message.channel.webhooks()
        try:
            web = webhooks[0]
            webid = web.id
            webtoken = web.token
        except discord.errors.Forbidden:
            await message.channel.send('Недостаточно прав!', delete_after = 15)
            return
        except:
            try:
                await message.channel.create_webhook(name = 'kvakep', avatar = message.guild.me.avatar_url)
                webhooks = await message.channel.webhooks()
                web = webhooks[0]
                webid = web.id
                webtoken = web.token
            except Exception as e:
                print(e)
                await message.channel.send('Недостаточно прав!', delete_after = 15)
                return

        wh = discord.Webhook.partial(
            id = webid,
            token = webtoken,
            adapter = discord.RequestsWebhookAdapter()
        )

        try:
            calc = message.content.split(' ', 1)[1]
        except IndexError:
            fail = discord.Embed(
                title = 'Используйте: -calc [выражение]',
                description = '***Список доступных функций: ***\n+ - сложение чисел\n- - вычитание чисел\n* - умножение чисел\n/ - деление чисел\nx^y - возведение числа x в степень y\nsqrt(x) - вычисление квадратного корня из числа\nsin(x) - вычисление синуса числа\ncos(x) - вычисление косинуса числа\ntg(x) - вычисление тангенса числа\nlog2(x) - вычисление логарифма числа по основанию 2\nlog10(x) - вычисление логарифма числа по основанию 10\n! - факториал числа\ne - экспонента\npi - число пи',
                color = discord.Color.dark_teal()
            )
            wh.send(
                embed = fail,
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'
            )
            return

        calc = calc.replace('sqrt', 'math.sqrt')
        calc = calc.replace('^', '**')
        calc = calc.replace('cos', 'math.cos')
        calc = calc.replace('sin', 'math.sin')
        calc = calc.replace('tg', 'math.tan')
        calc = calc.replace('log2', 'math.log2')
        calc = calc.replace('log10', 'math.log10')
        calc = calc.replace('pi', 'math.pi')
        calc = calc.replace('e', 'math.e')

        try:
            while True:
                number = re.search(r'\d*!', calc)
                exp = re.search(r'(.*)!', calc)
                if number:
                    num = number.replace('!', '')
                    num = eval(num)
                    calc = calc.replace(number, 'math.factorial({})'.format(num))
                elif exp:
                    num = exp.replace('!', '')
                    num = eval(num)
                    calc = calc.replace(number, 'math.factorial({})'.format(num))
                else:
                    break
        except:
            pass

        try:
            result = eval(calc)
            if math.isfinite(result):
                wh.send(
                    content = str(message.content.split(' ', 1)[1]) + ' = ' + str(result),
                    username = 'Funny Calculator',
                    avatar_url = 'https://i.imgur.com/y36oYtu.png'
                )
            else:
                wh.send(
                    content = 'Не скажу!',
                    username = 'Funny Calculator',
                    avatar_url = 'https://i.imgur.com/y36oYtu.png'
                )
        except ZeroDivisionError:
            wh.send(
                content = 'Я ещё не научился делить на 0 :(',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'
            )
            return
        except SyntaxError:
            wh.send(
                content = 'Не могу такое :(',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'
            )
            return
        except discord.errors.HTTPException:
            wh.send(
                content = 'Слишком много!',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'   
            )
            return
        except ValueError:
            wh.send(
                content = 'Ошибка!',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png' 
            )
            return
        except TypeError:
            wh.send(
                content = 'Не могу такое :(',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'
            )
            return
        except AttributeError:
            wh.send(
                content = 'Не могу такое :(',
                username = 'Funny Calculator',
                avatar_url = 'https://i.imgur.com/y36oYtu.png'
            )
            return
        
#00000     00000  00000000  00000     00000  0000
#000 00   00 000  0000      000 00   00 000   00
#000  00 00  000  00000000  000  00 00  000   00
#000   000   000  0000      000   000   000   00
#000         000  00000000  000         000  0000
    if msglower.startswith('-memberinfo') or msglower.startswith('-memi'):
        await message.delete()
        msg = message.content.split(' ', 1)

        try:
            member = msg[1]
            member = member.replace('<', '')
            member = member.replace('@', '')
            member = member.replace('>', '')
            member = message.guild.get_member(int(member))
        except IndexError:
            await message.channel.send('Используйте: -memberinfo [@member/member_id]', delete_after = 15)
            return

        created = member.created_at.date()
        year = created.year
        month = created.month
        if month == 1:
            month = 'января'
        elif month == 2:
            month = 'февраля'
        elif month == 3:
            month = 'марта'
        elif month == 4:
            month = 'апреля'
        elif month == 5:
            month = 'мая'
        elif month == 6:
            month = 'июня'
        elif month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'
        elif month == 9:
            month = 'сентября'
        elif month == 10:
            month = 'октября'
        elif month == 11:
            month = 'ноября'
        elif month == 12:
            month = 'декабря'
        day = created.day
        created = '{} {} {}'.format(day, month, year)

        joined = member.joined_at.date()
        year = joined.year
        month = joined.month
        if month == 1:
            month = 'января'
        elif month == 2:
            month = 'февраля'
        elif month == 3:
            month = 'марта'
        elif month == 4:
            month = 'апреля'
        elif month == 5:
            month = 'мая'
        elif month == 6:
            month = 'июня'
        elif month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'
        elif month == 9:
            month = 'сентября'
        elif month == 10:
            month = 'октября'
        elif month == 11:
            month = 'ноября'
        elif month == 12:
            month = 'декабря'
        day = joined.day
        joined = '{} {} {}'.format(day, month, year)

        nick = member.nick
        if nick == None:
            nick = member.display_name

        try:
            prem = member.premium_since.date()
            day = prem.day
            month = prem.month
            if month == 1:
                month = 'января'
            elif month == 2:
                month = 'февраля'
            elif month == 3:
                month = 'марта'
            elif month == 4:
                month = 'апреля'
            elif month == 5:
                month = 'мая'
            elif month == 6:
                month = 'июня'
            elif month == 7:
                month = 'июля'
            elif month == 8:
                month = 'августа'
            elif month == 9:
                month = 'сентября'
            elif month == 10:
                month = 'октября'
            elif month == 11:
                month = 'ноября'
            elif month == 12:
                month = 'декабря'
            year = prem.year
            prem = 'Действует с {} {} {}'.format(day, month, year)
        except AttributeError:
            prem = 'Не приобретена'

        status = member.status
        if status == discord.Status.online:
            status = '{} Онлайн'.format(client.get_emoji(596453205341241355))
        elif status == discord.Status.idle:
            status = '{} Не активен'.format(client.get_emoji(596453234227413031))
        elif status == discord.Status.dnd:
            status = '{} Не беспокоить'.format(client.get_emoji(596453249712652308))
        elif status == discord.Status.offline:
            status = '{} Оффлайн'.format(client.get_emoji(596453263927279729))

        mobile = member.is_on_mobile()
        if mobile == True:
            mobile = 'Мобильное приложение'
        elif mobile == False:
            mobile = 'Приложение для компьютера'

        toprole = member.top_role.mention

        memid = member.id

        incognito = client.get_emoji(596697306728759296)
        memi = discord.Embed(
            description = '{}Информация о пользователе {}'.format(incognito, member.mention),
            color = member.color
        )
        memi.set_thumbnail(
            url = member.avatar_url
        )
        memi.set_footer(
            text = 'Requested by {}'.format(message.author),
            icon_url = message.author.avatar_url
        )
        memi.add_field(
            name = 'Имя:',
            value = member.name,
            inline = True
        )
        memi.add_field(
            name = 'Тэг:',
            value = member.discriminator,
            inline = True
        )
        memi.add_field(
            name = 'Зарегистрирован: ',
            value = created,
            inline = True
        )
        memi.add_field(
            name = 'Подписка Discord Nitro:',
            value = prem,
            inline = True
        )
        memi.add_field(
            name = 'Ник:',
            value = nick,
            inline = True
        )
        memi.add_field(
            name = 'Зашёл на сервер:',
            value = joined,
            inline = True
        )
        memi.add_field(
            name = 'Статус:',
            value = status,
            inline = True
        )
        memi.add_field(
            name = 'Клиент:',
            value = mobile,
            inline = True
        )
        memi.add_field(
            name = 'Наивысшая роль:',
            value = toprole,
            inline = True
        )
        memi.add_field(
            name = 'ID:',
            value = memid,
            inline = True
        )
        await message.channel.send(embed = memi)






"""
 xxxxxxx   xxxxx    xxx      xxxxxxx    xxxxxxxx    xxxxxx   xxxxxx         xxxxxx  xxxxxxx   xxxxxxx       ################
xxx   xxx  xxx xx   xxx      xxx   xx   xxxx       xx   xx  xxx    x       xx   xx  xxx   xx  xxx   xx      ################
xxx   xxx  xxx  xx  xxx      xxxxxxx    xxxxxxxx  xxxxxxxx  xxx           xxxxxxxx  xxx   xx  xxx   xx      ################
xxx   xxx  xxx   xx xxx      xxx   xx   xxxx      xx    xx  xxx    x      xx    xx  xxx   xx  xxx   xx      ################
 xxxxxxx   xxx    xxxxx      xxx    xx  xxxxxxxx  xx    xx   xxxxxx       xx    xx  xxxxxxx   xxxxxxx       ################
"""
@client.event
async def on_reaction_add(reaction, user):

    if user == client.user:
        return

    if str(reaction.emoji) == '🚩' and user.id == 400231667408699392:
        await reaction.message.delete()

    if str(reaction.emoji) == '📌':
        if user.guild_permissions.manage_messages or user.id == 400231667408699392:
            await reaction.message.remove_reaction('📌', user)
            await reaction.message.pin()
        
    try:
        if reaction.message.id == myemojismsg.id and user.id == 400231667408699392:
            global emojiindex
            if str(reaction.emoji) == '◀':
                try:
                    await myemojismsg.edit(embed = embedlist[emojiindex-1])
                    emojiindex -= 1
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
                except IndexError:
                    emojiindex = 0
                    await myemojismsg.edit(embed = embedlist[emojiindex-1])
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
            if str(reaction.emoji) == '▶':
                try:
                    await myemojismsg.edit(embed = embedlist[emojiindex+1])
                    emojiindex += 1
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
                except IndexError:
                    emojiindex = 0
                    await myemojismsg.edit(embed = embedlist[emojiindex])
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
    except:
        pass
    


















client.run('NTgxODIzNzgzMDI3OTk4NzIx.XSTzMA.u-nnhKYLK0yuCvhMVsdOQwYaqq4')