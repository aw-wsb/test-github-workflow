from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    your_name = "Adrian"
    return render_template('hello.html', name=your_name)
=======
 return '<h1>Hello WSB! Greetings from Flask & Docker!</h1>'
if __name__ == "__main__":
 app.run(debug=True)
>>>>>>> b98ed1f974cbbe668c3bc001d0e1c5cd059ded4a
