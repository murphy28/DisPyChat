# DisPyChat
A very basic python library for creating DisposableChat.com bots.

### Basic Usage
```py
from dispo import DisPyChat

room = {
    "name":"Room",
    "password":""
}

# Additional parameters include the Bot Name, Bot Prefix, and User Agent. Values default to the ones seen in the next line.
# Ex: DisPyChat(room,"DispoBot","!","Disposable Chat Bot")
bot = DisPyChat(room)

bot.message("Hello World!")
```

### Handling Messages
```py
# Logs every new message to the console with the message author.
@bot.onMessage
def onMessage(message,author,id):
  print(f"{author}: {message}")
```

### Change Username
```py
# Changes the bots username to the first word of the latest message.
@bot.onMessage
def onMessage(message,author,id):
  bot.newName(message.split()[0])
```

### Get Users
```py
# Returns an array of users in the chat.
print(bot.getUsers())
```
