import tweepy
import re
from key import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
screen_name_list = []

class Listener(tweepy.Stream):
    global screen_name_list
    def on_status(self, status):
        if status.author.screen_name in screen_name_list and re.match("^RT @", status.text) == None and status.in_reply_to_status_id == None:
            if not status.favorited:
                api.create_favorite(status.id)
#           if not status.retweeted:
#               api.retweet(status.id)
    
def get_user_id_list():
    global screen_name_list
    screen_name_list = open('./screen_name.list', 'r').read().split('\n')
    screen_name_list = list(filter(lambda s: len(s), screen_name_list))
    user_id_list = []
    for screen_name in screen_name_list:
        user = api.get_user(screen_name=screen_name)
        user_id_list.append(user.id)
    return user_id_list

if __name__ == '__main__':
    user_id_list = get_user_id_list()
    listener = Listener(consumer_key, consumer_secret, access_token, access_token_secret)
    listener.filter(follow=user_id_list)


