import tweepy
import time

auth = tweepy.OAuthHandler('vHLh7jD4v2NJk6vP1OXHdtfhq', 'Zllc3qgTpvXDFx8b6noUp6glzYStRVYNbGtXN8nqF2EWbBVReh')
auth.set_access_token("3304451160-sWbtkoYWXdcbISAxUeOdJGruvih4VAJI9E6gFku", 'JFjo0PHKWEeeL0GJCTotBAjOfah00znVdNxOGKHSBnLyq')

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
