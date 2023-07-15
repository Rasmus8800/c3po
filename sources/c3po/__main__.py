"""Точка входа клиента для C3PO."""

import os

from discord import Intents

from bot import C3PO

__all__ = []

bot = C3PO(
    intents=Intents.default(),
)

token = os.getenv("C3PO_BOT_TOKEN")

if not token:
    raise RuntimeError("Specify the bot token!")

bot.run(token=token)
