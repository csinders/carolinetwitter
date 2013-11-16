import os
import time
from twitter import * 
from flask import Flask, request, render_template, redirect, abort, flash, jsonify
import json

app = Flask(__name__)  #create our flask app 

CONSUMER_KEY = "ZOWPlakwCO2Xa8rgEvornw"
CONSUMER_SECRET = "aNoDIKBmNkLqeXh5lJYcazhNRMgj7Mc1EJBZyOcCQA8"
OAUTH_TOKEN = "22389244-C4xVthVea0N3uMnJ5JdomjJcPJQwZ7ILQIBxJufhR"
OAUTH_SECRET = "GGvKIjvEaQJeOrgdSEvswVSt21d0ttcOmxuPTucqU3SgM"

#configure Twitter API
twitter = Twitter(auth= OAuth (OAUTH_TOKEN, OAUTH_SECRET,
					CONSUMER_KEY, CONSUMER_SECRET))


@app.route('/<username>')
def main(username=''):

	usertweets = get_user_tweets(username)
	sort_tweets_by_day(usertweets)
	templateData = {
		'tweets' : json.dumps(usertweets, indent=2)
	}
	return render_template('index.html', **templateData)




def get_user_tweets(username):
	return twitter.statuses.user_timeline(screen_name=username)


def sort_tweets_by_day(tweets):
	tweetsPerDate = {}

	for tweet in tweets: 
		tweet_day = tweet["created_at"].split(' ')[0]

		#create the key for the day if it don't exist 
		if tweet_day not in tweetsPerDate:
				tweetsPerDate[tweet_day] = []

		#add that tweet to the list of tweets for that day 
		tweetsPerDate[tweet_day].append(tweet)

	print([ (x,len(tweetsPerDate[x])) for  x in tweetsPerDate ])

	

#let's start the server, yo!
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)
