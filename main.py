import argparse
import sys

from src.address import Address
from src.file_repo import FileRepository
from src.url_repo import UrlRepository


def valid_ip(address: str) -> None:
    """Проверяет строку и печатает результат валидации IPv4."""
    try:
        if Address.address_validation(address):
            print(f"'{address}' — корректный IPv4-адрес.")
        else:
            print(f"'{address}' — НЕ является корректным IPv4-адресом.")
    except Exception as e:
        print(f"Ошибка: {e}")


def find_ip_file(path: str) -> None:
    """Ищет IPv4-адреса в файле и печатает их списком."""
    try:
        addresses = sorted(Address.get_all(FileRepository.get_text(path)))
        if addresses:
            print(f"Найдено уникальных IP-адресов: {len(addresses)}")
            for ip in addresses:
                print(ip)
        else:
            print(f"IP-адреса в файле '{path}' не найдены.")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {path}")
    except Exception as e:
        print(f"Ошибка: {e}")


def find_ip_url(url: str) -> None:
    """Ищет IPv4-адреса на веб-странице и печатает их списком."""
    try:
        addresses = sorted(Address.get_all(UrlRepository.get_text(url)))
        if addresses:
            print(f"Найдено уникальных IP-адресов: {len(addresses)}")
            for ip in addresses:
                print(ip)
        else:
            print(f"IP-адреса по URL '{url}' не найдены.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Утилита для валидации и поиска IPv4-адресов"
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    p_valid = subparsers.add_parser('valid', help="Проверить IPv4-адрес")
    p_valid.add_argument('address', type=str, metavar='ADDRESS',
                         help="Строка для проверки, например 192.168.1.1")

    p_find = subparsers.add_parser('find', help="Найти IPv4-адреса в файле или по URL")

    source = p_find.add_mutually_exclusive_group(required=True)
    source.add_argument('-f', '--file', type=str, metavar='PATH',
                        help="Путь к файлу")
    source.add_argument('-u', '--url', type=str, metavar='URL',
                        help="URL веб-страницы")

    args = parser.parse_args()


    if args.command == 'valid':
        valid_ip(args.address)
    elif args.command == 'find':

        if args.file is not None:
            find_ip_file(args.file)
        else:
            find_ip_url(args.url)