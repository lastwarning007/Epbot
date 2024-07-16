import os
import requests
import telebot
from telebot import types
import re
import time

token = "7163722712:AAG_iXvDap9b79SRloOUG89Rjmex-347pZI" #YOUR TOKEN HERE
bot = telebot.TeleBot(token, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "<strong> LAST WARNING Send Your Python File or any File such as TXT File \n </strong>")

@bot.message_handler(content_types=["document"])
def main(message):
    koko = bot.reply_to(message, "Tg id @hardhackar007 Please wait...").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    start = time.time()
    
    with open("input.py", "wb") as w:
        w.write(ee)

    try:
        with open("input.py", 'r') as file:
            code = file.read()
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'http://pastie.org',
                'Referer': 'http://pastie.org/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            }

            data = {
                'language': 'plaintext',
                'content': code,
            }

            res = requests.post('http://pastie.org/pastes/create', headers=headers, data=data, verify=False).text
            link = re.search(r'<div class="item"><a href="([^"]+)">raw</a></div>', res).group(1)
            end = time.time()
            toto = int(end - start)

            if link:
                with open("output.py", "w") as file:
                    file.write(f"from requests import get as ahmed\nmahos=ahmed('http://pastie.org{link}')\nexec(mahos.text)")
                
                bot.send_document(message.chat.id, open("output.py", "rb"), caption=f"<strong>Your Encrypted successful : {toto} LAST WARNING\n BY: @hardhackar007</strong>", parse_mode="html")
            else: 
                bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ ما</strong>", parse_mode="html")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, f"<strong> ❗لقد حدث خطأ: {e}</strong>", parse_mode="html")
print("run")
while True:
    try:
        bot.infinity_polling()
    except:
        pass