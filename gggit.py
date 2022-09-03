from ctypes import resize, sizeof
import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font


intents = discord.Intents.default()
intents.members = True #Enables it
bot = commands.Bot(command_prefix=">", intents = discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")




@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel

    background = Editor("sskttr.jpg")
    profile_image = await load_image_async(str(member.avatar_url))

    profile = Editor(profile_image).resize((650, 650)).circle_image()

    poppins = Font.poppins(size=120, variant="bold")
    poppins_small = Font.poppins(size=140, variant="light",)

    background.paste(profile, (645, 268))
    background.ellipse((645, 268), 650, 650, outline="white",stroke_width=5,)

    background.text((939, 160), f"Welcome to {member.guild.name}", color="Black", font=poppins, align="center", )
    background.text((947, 985), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")

    file = File(fp=background.image_bytes, filename="sskttr.jpg")
    await channel.send(f"Kamusta! {member.mention} Welcome tol! **{member.guild.name}** usap tayo dito tol <#1014281220282126449>")
    await channel.send(file=file)




bot.run("MTAwNTM1ODI0MTU2MTIwMjczMA.G4gSN_.bnMGHpNjiUjFvGHnKlHUVe8cyMWN2NsCE99GVo")