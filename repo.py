from flask import Flask, render_template, request
from github import Github
g=Github("fd7a0584744659f660c88d0ce3306362c3e9d9e6")
app=Flask(__name__)
@app.route('/')
def index():
    repositories=g.search_repositories(query='user:deepikaganesan')
    for repo in repositories:
        return repo.url
if __name__=='__main__':
    app.run(debug=True)
