#!/usr/bin/env python3

import os
import time
import random
from rich import print
from pyfiglet import figlet_format

# 🎬 MATRIX EFFECT
def matrix():
    os.system("clear")
    chars = "01"
    print("[green]Initializing Matrix Mode...[/green]\n")

    for _ in range(20):
        line = "".join(random.choice(chars) for _ in range(60))
        print("[green]" + line + "[/green]")
        time.sleep(0.05)

# 💻 FAKE HACKING SCREEN
def fake_hack():
    os.system("clear")
    print("[red]Accessing Secure Server...[/red]")
    
    steps = [
        "Connecting to server...",
        "Bypassing firewall...",
        "Injecting payload...",
        "Access granted!",
        "Downloading data...",
        "Cleaning traces..."
    ]

    for step in steps:
        print("[green]" + step + "[/green]")
        time.sleep(1)

    print("\n[red]Hack Complete 😈[/red]")
    time.sleep(2)

# 🎬 LOADING
def loading():
    os.system("clear")
    print("[green]Booting DarkSys...[/green]")
    for i in range(5):
        print("[green].[/green]", end="")
        time.sleep(0.4)
    print("\n")

# 🧠 BANNER
def banner():
    os.system("clear")
    print("[green]" + figlet_format("DarkSys") + "[/green]")
    print("[cyan]>> MATRIX EDITION <<[/cyan]")
    print("[yellow]Developed by Jugnu[/yellow]\n")

# ⚙️ SYSTEM FUNCTIONS
def system_info():
    os.system("uname -a")

def cpu_info():
    os.system("top -n 1")

def ram_info():
    os.system("free -h")

def disk_info():
    os.system("df -h")

def network_info():
    os.system("ip a")

# 🎯 MAIN MENU
def main():
    matrix()
    fake_hack()
    loading()

    while True:
        banner()
        print("[green]1.[/green] System Info")
        print("[green]2.[/green] CPU Info")
        print("[green]3.[/green] RAM Info")
        print("[green]4.[/green] Storage Info")
        print("[green]5.[/green] Network Info")
        print("[blue]6.[/blue] Run Matrix Again")
        print("[red]0.[/red] Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            cpu_info()
        elif choice == "3":
            ram_info()
        elif choice == "4":
            disk_info()
        elif choice == "5":
            network_info()
        elif choice == "6":
            matrix()
        elif choice == "0":
            print("[red]Exiting DarkSys...[/red]")
            time.sleep(1)
            break
        else:
            print("[red]Invalid Option![/red]")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
