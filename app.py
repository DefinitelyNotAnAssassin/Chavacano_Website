from flask import * 
import sqlite3
from flask_socketio import SocketIO, emit, join_room, leave_room





conn = sqlite3.connect("words.db")
c = conn.cursor()

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on("receiver")
def handle(text):
  print(text)
  temptext = text["msg"].split()
  translatedwords = []
  
  for i in temptext:
    conn = sqlite3.connect("words.db")
    c = conn.cursor()
    search = "SELECT * FROM chavacanowords WHERE filipinoword = ? OR filipinoword = ? OR filipinoword LIKE ? OR filipinoword LIKE ?"
    search = """SELECT chavacanoword
FROM (
  SELECT *, 1 AS exactmatch
  FROM chavacanowords 
  WHERE filipinoword = ? OR filipinoword = ?
  UNION ALL
  SELECT *, 0 AS exactmatch
  FROM chavacanowords 
  WHERE filipinoword LIKE ? OR filipinoword LIKE ?
) m
ORDER BY exactmatch DESC
LIMIT 1"""
    
    c.execute(search, (i, i.title(), '%'+i+'%', '%'+i.title()+'%'))
    result = c.fetchone()
    if result:
      translatedwords.append(result[0])
    else:
      translatedwords.append(i)
  
  print(temptext)
  result = ' '.join(translatedwords)
  print(result)
  emit('translate', result.lower())


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/translate")
def translate():
  return render_template("translate.html")

if __name__ == "__main__":
  socketio.run(app, debug = True)