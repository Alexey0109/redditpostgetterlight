import praw
import random
import telebot

#token = '966351011:AAGDUmgrpOfujpT5flyRlOn26Li-_U8f7Dg'
#Testbot token
token = '1138014823:AAG_GE3uqcakQaoGa3K6kV4c_nQJgo7hz58'
bot = telebot.TeleBot(token)

subreddit = None

def getPosts(sub):
    app_id = 'Vlu73kg2jM6Ueg'
    secret = 'YB7yFBbo67SlXo44x9hNG7Ae0Kc'
    reddit = praw.Reddit(client_id=app_id,
                     client_secret=secret,
                     user_agent='testscript')
    print(reddit)
    i = 0
    urls = {}
    for submission in reddit.subreddit(sub).new(limit=25):
        urls[i] = submission
        i += 1
    n = random.randint(0, 25)
    if n == 25: n - 1
    print(n, end=': ')
    print(urls[n])
    return urls[n]

content_filter = None

@bot.message_handler(content_types=['text'])
def GetSub(message):
    try:
        subreddit = message.text[1:]
        bot.send_message(message.chat.id, "Please, wait...")
        post = getPosts(subreddit)
        post_url = post.url
        bot.send_message(message.chat.id, post_url)
    except Exception as e:
        bot.send_message(message.chat.id, "Seems like no such subreddit")
        print(e)
bot.polling()