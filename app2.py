from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
    return '<h1> Wasim is owmer of MAnipulator </h1> \
    Pakistan zina bad'
@app.route('/about')
def index2():
    return """ ther are other share holders as well \n
     our talent and skills are multi dimensinal \r
     our teams are our  our biggest asset \
      they make difference and impact which others can't"""


app.run(debug=True)