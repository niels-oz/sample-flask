# coding: latin-1

from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

generations = [
    {
        'name': 'Lost Generation',
        'from': 1883,
        'until': 1900

    },
    {
        'name': 'WW2 Generation',
        'from': 1901,
        'until': 1927

    },
    {
        'name': 'Silent Generation',
        'from': 1928,
        'until': 1945

    },
    {
        'name': 'Baby Boomers',
        'from': 1946,
        'until': 1964

    },
    {
        'name': 'Generation X',
        'from': 1965,
        'until': 1980

    },
    {
        'name': 'Generation Y / Millenials',
        'from': 1981,
        'until': 1996

    },
    {
        'name': 'Generation Z',
        'from': 1997,
        'until': 2012

    },
    {
        'name': 'Generation Alpha',
        'from': 2013,
        'until': 2024
    },
    {
        'name': 'Generation Beta',
        'from': 2025,
        'until': 2039
    },
]


@app.route("/")
def hello_generations():
    return '<p>Hello Generations!</p>'


@app.route('/api/v1.0/generations/<int:year>', methods=['GET'])
def get_generation(year):
    generation = [gen for gen in generations if gen['from'] <= year <= gen['until']]
    if not generation:
        abort(404)  # generation not found
    return jsonify({'generation': generation[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Generation not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int('5000'), debug=True)
