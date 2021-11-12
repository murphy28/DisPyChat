from dispo import DisPyChat 
import json, requests, time

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)

bot = DisPyChat(config["room"],config["botname"],config["prefix"],config["userAgent"])

bot.message("DispoBot Successfully started, do '!help' for a list of commands!")

count = 0

def chuckNorris():
    return json.loads(requests.get("https://api.chucknorris.io/jokes/random").text)["value"]

def tronaldDump():
    return json.loads(requests.get("https://api.tronalddump.io/random/quote").text)["value"]

@bot.onMessage
def onMessage(message,author,id):
    if author != bot.botname:
        if message[0] == bot.prefix:
            command = message[1:].split()
            if command[0] == "ping":
                bot.message("Pong.")
            elif command[0] == "help":
                bot.message("List of commands:")
                time.sleep(0.01)
                bot.message("!ping - Bot test command, always returns pong.")
                time.sleep(0.01)
                bot.message("!count - Adds 1 to the chat count. Purely for fun.")
                time.sleep(0.01)
                bot.message("!chuck - Retrieve a random Chuck Norris joke.")
                time.sleep(0.01)
                bot.message("!trump - Retrieve a random Donald Trump quote.")
            elif command[0] == "count":
                global count
                count+=1
                bot.message("Current Count: " + str(count))
            elif command[0] == "chuck":
                bot.message(chuckNorris())
            elif command[0] == "trump":
                bot.message(tronaldDump())
