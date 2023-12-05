import json
import discord
from discord import app_commands
from discord.ext import commands


f = open("./config.json")
config = json.load(f)
f.close()

token = config["token"]
print(token)


intents = discord.Intents(messages=True, guilds=True, message_content=True)

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_message(message):
    print(f"{message.author.name} : {message.content}")


@client.event
async def on_ready():
    print("Le bot est prêt !")

    try:
        synced = await tree.sync(guild=discord.Object(id=1181600739320135751))
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@tree.command(guild=discord.Object(id=1181600739320135751), name="ping", description="Répond pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("PONG !", ephemeral=True)


@tree.command(guild=discord.Object(id=1181600739320135751), name="join")
async def join(ctx):
    if ctx.user.voice:
        await ctx.response.send_message("I'm coming !")
        await ctx.user.voice.channel.connect()
    else:
        await ctx.response.send_message("You are not connected to any voice channel.")


@tree.command(guild=discord.Object(id=1181600739320135751), name="leave")
async def leave(ctx):
    if len(client.voice_clients) > 0:
        await ctx.response.send_message("I'm leaving !")
        await client.voice_clients[0].disconnect(force=True)
    else:
        await ctx.response.send_message("I'm not in a voice channel !")
client.run(token=token)
