#app.py

from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', method=['POST'])
def addTodo():
    #access body information


if __name__ == "__main__":
    app.run(debug=True)







#GET, PUT, POST, DELETE
#GET and DELETE
#CRUD CREATE, RETRIEVE, UPDATE, DELETE