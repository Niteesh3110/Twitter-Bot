import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('')

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = 'Hello'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked this tweet')

	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
