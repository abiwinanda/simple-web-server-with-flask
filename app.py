from flask import Flask

# initialize the app
app = Flask(__name__)

# create a root route
@app.route('/')
def hello_world():
    return "Hello World!"

app.run(port=5000,   # run the webserver or app on port 5000
        debug=False) # set debug = True when you are in development environment
