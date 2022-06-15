import socket # для соединения
from colorama import init, Fore

# несколько цветов
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port):
    """
    определяем, имеет ли `хост` открытый `порт`
    """
    # создаем новый сокет
    s = socket.socket()
    try:
        # попытка присоединения к хосту через порт
        s.connect((host, port))
        # установите таймаут для чуть большей скорости
        #s.settimeout(0.2)
    except:
        # соединение не установлено, порт открыт!
        # возвращает false
        return False
    else:
        # соединение установлено, порт открыт!
        return True

# адрес сайта вводит пользователь
host = input("Enter the host:")
# итерация по пртам , из диапазона от 1 до 1024
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} открыт      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} закрыт    {RESET}", end="\r")

