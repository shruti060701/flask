from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask on Railway!"})

if __name__ == '__main__':
    app.run(port=5000)
