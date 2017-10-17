from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    reply=""
    if 'symbol' in request.args:
        #name = request.args['symbol']
        #The request obj. stores info about the request sent to the server. 
        #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
        #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
        if name == 'sodium':
            reply = "Na"
    
        elif name == 'hydrogen':
            reply = "H"
            
            
    return render_template('home.html', response = reply)
   

@app.route("/page1")
def render_page1():
  
    name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if name == 'gold':
        reply = "Au"
    
    elif name == 'lithium':
        reply = "Li"
            
            #reply = "My favorite color is lavender."
    return render_template('page1.html', response = reply)
    
    

@app.route("/page2")
def render_page2():
    
    name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if name == 'carbon':
        reply = "C"
    
    elif name == 'sulfur':
        reply = "S"
            
            #reply = "My favorite color is lavender."
    return render_template('page2.html', response = reply)
    
    

    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
