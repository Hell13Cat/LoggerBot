import discord, time, json, os
from discord.ext import commands


namefilelog=str(os.getcwd()+"\log\\"+str(time.ctime(time.time()))+".txt").replace("\\","/").replace(":","-").replace("-",":",1)
file = open(str(namefilelog), "wb")
file.write((str(time.ctime(time.time()))+"\n").encode('utf8'))
file.close()


global counter
counter = 0



def filelog(namefilelog, guild, msg, channel, autor):
    global counter
    counter += 1
    text = (str(time.ctime(time.time()))+"->>"+str(guild)+"->>"+str(channel)+"->>"+str(autor)+"->>"+str(msg)+"\n").encode('utf8')
    file = open(namefilelog, "ab")
    file.write(text)
    file.close()



tokenfile = str(os.getcwd()+"\\token.txt").replace("\\","/").replace(":","-").replace("-",":",1)
DISCORD_BOT_TOKEN = open(tokenfile, "r").read()
client = discord.Client()
owneridfile = str(os.getcwd()+"\\idowner.txt").replace("\\","/").replace(":","-").replace("-",":",1)
ownerid = open(owneridfile, "r").read()



@client.event
async def on_ready():
    print("Log Chat Run")
    print('-------------------------')
    print("Имя бота:"+str(client.user.name))
    print("ID бота:"+str(client.user.id))
    print('-------------------------')

#discord.Activity(**kwargs)  discord.Streaming(*, name, url, **extra)
runlog = 0
@client.event
async def on_message(message, *msg):
    global runlog
    global counter
    if runlog==1:
        filelog(namefilelog,message.guild,message.content,message.channel,message.author)
    else:
        pass



    if message.content=="log!count":
        if ownerid == str(message.author.id):
            await message.delete()
            channel = message.channel
            await channel.send("```Залогинено " + str(counter) + " сообщений чата.```")
        else:
            await message.delete()
            channel = message.channel
            await channel.send("```Отказано в доступе. Вы не владелец сервера.```")



    if message.content=="log!start":
        if ownerid == str(message.author.id):
            game = discord.Game("Spy!")
            await client.change_presence(status=discord.Status.online, activity=game)
            runlog=1
            await message.delete()
            channel = message.channel
            await channel.send("```Логирование включено.```")
        else:
            await message.delete()
            channel = message.channel
            await channel.send("```Отказано в доступе. Вы не владелец сервера.```")



    if message.content=="log!stop":
        if ownerid == str(message.author.id):
            game = discord.Game("Wait....")
            await client.change_presence(status=discord.Status.dnd, activity=game)
            runlog=0
            await message.delete()
            channel = message.channel
            await channel.send("```Логирование выключено```")
        else:
            await message.delete()
            channel = message.channel
            await channel.send("```Отказано в доступе. Вы не владелец сервера.```")


    if message.content=="log!size":
        if ownerid == str(message.author.id):
            await message.delete()
            sizelog = os.path.getsize(namefilelog)
            channel = message.channel
            await channel.send("```Размер логов " + str(sizelog) + " байт.```")
        else:
            await message.delete()
            channel = message.channel
            await channel.send("```Отказано в доступе. Вы не владелец сервера.```")


    if message.content=="log!link":
        if ownerid == str(message.author.id):
            await message.delete()
            channel = message.channel
            await channel.send("```Ссылка на бота:```https://discordapp.com/oauth2/authorize?client_id="+str(client.user.id)+"&permissions=8&scope=bot")
        else:
            await message.delete()
            channel = message.channel
            await channel.send("```Отказано в доступе. Вы не владелец сервера.```")



client.run(DISCORD_BOT_TOKEN)