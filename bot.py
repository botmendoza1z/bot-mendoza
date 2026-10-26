import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# --- Servidor web para que Render no apague el bot ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Mendoza activo 24/7"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# --- Bot de Discord ---
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def entra(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Ya estoy en {channel.name} 24/7 🔥')
    else:
        await ctx.send('Primero métete a un canal de voz')

@bot.command()
async def sal(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Me salí')
    else:
        await ctx.send('No estoy en voz')

TOKEN = os.getenv('DISCORD_TOKEN')
if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    bot.run(TOKEN)
