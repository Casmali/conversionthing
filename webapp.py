from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/home")
def render_home():
    name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if symbol == 'sodium':
        reply = "Cl"
    
    elif symbol == 'hydrogen':
        reply = "H "
            
            #reply = "My favorite color is lavender."
    return render_template('response.html', response = reply)
   

@app.route("/p1")
def render_page1():
    name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if symbol == 'gold':
        reply = "Au"
    
    elif symbol == 'lithium':
        reply = "Li"
            
            #reply = "My favorite color is lavender."
    return render_template('response.html', response = reply)
    
    

@app.route("/p2")
def render_page2():
    name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if symbol == 'carbon':
        reply = "C"
    
    elif symbol == 'sulfur':
        reply = "S"
            
            #reply = "My favorite color is lavender."
    return render_template('response.html', response = reply)
    
    


#@app.route("/response")
#def render_response():
    #name = request.args['symbol']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    #if symbol == 'gold':
     #   reply = "Au"
    
    #elif:symbol == 'lithium;"
        
        #reply = "Li"
            
            #reply = "My favorite color is lavender."
            #return render_template('response.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
