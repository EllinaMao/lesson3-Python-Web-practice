from colorama import init, Fore

init(autoreset=True)

def line(name = ""):
    print (Fore.LIGHTBLUE_EX + 10*"-" + name + 10*"-")