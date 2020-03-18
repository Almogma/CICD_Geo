'''
Authors: Almog Mahluf - 205490170
         Alon Gabay   - 2080646080
         Michael Elisha - 316904978
'''
import os
from time import sleep
from src.geo_class import Geo


def clear():
    sleep(3)
    os.system('clear')


def close():
    print("program has been closed")
    sleep(1)
    exit(0)


def main():
    while True:
        print("""
        1. check ip details 
        2. check dns details
        3. exit
        """)

        menu = input()

        switcher = {
            1: lambda x: Geo.input_location("ip"),
            2: lambda x: Geo.input_location("dns"),
            3: lambda x: close(),
        }
        switcher.get(int(menu))(0)


if __name__ == "__main__":
    main()
