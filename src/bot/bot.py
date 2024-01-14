import json
import discord



f = open("./config.json")
config = json.load(f)
f.close()

token = config["token"]
print(token)


intents = discord.Intents(messages=True, guilds=True, message_content=True)

bot = discord.Bot(intents=intents)

servers = [1181600739320135751]


connections = {}


@bot.event
async def on_message(message):
    print(f"{message.author.name} : {message.content}")


@bot.event
async def on_ready():
    print("Le bot est prêt !")

    try:
        print("coucou")
        #synced = await tree.sync(guild=discord.Object(id=1181600739320135751))
        #print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.slash_command(guild_ids=servers, name="ping", description="Répond pong.")#guild=discord.Object(id=1181600739320135751), name="ping", description="Répond pong")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("PONG !", ephemeral=True)


@bot.slash_command(guild_ids=servers, name="join")
async def join(ctx):
    print(ctx)
    if ctx.user.voice:
        await ctx.response.send_message("I'm coming !")
        vc = await ctx.user.voice.channel.connect()
        sink = discord.sinks.MP3Sink()
        vc.start_recording(sink, test_son, ctx)
        print(sink)
        print(vc.is_recording())
    else:
        await ctx.response.send_message("You are not connected to any voice channel.")


async def test_son(sink, ctx):
    recorded_users = [
        f"<@{user_id}>"
        for user_id, audio in sink.audio_data.items()
    ]
    files = [discord.File(audio.file, f"{user_id}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]
    await ctx.channel.send(f"Finished! Recorded audio for {', '.join(recorded_users)}.", files=files)


@bot.slash_command(guild_ids=servers, name="leave")
async def leave(ctx):
    if len(bot.voice_clients) > 0:
        vc = ctx.user.voice
        vc.stop_recording()
        await bot.voice_clients[0].disconnect(force=True)
        await ctx.response.send_message("I'm leaving !")
    else:
        await ctx.response.send_message("I'm not in a voice channel !")


bot.run(token=token)
