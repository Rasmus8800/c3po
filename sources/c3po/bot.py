"""Модуль с клиентом для C3PO."""

from typing import Any

from discord import Client, Intents
from loguru import logger

__all__ = ["C3PO"]


class C3PO(Client):
    """Клиент для C3PO."""

    def __init__(self, *, intents: Intents, **options: Any) -> None:
        """Создает экземпляр клиента для C3PO.

        :param intents: Намерения бота.
        """
        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        if not self.user:
            logger.error("User cant be none!")
        else:
            logger.info(f"Logged in {self.user} ({self.user.id})!")
