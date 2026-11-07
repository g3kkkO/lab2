# Лабораторная работа №2: Регулярные выражения в Python

**Вариант 2:** Проверка и поиск синтаксически корректных IP-адресов (IPv4).

## Описание проекта

Утилита командной строки (CLI) для валидации IPv4-адресов и поиска их в тексте. Программа поддерживает три режима работы: проверка пользовательского ввода, поиск адресов в локальном файле и поиск на веб-странице по URL.

## Возможности

- **Валидация** — проверка, является ли строка корректным IPv4-адресом целиком.
- **Поиск в файле** — находит все IPv4-адреса в локальном текстовом файле
- **Поиск по URL** — получает веб-страницу, очищает её от HTML-разметки и находит все IPv4-адреса.
- **Очистка разметки** — удаление тегов `<script>` и `<style>` вместе с содержимым.
- **Границы regex** — `(?<!\d)` и `(?!\d)` не дают поймать адрес внутри более длинного числа.
- **CLI на argparse** — subcommands `valid` и `find` с флагами `-f` / `-u`.


## Структура проекта

```text
lab2/
├── files/                      # Сохранённые текста для офлайн-тестов
│   ├── elma365.txt
│   ├── sber.txt
│   ├── yandex.txt
│   ├── mail.txt
│   └── skill.txt
├── src/
│   ├── __init__.py
│   ├── address.py              # Класс Address (валидация и поиск)
│   ├── file_repo.py            # Класс FileRepository (чтение файлов)
│   └── url_repo.py             # Класс UrlRepository (загрузка и очистка HTML)
├── tests/
│   └── test_valid_address.py   # Unit-тесты (pytest)
├── main.py                     # CLI (argparse), точка входа
├── pyproject.toml              # Зависимости проекта
├── pytest.ini                  # Настройки pytest (pythonpath, маркеры)
├── uv.lock
└── README.md
```

## Модули

| Файл | Что содержит |
|---|---|
| `src/address.py` | `Address` — `valid_pattern`, `find_pattern`, `address_validation()`, `get_all()`. |
| `src/file_repo.py` | `FileRepository` — `get_text()` читает файл целиком в UTF-8. |
| `src/url_repo.py` | `UrlRepository` — `get_text()` загружает страницу и очищает от тегов. |
| `tests/test_valid_address.py` | Параметризованные тесты: 53 кейса валидации, 5 файлов, 5 URL. |
| `main.py` | `argparse` CLI: `valid`, `find -f`, `find -u`. |

## Установка и запуск

Склонируйте репозиторий и перейдите в папку проекта:

```bash
git clone https://github.com/g3kkkO/lab2.git
cd lab2
```

### Способ 1: с использованием uv

```bash
uv sync
uv run main.py --help
```

### Способ 2: классическое виртуальное окружение

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
pip install requests pytest
python main.py --help
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests pytest
python3 main.py --help
```

Далее замените `uv run` на `python`.

## Как пользоваться

CLI построен на `argparse`. Две команды: `valid` (проверка) и `find` (поиск).

### Проверка адреса

```bash
uv run main.py valid 192.168.1.1
uv run main.py valid 256.0.0.1
uv run main.py valid "192.168.1.1 "
```

### Поиск в файле

```bash
uv run main.py find -f files/elma365.txt
uv run main.py find --file files/sber.txt
```

### Поиск по URL

```bash
uv run main.py find -u https://elma365.com/ru/baza-znaniy/ip/
uv run main.py find --url https://education.yandex.ru/journal/ip-adres
```

### Справка

```bash
uv run main.py --help
uv run main.py find --help
```

## Пример работы

```text
$ python main.py valid 192.168.1.1
'192.168.1.1' — корректный IPv4-адрес.

$ python main.py valid 256.0.0.1
'256.0.0.1' — НЕ является корректным IPv4-адресом.

$ python main.py find -f files/elma365.txt
Найдено уникальных IP-адресов: 14
8.8.8.8
10.0.0.0
77.88.55.88
93.184.216.34
142.250.185.46
172.16.0.0
192.168.0.0
192.168.1.0
192.168.1.1
192.168.1.10
192.168.1.15
192.168.1.2
208.80.154.224
255.255.255.0
```

## Регулярное выражение

В основе лежит шаблон одного октета (числа от 0 до 255):

```regex
(?:2[0-5][0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])
```

**Шаблон для валидации** (вся строка — адрес):

```regex
(?:ОКТЕТ\.){3}ОКТЕТ
```

**Шаблон для поиска** (с границами):

```regex
(?<!\d)(?:ОКТЕТ\.){3}ОКТЕТ(?!\d)
```

### Ключевые моменты

- Порядок альтернатив важен: сначала трёхзначные (250–255, 200–249, 100–199), затем двузначные и однозначные. Если написать `\d{1,3}`, регулярка пропустит `999`.
- `(?<!\d)` — перед адресом не должно быть цифры.
- `(?!\d)` — после адреса не должно быть цифры.
- `re.fullmatch` — для валидации ввода.
- `re.findall` — для поиска в тексте.

## Тестирование

Запуск всех тестов:

```bash
pytest
```


### Что покрыто

- 53 кейса валидации (граничные значения, превышение 255, ведущие нули, неверное количество октетов, посторонние символы).
- 5 офлайн-тестов поиска в текстовых файлах
- 5 сетевых тестов, помеченных
