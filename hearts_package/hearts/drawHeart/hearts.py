from colorama import Fore
from colorama import Style


def draw_heart():
    print(f"{Fore.MAGENTA} :3 {Style.RESET_ALL}")


def emoticon_heart():
    print("\U0001F49C")


def more_hearts(count: int = 3):
    print("\U0001F49E" * count)
