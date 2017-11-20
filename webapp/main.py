from flask import Flask, render_template, jsonify
import sparql
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getData/<int:requestid>')
def getData(requestid):
    
    query = 'query' + str(requestid)
    data = sparql.get_query_results(query)

    stateData = [['State', 'Count']]
    for dataPoint in data['results']['bindings']:
        data_count = int(dataPoint['data_count']['value'])
        state = dataPoint['state_name']['value']
        dpArray = [state, data_count]
        stateData.append(dpArray)
    statedataJson = json.dumps(stateData)
    print(statedataJson)
    return jsonify(statedataJson)


@app.route('/getChartData')
def getChartData():

    data = sparql.get_query_results('query5')

    stateData = [['Restaurant Count', 'Population Count', { 'role': 'annotation' }]]
    for dataPoint in data['results']['bindings']:
        rest_count = int(dataPoint['restaurent_count']['value'])
        popcount = int(dataPoint['18_plus_pop']['value'])
        state = dataPoint['state']['value']
        dpArray = [rest_count, popcount, state]
        stateData.append(dpArray)
    statedataJson = json.dumps(stateData)
    return jsonify(statedataJson)


@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
