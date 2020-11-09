from flask import Flask
import finedust
import time

app = Flask(__name__)

@app.route('/')
def index():
    findust.create_table()
    findust.insert_data()

    return ('hello world')

if __name__ == "__main__":
    app.run()