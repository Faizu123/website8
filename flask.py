from flask_frozen import Freezer
from myapplication import app

freezer = Freezer(app)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == '__main__':
    freezer.freeze()