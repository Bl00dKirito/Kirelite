import os

import tts
import profile

import telepot

if profile.data['telegram'] == 'y':
    def handle(msg):
        chat_id = msg['chat']['id']
        username = msg['chat']['username']
        command = msg['text'].lower().replace("'", "")

        if username == profile.data['telegram_username']:
            print(profile.data['ai_name'] +
                  " thinks you said '" + command + "'")
            return command
        else:
            error_msg = 'You are not authorised to use this bot.'
            bot.sendMessage(chat_id, error_msg)

        bot = telepot.Bot('386105162:AAFxrABBZO-eL2EVUQ_SyTMN1H-0wITHy30')
        bot.notifyOnMessage(handle)

        while True:
            time.sleep(10)
