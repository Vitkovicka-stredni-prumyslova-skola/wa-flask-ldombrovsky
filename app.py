from flask import Flask, render_template

#import meho blueprintu z modulu general
from general.general import general_bp

app = Flask(__name__)

app.register_blueprint(general_bp)




#@app.route ("/")
#def home():
#    return render_template("index.html")