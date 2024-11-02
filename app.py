from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, world"

@app.route("/say_hi")
def say_hello():
  return "Hi"

if __name__ == "__main__":
  app.run(debug=True)