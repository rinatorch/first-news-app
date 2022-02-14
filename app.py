from flask import Flask
from flask import render_template
app = Flask(__name__)

#this is a decorator
@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
