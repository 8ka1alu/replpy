from flask import Flask
from threading import Thread
import discord

app = Flask(__name__)

@app.route("/")
def main():
  return discord.__version__

def run():
  app.run("0.0.0.0", port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
