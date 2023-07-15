"""Модуль с обработчиками логов."""

import logging
import sys

from loguru import logger

__all__ = ["InterceptHandler"]


class InterceptHandler(logging.Handler):
    """Перехватывающий обработчик."""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno  # type: ignore

        frame, depth = sys._getframe(6), 6

        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore
            depth += 1

        it = logger.opt(depth=depth, exception=record.exc_info)

        it.log(level, record.getMessage())
