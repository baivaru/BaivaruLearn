import requests
import telegram
import json
import time

#get the token from t.me/botfather - command is /newbot
bot_token = 'xxxxx:xxxxxxxx'

#get your user id via t.me/myidbot - command is /getid
user_id = 'xxxxx'

bot = telegram.Bot(token=bot_token)

while True:
    #calling api via requests package and getting the response as a json object
    req = requests.get('https://api.chucknorris.io/jokes/random').json()
    
    #getting the 'value' field from the request response
    joke = req['value']

    #send the message to your chat
    bot.send_message(chat_id = user_id, text = joke)

    #wait 120 seconds before running it again, since while loop it will run again
    time.sleep(120)