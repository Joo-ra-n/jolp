from flask import Flask
import findust
import time

app = Flask(__name__)

@app.route('/')
def index():
    findust.create_table()
    # while (True):
    findust.insert_data()
    time.sleep(5)

    return ('hello world')

if __name__ == "__main__":
    app.run()