from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
# def render_main():
#     reply=""
#     if 'symbol' in request.args:
#         reply="oh"
#         name = request.args['symbol']
#         if name == 'Mr.Snuffleupagus':
#             reply = "Correct"
#         else:
#             reply = "Incorrect"
   
    return render_template('home.html')
   

@app.route("/page1")
def render_page1():
    reply=""
    if 'first' in request.form:
        name = request.form['first']
        if name == 'Mr.Snuffleupagus':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was Mr. Suffleupagus"      
    if 'second' in request.form:
        name = request.form['second']
        if name == 'Aloysius Snuffleupagus':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was Aloysius Snuffleupagus"  
     if 'third' in request.form:
        name = request.form['third']
        if name == 'August 19th':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was August 19th"
      if 'fourth' in request.form:
        name = request.form['fourth']
        if name == 'Eternally 4 1/2 years old ':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was Eternally 4 1/2 years old"
      if 'fifth' in request.form:
        name = request.form['fifth']
        if name == ' Big Bird':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was Big Bird"
      if 'sixth' in request.form:
        name = request.form['sixth']
        if name == ' tbd':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was tbd"
      if 'seventh' in request.form:
        name = request.form['seventh']
        if name == 'Senor Snuffalapogo':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was Senor Snuffalapogo"
    if 'eighth' in request.form:
        name = request.form['eighth']
        if name == 'ALOYSIUS SNUFFLEUPAGUS.':
             reply = "Correct"   
        else:
             reply = "Incorrect: the answer was ALOYSIUS SNUFFLEUPAGUS."
    return render_template('page1.html', response = reply)
    
    

@app.route("/page2")
# def render_page2():
#     reply=""
#     if 'symbol' in request.args:
#         name = request.args['symbol']   
#         if name == 'carbon':
#              reply = "C"
#         elif name == 'sulfur':
#              reply = "S"            
    return render_template('page2.html')
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
