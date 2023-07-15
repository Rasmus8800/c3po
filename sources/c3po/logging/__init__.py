"""Пакет с логированием."""

import logging

from .handlers import InterceptHandler

__all__ = ["InterceptHandler", "setup_logging"]


def setup_logging() -> None:
    """Устанавливает логирование."""
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(InterceptHandler())

    http = logging.getLogger("discord.http")
    http.setLevel(logging.INFO)
    http.addHandler(InterceptHandler())
