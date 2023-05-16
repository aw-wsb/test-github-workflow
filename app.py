<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello WSB! Greetings from Flask!</h1>'
if __name__ == "__main__":
=======
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello WSB! Greetings from Flask!</h1>'
if __name__ == "__main__":
>>>>>>> f7aa38272327614277e5232a6f373649e8b7f08d
 app.run(debug=True)