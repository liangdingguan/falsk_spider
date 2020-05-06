from flask import Flask
import re

app=Flask(__name__)

@app.route('/')
def index():

    with open('index.html','r') as  f:
        content=f.read()

    return content


app.run()




