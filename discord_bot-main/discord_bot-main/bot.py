import discord
import response as res
import yt_dlp as youtube_dl
from time import sleep
from gtts import gTTS
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = res.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("DISCORD_TOKEN")
    # set discord intents to admin
    intents = discord.Intents.all()
    intents.members = True

    # create client
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel is not None and player.is_connected():
            text = "Salut " + member.nick
            language = 'ro'
            speech = gTTS(text=text, lang=language)
            speech.save("soundboard/speech.mp3")
            player = member.guild.voice_client
            player.play(discord.FFmpegPCMAudio(executable="/snap/bin/ffmpeg", source="soundboard/speech.mp3"))

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel is not None and after.channel is None:
            text = member.nick + " a ieșit din vois cenăl"
            language = 'ro'
            speech = gTTS(text=text, lang=language)
            speech.save("soundboard/speech.mp3")
            player = member.guild.voice_client
            player.play(discord.FFmpegPCMAudio(executable="/snap/bin/ffmpeg", source="soundboard/speech.mp3")) 

    @client.event
    async def on_member_join(member):
        print(f'{member} has joined the server!')


    @client.event
    async def on_message(message):

        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        nickname = str(message.author.nick)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        if res.containsBadWords(user_message):
            await message.author.move_to(None)
        elif "joaca piatra-foarfeca-hartie" in user_message:
            await message.channel.send(nickname + " a dat " + res.chooseRandomPHF())
        elif "joaca barbut" in user_message:
            await message.channel.send(nickname + " a dat " + str(res.chooseRandomDiceScore()))
        elif "joaca pacanele" in user_message:
            await message.channel.send(nickname + " a dat ")
            await message.channel.send(res.chooseRandomPacanele())
        elif "meme pls" in user_message:
            await message.channel.send(res.getMeme(user_message))

        # use soundboard
        player = message.guild.voice_client
        
        if user_message == 'join':
            await message.author.voice.channel.connect()

        if user_message == 'leave':
            await player.disconnect()
        
        if user_message == 'mac':
            player.play(discord.FFmpegPCMAudio(executable="/snap/bin/ffmpeg", source="soundboard/quack.mp3"))
            

        if user_message.split(' ')[0] == 'play':
            text = user_message[4:]
            print(text)
            language = 'ro'
            speech = gTTS(text=text, lang=language)
            speech.save("soundboard/speech.mp3")
            player.play(discord.FFmpegPCMAudio(executable="/snap/bin/ffmpeg", source="soundboard/speech.mp3"))


    client.run(TOKEN)