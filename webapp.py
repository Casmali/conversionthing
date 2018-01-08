from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    reply=""
    if 'symbol' in request.args:
        reply="ohguhftydtyf yhfhtftyfytictu"
        name = request.args['symbol']
        if name == 'sodium':
            reply = "Na"
        elif name == 'hydrogen':
            reply = "Hey"""
        elif name == 'hgen':
            reply = "hwllo"""
    return render_template('home.html', response = reply)
   

@app.route("/page1")
def render_page1():
    reply=""
    if 'symbol' in request.args:
        name = request.args['symbol']
        if name == 'gold':
             reply = "Au"   
        elif name == 'lithium':
             reply = "Li"       
    return render_template('page1.html', response = reply)
    
    

@app.route("/page2")
def render_page2():
    reply=""
    if 'symbol' in request.args:
        name = request.args['symbol']   
        if name == 'carbon':
             reply = "C"
        elif name == 'sulfur':
             reply = "S"            
    return render_template('page2.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
