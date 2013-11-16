import os
import time
from twitter import * 
from flask import Flask, request, render_template, redirect, abort, flash, jsonify

app = Flask(__name__)  #create our flask app 

#configure Twitter API
twitter = Twitter(auth=OAuth(os.environ.get('OAUTH_TOKEN'), os.environ.get('OAUTH_SECRET'),
						os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))

	)

@app.route('/')
def main():

	return render_template('index.html')




#let's start the server, yo!
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)
