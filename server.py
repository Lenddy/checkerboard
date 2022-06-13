from flask import Flask,render_template
app = Flask(__name__)

@app.route("/checkerboard")
def checkerboard():
    return  render_template("index.html",first_name = "Lenddy") 


if  __name__ == "__main__":
    app.run(debug= True)