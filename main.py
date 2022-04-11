import discord
import datetime
import asyncio
import time
from discord.ext import commands,tasks
from functions.date_register import date_register
from functions.sleep_return_resp import sleep_return_resp
TOKEN = '**************' ## Вставьте токен своего бота


client = discord.Client()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.',intents=intents)

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@bot.event
async def on_member_join(member):
    await member.guild.system_channel.send(f"К нам прилетел {member.mention}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Команда не найдена (Список команд .help)**")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Аргумент отсутствует (.fun arg)**')


@bot.command( pass_context= True )
async def call(ctx,text):
  async for members in ctx.guild.fetch_members(limit=150):
    if members == bot.user:
      pass
    else:
      await ctx.send(f"{text}-{members.mention}")


@bot.command( pass_context= True )
async def return_resp(ctx):
  print(1)
  while True:
    img_day,day_str,s = date_register()
    print(1)
    if sleep_return_resp(s) == True:
      await ctx.send(file=discord.File("couples/" + img_day), content="Рассписания на " + day_str)
      await asyncio.sleep(60)
    else:
      await asyncio.sleep(1)



bot.run(TOKEN)