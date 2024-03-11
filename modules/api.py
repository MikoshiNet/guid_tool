# pylint: disable=missing-docstring
# antglo modules/discord.py
# March 11, 2024

import discord
from discord.ext import commands
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Devices

# Create SQLAlchemy engine and session
engine = create_engine('sqlite:///modules/database.db', echo=True)
Session = sessionmaker(bind=engine)

# Create Discord bot instance
bot = commands.Bot(command_prefix='!')

# Define a command to query the database
@bot.command()
async def get_device(ctx, device_id: int):
    session = Session()
    device = session.query(Devices).get(device_id)
    if device:
        await ctx.send(f"Device found: {device.name}")
    else:
        await ctx.send("Device not found.")
    session.close()

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
