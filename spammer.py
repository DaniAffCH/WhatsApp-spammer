from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import selenium.common.exceptions
import os

def header():
    color = {
        "purple": '\033[0;35m',
        "blue": '\033[0;34m',
        "reset": '\033[0m'
    }
    print("""
 """+color["purple"]+""" _      __"""+color["reset"]+color["blue"]+"""   __         __                                  """+color["purple"]+"""____"""+color["reset"]+color["blue"]+"""
 """+color["purple"]+"""| | /| / /"""+color["reset"]+color["blue"]+"""  / /  ___ _ / /_  ___ ___ _   ___    ___        """+color["purple"]+"""/ __/"""+color["reset"]+color["blue"]+"""   ___  ___ _  __ _   __ _  ___   ____
 """+color["purple"]+"""| |/ |/ /"""+color["reset"]+color["blue"]+"""  / _ \/ _ `// __/ (_-</ _ `/  / _ \  / _ \      """+color["purple"]+"""_\ \ """+color["reset"]+color["blue"]+"""   / _ \/ _ `/ /  ' \ /  ' \/ -_) / __/
 """+color["purple"]+"""|__/|__/"""+color["reset"]+color["blue"]+"""  /_//_/\_,_/ \__/ /___/\_,_/  / .__/ / .__/     """+color["purple"]+"""/___/"""+color["reset"]+color["blue"]+"""   / .__/\_,_/ /_/_/_//_/_/_/\__/ /_/
                                """+color["blue"]+"""       /_/    /_/                /_/

"""+color["purple"]+"""
 ▄▄▄▄ ▓██   ██▓   ▓█████▄  ▄▄▄       ███▄    █  ██▓ ▄▄▄        █████▒ █████▒▄████▄   ██░ ██
▓█████▄▒██  ██▒   ▒██▀ ██▌▒████▄     ██ ▀█   █ ▓██▒▒████▄    ▓██   ▒▓██   ▒▒██▀ ▀█  ▓██░ ██▒
▒██▒ ▄██▒██ ██░   ░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒██  ▀█▄  ▒████ ░▒████ ░▒▓█    ▄ ▒██▀▀██░
▒██░█▀  ░ ▐██▓░   ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░██▄▄▄▄██ ░▓█▒  ░░▓█▒  ░▒▓▓▄ ▄██▒░▓█ ░██
░▓█  ▀█▓░ ██▒▓░   ░▒████▓  ▓█   ▓██▒▒██░   ▓██░░██░ ▓█   ▓██▒░▒█░   ░▒█░   ▒ ▓███▀ ░░▓█▒░██▓
░▒▓███▀▒ ██▒▒▒     ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░ ▒ ░    ▒ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒
▒░▒   ░▓██ ░▒░     ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░ ░      ░       ░  ▒    ▒ ░▒░ ░
 ░    ░▒ ▒ ░░      ░ ░  ░   ░   ▒      ░   ░ ░  ▒ ░  ░   ▒    ░ ░    ░ ░   ░         ░  ░░ ░
 ░     ░ ░           ░          ░  ░         ░  ░        ░  ░              ░ ░       ░  ░  ░
      ░░ ░         ░                                                       ░
"""+color["reset"]+"""
    """)

def question(quest):
    print(str(quest)+"[y/n]")
    ans = input()
    return True if ans == "y" else False

def loadDriver():
    #travis support
    options = Options()
    options.headless = True

    print("Loading gecko driver...")
    if ('TRAVIS' in os.environ):
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Firefox()
    print("Done")
    return driver

def login(driver):
    try:
        driver.find_element(By.XPATH, "//canvas[@aria-label='Scan me!']")
        print("Please scan QR Code to login into WhatsApp Web")
        if ('TRAVIS' not in os.environ):
            while (True):
                try:
                    driver.find_element(By.XPATH, "//canvas[@aria-label='Scan me!']")
                except selenium.common.exceptions.NoSuchElementException:
                    print("User logged")
                    break

    except selenium.common.exceptions.NoSuchElementException:
        print("User logged")

def setVictim(driver):
    print("Enter name of victim (emojis must be included too): ")
    victim = input()
    try:
        search = driver.find_element(By.XPATH, "//div[@class='_1awRl copyable-text selectable-text'][@data-tab='3']")
        search.click()
        search.send_keys(victim)
        driver.find_element(By.XPATH, "//span[@title='"+victim+"']")
        search.send_keys(Keys.RETURN)

    except selenium.common.exceptions.NoSuchElementException:
        print("Victim not found, try again")
        driver.find_element(By.XPATH,"//button[@class='_3Wrfs']").click()
        setVictim(driver)

def attack(driver):
    print("Enter Spam Message : ")
    msg = input()
    print("Number of times it will be sent: ")
    while True:
        n = int(input())
        if (n>0):
            break
        print("Invalid number of times, try again")

    if question("START ATTACK?"):
        try:
            text_field = driver.find_element(By.XPATH,"//div[@class='_1awRl copyable-text selectable-text'][@data-tab='6']")
            for i in range(n):
                print("Sent "+str(i)+" messages")
                text_field.send_keys(msg)
                text_field.send_keys(Keys.RETURN)

            print("Done!")
        except Exception as e:
            print(e.__class__)
            print("ERROR!")

if __name__ == "__main__":
    header()
    driver = loadDriver()
    print("Loading WhatsApp Web")
    driver.get("https://web.whatsapp.com/")
    login(driver)
    if ('TRAVIS' not in os.environ):
        while True:
            setVictim(driver)
            attack(driver)
            if not question("Do you wanna attack again?"):
                break
