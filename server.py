from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/dojo")
def dojo():
    return "dojo"


@app.route("/say/flask")
def say_flask():
    return "Hi Flask"


@app.route("/say/michael")
def say_michael():
    return "Hi Michael"


@app.route("/say/john")
def say_John():
    return "Hi John"


@app.route("/repeat/hello/<int:number>")
def repeat_hello(number):
    print(number)
    return " Hello " * number


@app.route("/repeat/bye/<int:number>")
def repeat_bye(number):
    print(number)
    return " bye " * number


@app.route("/repeat/dogs/<int:number>")
def repeat_dogs(number):
    print(number)
    return " dogs " * number


if __name__ == "__main__":
    app.run(debug=True)
