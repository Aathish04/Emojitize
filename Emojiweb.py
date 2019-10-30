
#All My Imports
from flask import Flask, render_template, request
from EmojitizeScript import emojitize as emojitize
import re
import emoji


app = Flask(__name__)

#The actual Website
@app.route('/', methods = ['POST', "GET"]) #The websites url is / and the features ill use are POST and GET
def Emojiweb(): #Make a function Emojiweb
    if request.method != "POST": #If nothing is requested from the site.
        return render_template("Emojiweb.html") #Just show the regular site
    if request.method == "POST": #if something is requested
        textIN = request.form['TextIn'] #Get the text that was written in the textbox
        return render_template("Emojiweb.html", EmojisOut = emojitize(textIN), TextIN = textIN) # and return the website, but with the output and input

if __name__ == '__main__':
   app.run()