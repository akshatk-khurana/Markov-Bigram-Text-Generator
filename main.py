IN_FILE_PATH = "frequencies.json"

from flask import Flask, jsonify
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

@app.route("/word-generation-api/<number>", methods=["GET"])
def generate_words(number):

    words = None
    freq = None
    with open(IN_FILE_PATH, "r") as f:
        freq = json.loads(f.read())
        words = list(freq.keys())

    text = [random.choice(words)]

    for i in range(int(number)-1):
        possibilities = freq[text[-1]]["ORDERED"]
        next_word = None

        if len(possibilities) == 0:
            next_word = random.choice(words)
        else:
            possibilities = iter(possibilities)

            for word in possibilities:
                next_word = word
                if next_word not in text:
                    break

        text.append(next_word)

    return jsonify({"text" : " ".join(text),
                    "words" : text})

# API url http://127.0.0.1:5000/word-generation-api/10