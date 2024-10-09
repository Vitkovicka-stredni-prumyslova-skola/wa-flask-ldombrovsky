from flask import Flask, render_template, Blueprint


general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    statuc_folder='static')

@general_bp.route('/')
def home():
    return render_template("index.html")