from flask import Flask, render_template, request
from jira_core import jira_list_request
import time
import re

app = Flask(__name__)
@app.route("/")

def index():
    title = "Jira List"
    jira_list = jira_list_request()
    return render_template('index.html', page_title=title,news_list=jira_list)


if __name__ == "__main__":
    app.run(debug = True)



#projects = jira.projects()
#projects
#print(projects)
#issue = jira.issue('TEST1-1')
#jira.add_worklog("TEST1-1", timeSpent="2h")
#issues_in_prj = jira.search_issues('project=TEST1')
#print(type(issues_in_prj))
#all_prj_issues_but_mine = jira.search_issues('project=TEST1 and assignee != currentUser()')
#all_prj_issues_but_mine




