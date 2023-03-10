import os

import openai
from flask import Flask, redirect, render_template, request, url_for,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
openai.api_key = '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'


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt= generate_prompt(animal),
            temperature=1.0,
            stop=None,
            max_tokens=1024,
            
        )
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt= generate_prompt('animal'),
        temperature=1.0,
        stop=None,
        max_tokens=1024,
    )
    return jsonify(response)

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return animal
    
