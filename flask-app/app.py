from flask import Flask, render_template
import random
app = Flask(__name__)
images = ["https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif","https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif"]
@app.route('/')
def index():
    return render_template('index.html', url=random.choice(images))
app.run(host="0.0.0.0")
