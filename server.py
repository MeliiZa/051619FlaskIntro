"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          <p>What compliment would you like?</p>
          <p><input type="radio" name="compliment" value="awesome">Awesome<br>
          <input type="radio" name="compliment" value="cute">Cute<br>
          <input type="radio" name="compliment" value="smart">Smart<br>
          <input type="radio" name="compliment" value="funny">Funny<br>
          <input type="radio" name="compliment" value="beautiful">Beautiful<br></p>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def insult_person():
  """Insults the user, its not nice, but it was in the instructions ¯_(ツ)_/¯ """
    # player = request.args.get("person")

    # insult = request.args.get("insult")

  return """
    <!doctype html>
    <html>
      <head>
        <title>I will insult you ¯_(ツ)_/¯</title>
      </head>
      <body>
      You are a....
        
        
      </body>
    </html>
    """

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
