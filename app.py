from flask import Flask, render_template, request, redirect, url_for
# Flask: main class, render_template for HTML file in index file, request: que te dejá ver the data from server, redirect: to a diff URL
# url_for: for redirect

import database #database_fn

app= Flask(__name__)  #app object

@app.before_request
def initialize():
    init_db()
