from colorama import Fore, Style
from time import sleep
for c in range(10, -1, -1):
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '{:^10}'.format(c))
    sleep(1)
print(Style.BRIGHT + Fore.YELLOW + '{:^10}'.format('!BOOM!'))
