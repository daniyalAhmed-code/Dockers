from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis = Redis(host=os.getenv('Host'), port=int(os.getenv('Port')),
              password=os.getenv('PASSWORD'))


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
