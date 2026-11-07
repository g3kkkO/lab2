class FileRepository:
    """Чтение текста из локального файла."""

    @classmethod
    def get_text(cls, path: str) -> str:
        """Читает файл целиком и возвращает его содержимое как строку."""
        with open(path, encoding="utf-8") as f:
            return f.read()