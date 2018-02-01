import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__) 
app.secret_key = os.environ["SECRET_KEY"];

highscore = 0


@app.route('/',methods=['GET','POST'])
def render_main():
    reply=""
    if 'symbol' in request.args:
        reply="oh"
        name = request.args['symbol']
        if name == 'Mr.Snuffleupagus':
            reply = "Correct"
        else:
            reply = "Incorrect"
    return render_template('home.html')
   

@app.route('/page1', methods=['GET','POST'])
def render_page1():
    correct = 0
    reply=["","","","","","","",""]
    if 'first' in request.form:
        name = request.form['first']
        if name == 'Mr.Snuffleupagus':
            reply[0] = "Correct"   
            correct = correct + 1
        else:
            reply[0] = "Incorrect: the answer was Mr. Suffleupagus"      
    if 'second' in request.form:
        name = request.form['second']
        if name == 'Aloysius Snuffleupagus':
            reply[1] = "Correct"
            correct = correct + 1
        else:
            reply[1] = "Incorrect: the answer was Aloysius Snuffleupagus"  
    if 'third' in request.form:
        name = request.form['third']
        if name == 'August 19th':
            correct = correct + 1
            reply[2] = "Correct"   
        else:
            reply[2] = "Incorrect: the answer was August 19th"
    if 'fourth' in request.form:
        name = request.form['fourth']
        if name == 'Eternally 4 1/2 years old ':
            correct = correct + 1
            reply[3] = "Correct"   
        else:
            reply[3] = "Incorrect: the answer was Eternally 4 1/2 years old"
    if 'fifth' in request.form:
        name = request.form['fifth']
        if name == ' Big Bird':
            correct = correct + 1
            reply[4] = "Correct"   
        else:
            reply[4] = "Incorrect: the answer was Big Bird"
    if 'sixth' in request.form:
        name = request.form['sixth']
        if name == ' tbd':
            correct = correct + 1
            reply[5] = "Correct"   
        else:
            reply[5] = "Incorrect: the answer was tbd"
    if 'seventh' in request.form:
        name = request.form['seventh']
        if name == 'Senor Snuffalapogo':
            correct = correct + 1
            reply[6] = "Correct"   
        else:
            reply[6] = "Incorrect: the answer was Senor Snuffalapogo"
    if 'eighth' in request.form:
        name = request.form['eighth']
        if name == 'ALOYSIUS SNUFFLEUPAGUS.':
            correct = correct + 1
            reply[7] = "Correct"   
        else:
            reply[7] = "Incorrect: the answer was ALOYSIUS SNUFFLEUPAGUS."
    global highscore
    if correct >= highscore:
        highscore = correct
    session["highScore"] = highscore
    session["numCorrect"] = correct
    return render_template('page1.html', re1 = reply[0], re2 = reply[1], re3 = reply[2], re4 = reply[3], re5 = reply[4], re6 = reply[5], re7 = reply[6], re8 = reply[7])
    
    

@app.route('/page2',methods=['GET','POST'])
def render_page2():
#     reply=""
#     if 'symbol' in request.args:
#         name = request.args['symbol']   
#         if name == 'carbon':
#              reply = "C"
#         elif name == 'sulfur':
#              reply = "S"            
    return render_template('page2.html')
    
    
if __name__=="__main__":
    app.run(debug=False)
