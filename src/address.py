import re


class Address:
    """Работа с IPv4-адресами: валидация строки и поиск в тексте."""

    # Один октет IPv4: альтернативы от 0 до 255.
    _OCTET = r'(?:2[0-5][0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'

    # Шаблон для проверки строки целиком.
    valid_pattern = rf'(?:{_OCTET}\.){{3}}{_OCTET}'

    # Шаблон для поиска в тексте: границы (?<!\d)/(?!\d) не дают
    # поймать адрес внутри более длинного числа (например, 999192.168.1.12999).
    find_pattern = rf'(?<!\d)(?:{_OCTET}\.){{3}}{_OCTET}(?!\d)'

    @classmethod
    def address_validation(cls, address: str) -> bool:
        """Проверяет, является ли строка корректным IPv4-адресом целиком."""
        return re.fullmatch(cls.valid_pattern, address) is not None

    @classmethod
    def get_all(cls, text: str) -> list[str]:
        """Возвращает список уникальных IPv4-адресов, найденных в тексте."""
        return list(set(re.findall(cls.find_pattern, text)))