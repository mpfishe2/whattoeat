from flask import Flask, request, jsonify, render_template
from libraries.helper import loadEnvVariables
from libraries.formatters import format_recipe
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    openai.api_key = loadEnvVariables()
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=message,
      max_tokens=4000
    )
    # TODO: not sure if this is really doing anything to better format the text
    if "recipe" in message:
        return jsonify(format_recipe(response.choices[0].text.strip()))
    else:
        return jsonify(response.choices[0].text.strip())

@app.route('/api/save', methods=['POST'])
def save():
    message = request.json['message']
    with open('bot_replies.txt', 'a') as file:
        file.write(message + '\n')
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)