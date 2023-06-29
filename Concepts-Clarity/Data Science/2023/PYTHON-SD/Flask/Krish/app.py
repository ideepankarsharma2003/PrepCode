from flask import Flask

app= Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my youtube channel'

if __name__=='main':
    app.run()