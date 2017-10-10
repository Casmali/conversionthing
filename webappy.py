from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template("page1.html")
    

@app.route("/p2")
def render_page2():
    return render_template("page2.html")

@app.route("/response")
def render_response():
    name = request.args['color']
    #The request obj. stores info about the request sent to the server. 
    #The args is a multi dict,(like a doctionary) but it can have multiple values for the same key
    #The info in args is visible in the url for the pages being requested (ex.../response?color=blue)
    if name == 'lavender':
        reply = "That's my favorite color, too"
    else:
            reply = "My favorite color is lavender."
            return render_template('response.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
