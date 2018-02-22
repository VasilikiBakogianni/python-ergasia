import tweepy,json
import collections,re

from tweepy import OAuthHandler

# Identification keys for twitter
consumer_key = 'tM5kw6PxV6QFQBC9HZ2npSNks'
access_token= '2758633369-ZJLmPrEEWQp1GisvheyVefJekVeF0weSXpgaeJQ'
conSec = '3fSt1Vc5HWvjJ0HBXMaDR4HSeInmdmbPRuNbJNhppL2gmmlsXk'
accSec = 'gCDhGmyk93k3hc7yTzJIPhKB5UsyDQlRGSeWJSNCkpLdd'

auth = OAuthHandler(consumer_key, conSec)
auth.set_access_token(access_token, accSec)

api = tweepy.API(auth)
# Check if screen name is valid
while True:
    try:
        screename = (raw_input("What is the screen name of the user you want? "))
        # We only want the last 10 tweets
        txt = " "
        for status in tweepy.Cursor(api.user_timeline, screen_name=screename).items(10):
            txt = txt + " " + status._json['text']
        break
    except Exception:
        print ("\n")
        print("Not a valid screen name.")

# We do not care about the numbers in the tweets
txt = ''.join([i for i in txt if not i.isdigit()])

# Same for special characters
txt = ' '.join(re.sub("(#[A-Za-z0-9]+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())

# Seperate the words using ' '
lst = txt.split(' ')

# Remove u (unicode) we do not need it
lst = [x.encode('ascii', errors='replace') for x in lst]

# We count the number of times each word has appeared
counter = collections.Counter(lst)

# Which word has appeared the most times?
poplr = str((counter.most_common(1)))

# Only characters
poplr = re.sub('[^a-zA-Z]+', '', poplr)

print ("The most popular word among the past ten tweets is: " + poplr + ".")