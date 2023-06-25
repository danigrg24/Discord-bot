import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def containsBadWords(message) -> bool:
    p_message = message.lower()
    f = open("bad_words.txt", "r")
    badWords = f.read().split("\n")

    wordsInMessage = p_message.split(" ")
    for word in wordsInMessage:
        if(word in badWords):
            return True
        
    f.close()
    return False

def chooseRandomPHF() -> str:
    return random.choice(["piatra", "hartie", "foarfeca"])

def chooseRandomDiceScore() -> int:
    return random.randint(1, 12)

def chooseRandomPacanele() -> str:
    possibile = [":grapes:", ":lemon:", ":cherries:", ":melon:", ":crown:", ":seven:", ":gem:", ":star:"]
    return (random.choice(possibile) + " " + random.choice(possibile) + " " + random.choice(possibile) + random.choice(possibile) + " " + random.choice(possibile) +
            "\n" + random.choice(possibile) + " " + random.choice(possibile) + " " + random.choice(possibile) + random.choice(possibile) + " " + random.choice(possibile) +
            "\n" + random.choice(possibile) + " " + random.choice(possibile) + " " + random.choice(possibile) + random.choice(possibile) + " " + random.choice(possibile))

def getMeme(user_message) -> str:
    text = user_message.split("meme pls")[1]
    text0 = text.split(" sau ")[0]
    text1 = text.split(" sau ")[1]
    url = ("https://api.imgflip.com/caption_image?text0=" + text0 + "&text1=" + text1 + 
           "&username=" + os.environ["IMGFLIP_USERNAME"] + "&password=" + os.environ["IMGFLIP_PASSWORD"] + "&template_id=181913649")
    print(url)
    response = requests.get(url)
    data = response.json()
    return data["data"]["url"]
