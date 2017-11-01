from flask import Flask, render_template
import sparql


app = Flask(__name__)


@app.route('/')
def index():
    data = sparql.get_query_results()

    return render_template('index.html', data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
