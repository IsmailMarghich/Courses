from flask import Flask, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def hello_world():
    return 'Runescape is the best game'

if __name__ == "__main__":
    app.run(debug=True)
