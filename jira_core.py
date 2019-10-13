from jira import JIRA
from flask import Flask, render_template, request
import re

jira = JIRA('https://lp14jcloud.atlassian.net/', basic_auth=('madhape@yandex.ru', 'oeljsEIFSFZy9lgvbuKDF237'))
def radio(id):
    onclick = f"printResult('{id}')"
    body = f'input type="radio" name="task" id="{id}" onclick={onclick}'
    return f'<{body}>'
def jira_list_request():
    jira_list = []
    jira_list_uf = jira.search_issues('project=TEST1')
    for issue in jira_list_uf:
        jira_time = int(issue.fields.timespent / 3600)
        jira_list.append({
            'Key':issue.key, 
            'Name': issue.fields.summary, 
            'Creator':issue.fields.creator.displayName, 
            'Time':jira_time, 
            'Radio':radio(issue.key)
        })
    return jira_list
print(jira_list_request())
#help(jira_list_request().fields)