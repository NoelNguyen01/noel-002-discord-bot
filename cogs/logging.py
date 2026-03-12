import logging
from discord import Client
from discord.ext import commands

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message_delete(message):
    logging.info(f'Message deleted: {message.content}')

@bot.event
async def on_message_edit(before, after):
    logging.info(f'Message edited from: {before.content} to: {after.content}')

@bot.event
async def on_member_join(member):
    logging.info(f'Member joined: {member.name}')

@bot.event
async def on_member_remove(member):
    logging.info(f'Member left: {member.name}')