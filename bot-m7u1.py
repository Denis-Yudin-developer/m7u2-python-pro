import discord
from discord.ext import commands
import get_model

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    res = ""
    img_format =["png", "jpg", "jpeg"]
    if ctx.message.attachments != []:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_name = "123.png" => ["123", "png"]
            format = file_name.split(".")[1]
            if format not in img_format:
                await ctx.send("Неверный формат файла")
                return
            await attachment.save(file_name)
            await ctx.send("Вы сохранили файл")
            #обрабатываем ошибочную ситуацию
            res = get_model.classife_image(file_name)
            if res == "":
                await ctx.send("Прошу прощения! С моделью возникла ошибка")
            else:
                await ctx.send(res)

bot.run("MTE1MjU5OTM4MzQ4NTk4ODkxNA.GT6wY2.W8oePE8-Y-OTSmESsXoV34kywpH3Lg3DVFQ1Kk")