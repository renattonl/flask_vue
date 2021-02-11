from flask import Flask
from flask_restful import Resource, Api, abort
import uuid
import json
from datetime import datetime, timezone

app = Flask(__name__)
api = Api(app)


def generate_uuid():
    identifier = uuid.uuid4()
    return json.dumps(identifier, default=str)


def get_utc_now():
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    return json.dumps(now, default=str)


MEASUREMENTS = [
    {
        "id": "654646546546",
        "sys": 120,
        "dia": 80,
        "pul": 70,
        "created": get_utc_now(),
        "user_id": "65465465465465465"
    },
    {
        "id": "7574635453453",
        "sys": 170,
        "dia": 90,
        "pul": 70,
        "created": get_utc_now(),
        "user_id": "2345647656768"
    },
]


class Measurement(Resource):
    def get(self, id):
        for measurement in MEASUREMENTS:
            if id == measurement.get('id'):
                return measurement, 200
        abort(404, message=f'Measurement ID={id} was not found')


api.add_resource(Measurement, "/v1/measurements/<string:id>")

if __name__ == "__main__":
    app.run(debug=True)
