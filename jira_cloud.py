from flask import Flask, render_template, request
from jira_core import jira_list_request, login_pass
import time
import re

app = Flask(__name__)
@app.route("/")

def index():
    title = "Jira List"
    jira_list = jira_list_request()
    empty = ['']
    if login_pass != empty:
        return render_template('index.html', page_title=title,jira_list=jira_list)
    else:
        return render_template('auth.html', page_title=title)

if __name__ == "__main__":
    app.run(debug = True)

#jira.add_worklog("TEST1-1", timeSpent="2h")