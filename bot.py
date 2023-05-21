# - 채널 만들기
import telegram
import schedule
import time
import datetime
import pytz

token = ""
bot = telegram.Bot(token)
public_chat_name = "@ktest2022"


def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    
    else :
        text=('alarm : '+str(now))
        bot.sendMessage(chat_id = public_chat_name, text = text).chat_id
        #print("current time = ", str(now))

schedule.every(30).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(30)
    

# # id_channel = bot.sendMessage(chat_id = public_chat_name, text = "alarm").chat_id
# print(id_channel)

""" def job():
    now_local = datetime.datetime.now()
    now_local_time = now_local.strftime("%Y-%m-%d %H:%M:%S")
    
    # 특정 시간 회피
    if now_local.strftime("%H") >= "23" or now_local.strftime("%H") <= "6":
        pass
    bot.sendMessage(chat_id=chat_id, text=('지금은 ' + str(now_local_time) + ' 야'))

schedule.every(0).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1) """