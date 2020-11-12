import sentry_sdk
from flask import Flask, jsonify, request
from datetime import date
from flask_restful import Resource, Api
from app.api.search import Search
from app.api.tv_shows import Top250
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://95ce977722294eae9055d6af5a69b111@o475339.ingest.sentry.io/5513251",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def __init__(self):
        pass

    def get(self):
        return jsonify({
            'status': True,
            'date': str(date.today().strftime("%b-%d-%Y")),
            'docs': 'https://chauhannaman98.github.io/IMDb-API/',
            'api-services-available': {
                'Search by title': request.base_url+'search?stype=title&q=Titanic',
                'Search by name': request.base_url+'search?stype=name&q=Jim',
                'Top25 TV Shows': request.base_url+'tv-shows/top250',
            }
        })


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


api.add_resource(Home, '/')
api.add_resource(Search, '/search', endpoint='search')
api.add_resource(Top250, '/tv-shows/top250', endpoint='top250')

if __name__ == '__main__':
    app.run(debug=True)