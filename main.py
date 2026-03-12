import discord

# Create a new instance of the bot
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')