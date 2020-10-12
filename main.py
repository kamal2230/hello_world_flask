from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World. Good Evening.</h1>"

if __name__ == '__main__':
    app.run()
