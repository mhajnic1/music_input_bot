import requests
import time


with open(r"C:\Users\MH\Desktop\Projekti\DiscordBots\PlayMusic\music.txt", "r") as music:
	lines = music.readlines()

pjesma = []

for l in lines:
    as_list = l.split("\n")
    pjesma.append(as_list[0])  

for k in pjesma:
    url = "https://discord.com/api/v9/channels/942845010896900146/messages"

    payload = {
            "content" : "p!Play " + k
        }

    headers = {
            "Authorization" : "MzA4Mzk4Mjk5MjI2OTYzOTY4.Gaw_8V.Fete7q0U-hrQJjzJUtoucvaf8yrwiPeCWmIAso"
        }

    res = requests.post(url, payload, headers = headers)

    time.sleep(1)