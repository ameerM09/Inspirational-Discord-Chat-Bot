from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')

def menu():
  return 'Hello! I am still online and ready to encourage!'

def run():
  app.run(host='0.0.0.0', port=8080)

def online():
  thr = Thread(target=run)
  thr.start()
