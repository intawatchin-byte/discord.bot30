import discord
from discord.ext import commands
import os

bot = discord.ext.commands.Bot(command_prefix='!', intents=discord.Intents.all())

#Token bot
TOKEN = "MTQ4MzcxOTIwMzEyNjExNjQ0Mw.GA-_ni.ywIKu6GPQ-dJGzRhJEdhdUubg0JW3NAlnj7IVI"

@bot.event
async def on_ready():
    print("Bot Online!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1479410264397971549)
    text = f"ยินดีต้อนรับ {member.mention} สู่เซิร์ฟเวอร์ของเรา!"
    await channel.send(text)
    await member.send("ยินดีต้อนรับสู่เซิร์ฟเวอร์ของเรา! หากคุณมีคำถามหรือข้อสงสัยใด ๆ อย่าลังเลที่จะถามเราได้เลยนะครับ!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1479410264397971549)
    text = f"ลาก่อน {member.mention} หวังว่าจะได้เจอกันอีกนะ!"
    await channel.send(text)
    await member.send("ขอบคุณที่เคยเป็นส่วนหนึ่งของเซิร์ฟเวอร์ของเรา! หากคุณต้องการกลับมาอีกครั้งในอนาคต เรายินดีต้อนรับเสมอครับ!")

bot.run("MTQ4MzcxOTIwMzEyNjExNjQ0Mw.GA-_ni.ywIKu6GPQ-dJGzRhJEdhdUubg0JW3NAlnj7IVI")
from myserver import server_on

server_on()

bot.run(os.getenv('TOKEN'))