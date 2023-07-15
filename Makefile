.PHONY: all styles types tests
.DEFAULT_GOAL := all

all: styles types tests

# Форматирует исходный код и тесты.
styles:
	@black sources tests
	@ruff check sources tests

# Проверяет типы в исходном коде и тестах.
types:
	@mypy sources tests

# Запускает тесты и измеряет покрытие исходного кода.
tests:
	@coverage run -m pytest
	@coverage report