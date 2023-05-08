from flask import Flask, render_template, request
import sqlalchemy as db

def searchdd(serchText):
    select_query = db.select(portfolio).where(portfolio.columns.title == serchText)
    select_result = connection.execute((select_query))
    searchRepositories =select_result.fetchall()
    if len(searchRepositories) ==0:
        select_query = db.select(portfolio).where(portfolio.columns.link == serchText)
        select_result = connection.execute((select_query))
        searchRepositories = select_result.fetchall()
    return searchRepositories


app = Flask(__name__)

try:
    engine = db.create_engine('mysql+pymysql://root:ason121245@localhost:3306/my_database')
    connection = engine.connect()
    print("Connect DB")
except Exception as ex:
    print("ERROR Connect DB")
    print(ex)

metadata = db.MetaData()
portfolio = db.Table('developers_portfolio', metadata,
                 db.Column('developers_portfolio_id', db.Integer, primary_key=True),
                 db.Column('title', db.Text),
                 db.Column('link', db.Text))

metadata.create_all(engine)

insertion_query = portfolio.insert().values([
    {"title":"Google Kubernetes", "link":"https://github.com/kubernetes/kubernetes"},
    {"title":"Apache Spark", "link":"https://github.com/apache/spark"},
    {"title":"Microsoft Visual Studio Code", "link":"https://github.com/Microsoft/vscode"},
    {"title":"NixOS Package Collection", "link":"https://github.com/NixOS/nixpkgs"},
    {"title":"Rust", "link":"https://github.com/rust-lang/rust"},
    {"title":"Firehol IP Lists", "link":"https://github.com/firehol/blocklist-ipsets"},
    {"title":"Red Hat OpenShift", "link":"https://github.com/openshift/origin"},
    {"title":"Ansible", "link":"https://github.com/ansible/ansible"},
    {"title":"Automattic WordPress Calypso", "link":"https://github.com/Automattic/wp-calypso"},
    {"title":"Microsoft .NET CoreFX", "link":"https://github.com/dotnet/corefx"},
    {"title":"Microsoft .NET Roslyn", "link":"https://github.com/dotnet/roslyn"},
    {"title":"Node.js", "link":"https://github.com/nodejs/node"},
    {"title":"TensorFlow", "link":"https://github.com/tensorflow/tensorflow"},
    {"title":"freeCodeCamp", "link":"https://github.com/freeCodeCamp/freeCodeCamp"},
    {"title":"Space Station 13", "link":"https://github.com/tgstation/tgstation"}
])
#connection.execute(insertion_query)

selall = db.select(portfolio)
selres = connection.execute(selall)
allListRepositories = selres.fetchall()

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get('clear') =='Clear':
            d = searchdd("s")
            return render_template('index.html', allListRepositories=d, len=len(d))
        elif request.form.get('all') =='All List':
            render_template('index.html' , allListRepositories = allListRepositories, len = len(allListRepositories))
        elif request.form.get('searchBtn') == 'Search':
            a = request.form.get("search")
            d = searchdd(a)
            return render_template('index.html' , allListRepositories = d, len = len(d))
    return render_template('index.html' , allListRepositories = allListRepositories, len = len(allListRepositories),sum = sum)

if __name__ == '__main__':
    app.run(debug=True, port=5001 )




