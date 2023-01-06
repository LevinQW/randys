import random

import discord
from discord.ext import commands

import time

import wikipedia

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from discord.ext.commands import CheckFailure

# file = open('config.json', 'r')
# config = json.load(file)

bot = commands.Bot(intents=discord.Intents.all() , command_prefix='*' , description='The Best Bot For the Best User!')


@bot.command(name='prefix')
async def prefix(ctx):
    await ctx.send(f'Ты придурок? Префикс бота: "*". Иначе как бы ты написал эту команду?\nasd\nasd', )


@bot.command(name='hello')
async def hello(ctx):
    embed = discord.Embed(title="Привет!", description=f'**Это тестовый бот для дискорда (вау)!\n Давай на связи**\n ||ZZzzz...||', colour=0xd6aeee)
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print('------BOT ONLINE------')
    await bot.change_presence(status = discord.Status.do_not_disturb, activity=discord.Game('AFK'))


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, count: int):

        await ctx.channel.purge(limit=count+1)

        embed = discord.Embed(title="Успешно!✅", description=f'Удалено {count} сообщений!', colour=0xd6aeee)
        embed.set_footer(text=f'Запрос от {ctx.author}')
        msg = await ctx.send(embed=embed)
        # id = msg.id
        time.sleep(4)
        await bot.delete_message(msg)





@clear.error
async def clear_error(ctx, error):
    if isinstance(error, CheckFailure):
        msg = "Недостаточно прав на использование этой команды!"
        await ctx.send(msg)



@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="Причина не указана."):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"{user.name} был кикнут!", description=f"----------------\nПричина: {reason}\n----------------")
        kick.set_footer(text=f'Запрос от {ctx.author}') #, icon_url=ctx.author.avatar_url)
        await ctx.message.delete()

        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@bot.command(name='wiki')
async def wiki(ctx, arg=None):
    if arg == None:
        none = discord.Embed(title= "Ошибка!", description="***wiki [запрос]**")
        await ctx.send(embed= none)
    else:
      wikipedia.set_lang("ru")
      summary = wikipedia.summary(arg, sentences=2)

      embed = discord.Embed(title= "Запрос: " + arg, description= summary, colour=0xAFEEEE)
      embed.set_footer(text=f'Запрос от {ctx.author}')
      embed.set_author(name='Wikipedia.org', url="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0", icon_url="https://cdn.discordapp.com/attachments/893516645102915665/1060271730070933575/800px-Wikipedia-logo-v2.svg.png")


      await ctx.send(embed= embed)





@kick.error
async def kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        msg = "Недостаточно прав на использование этой команды!"
        await ctx.send(msg)


@bot.command()
async def ach(ctx, *, text):
    text1 = text
    if len(text1) >= 30:

        await ctx.send(embed=discord.Embed(title= "Ошибка", description=f'Dлина текста не должна превышать **30**', colour=discord.Color.red()))

        return
    else:
      text1 = text
      achievement = Image.open("achievment.png")
      colors = ["white"]
      drawer = ImageDraw.Draw(achievement)
      if len(text1) >= 20:
        font = ImageFont.truetype("F77 Minecraft.ttf", 14)
        for color in colors:
          drawer.text((60, 35), text=text1, font=font, fill=color)
        file = discord.File("exit.png", filename="exit.png")
        embed = discord.Embed(title="Достижение!", description=f"{ctx.author.mention} получил новое достижение!", colour=0xFFD700)
        embed.set_image(url="attachment://exit.png")
      elif len(text1) < 20:
          font = ImageFont.truetype("F77 Minecraft.ttf", 15)
          for color in colors:
              drawer.text((60, 35), text=text1, font=font, fill=color)
          file = discord.File("exit.png", filename="exit.png")
          embed = discord.Embed(title="Достижение!", description=f"{ctx.author.mention} получил новое достижение!",
                                colour=0xFFD700)
          embed.set_image(url="attachment://exit.png")



    achievement.save("exit.png")

    # await ctx.send(file = discord.File("exit.png"))
    await ctx.send(file=file, embed=embed)


@bot.command()
async def rand(ctx, arg: int):
   if arg.__int__() and arg <= 10000 and arg != 0:
     result = random.randint(0, arg)
     x = 1 / arg

     result2 = round(x, 4)
     embed = discord.Embed(title= 'Рандомное число от 1 до ' + str(arg), description='Выпало  число: ' + str(result) + '\n Вероятность события = ' + str(result2), colour=0x9400D3)
     await ctx.send(embed=embed)

   elif arg > 10000:
       embed = discord.Embed(title='Ошибка', description='Число не должно превышать **10 000**', colour=discord.Color.red())
       await ctx.send(embed=embed)

   elif arg.__str__():
       embed = discord.Embed(title='Ошибка', description='Нужно ввести число, которое ≥ 1', colour=discord.Color.red())
       await ctx.send(embed=embed)

   elif arg <= 0:
       embed = discord.Embed(title='Ошибка', description='Нужно ввести число, которое ≥ 1', colour=discord.Color.red())
       await ctx.send(embed=embed)


   else:
       embed = discord.Embed(title='Ошибка', description='Нужно ввести число, которое ≥ 1', colour=discord.Color.red())
       await ctx.send(embed=embed)


@rand.error
async def kick_error(ctx: commands.Context, error: commands.CommandError):

    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title='Ошибка', description='Нужно ввести число, которое ≥ 1', colour=discord.Color.red())
        await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def text(ctx, *, arg=None):
    if arg == None:
        await ctx.send("Введи текст!")


    else:
        await ctx.send(arg)


@bot.command()
async def embed(ctx, *, arg):
    embed = discord.Embed(title=arg, colour=0xFFD700)
    await ctx.send(embed=embed)






















bot.run('MTA0NTc1NTYxODg2NDEzNjI1NQ.GDzBtS.4sY78lBuLRO_pH7DLZNZ-phGf-7ueGHb9CS2OQ')        #974478826566