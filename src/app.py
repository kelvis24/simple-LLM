from flask import Flask, render_template, jsonify, request
import random  # Import random module

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-greeting', methods=['POST'])
def get_greeting():
    data = request.json
    message = data.get('message', '')
    
    # Generate a random greeting response
    greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!", "What's up?", "Howdy!", "Good day!"]
    
    return jsonify(greeting=random.choice(greetings))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
