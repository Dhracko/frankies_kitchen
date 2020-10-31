# Module error pages
from flask import render_template
from app import app


# 404 page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 410 page

@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410


# 500 page

@app.errorhandler(500)
def page_not_found(e):
    return render_template('410.html'), 500

