from flask import Flask, jsonify
import sqlite3
from database import init_db

app = Flask(__name__)

@app.route("/levels")
def get_levels():
    conn = sqlite3.connect("water.db")
    c = conn.cursor()
    c.execute("SELECT level,timestamp FROM readings ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()

    return jsonify(rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
