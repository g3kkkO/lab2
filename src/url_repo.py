import re

import requests


class UrlRepository:
    """Загрузка текста веб-страницы по URL с очисткой от разметки."""

    @classmethod
    def get_text(cls, url: str) -> str:
        """Получает страницу и возвращает её текст без HTML-разметки."""
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return cls._remove_tags(response.text)

    @staticmethod
    def _remove_tags(html: str) -> str:
        """Удаляет script/style вместе с содержимым, затем остальные теги."""
        html = re.sub(r'<script[^>]*>.*?</script>', ' ', html,
                      flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r'<style[^>]*>.*?</style>', ' ', html,
                      flags=re.DOTALL | re.IGNORECASE)
        return re.sub(r'<[^>]*>', ' ', html, flags=re.DOTALL)