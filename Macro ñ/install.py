import json
import winshell
import shutil
import os.path
import colorama
import os

os.system("title installing macro...")

colorama.init()

startup = winshell.startup()
file_exists = os.path.exists('macro.pyw')

def main():
    with open('./config.json') as js:
        config = json.load(js)

    startUp = config.get('startUpWithWindows')

    if startUp == True:
        print('Your program will start with windows (config.json)')
        print(f'Moving program to {startup}...')
        if file_exists:
            shutil.move(f'macro.pyw', f'{startup}/macro.pyw')
            input(f"{colorama.Fore.GREEN}Program successfully installed, you can close this window")

        else:
            input(f"{colorama.Fore.RED}ERROR: Program already installed, or you moved / renamed any file")

main()