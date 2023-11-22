import requests
import time
import random
# Specify the path to your input file
file_path = r"path to txt file with music choices"

# Read the lines from the file
with open(file_path, "r") as music:
    lines = music.readlines()

# Remove leading and trailing whitespaces from each line
pjesma = [line.strip() for line in lines]

# Specify the Discord bot API endpoint
url = "message url"

# Specify the Discord bot authorization token
headers = {
    "Authorization": "authorisation code"
}

# Loop through each song and send a play command to the bot
for song in pjesma:
    payload = {
        "content": "test is " + song
    }

    res = requests.post(url, payload, headers=headers)
    print(payload)
    # Generate a random waiting time between 1.5 and 4 seconds
    wait_time = random.uniform(1.5, 4.0)
    time.sleep(wait_time)
