import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    if not attachments:
        await ctx.send("В сообщении нет  изображений.")
        return
    
    for attachment in attachments:
        if attachment.content_type.startswith('image'):
            await attachment.save(f'images/{attachment.filename}')
            await ctx.send(f'Изображение "{attachment.filename}" сохранено!')
        else:
            await ctx.send(f'Файл "{attachment.filename}" не является изображением.')

bot.run("MTE1Mjk2MDkxMzc3MTYwMjAwMQ.Gvsrv4.SOxGnnRJmf0IPJ0kSwoZ9qRi6YRhZXC37mgH-k")
