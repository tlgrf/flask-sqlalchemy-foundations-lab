from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Earthquake
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    q = Earthquake.query.get(id)
    if q:
        return jsonify(id=q.id, magnitude=q.magnitude,
                       location=q.location, year=q.year), 200
    return jsonify(message=f"Earthquake {id} not found."), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_by_magnitude(magnitude):
    results = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    quakes = [{
      'id':        e.id,
      'magnitude': e.magnitude,
      'location':  e.location,
      'year':      e.year
    } for e in results]
    return jsonify(count=len(quakes), quakes=quakes), 200

if __name__ == '__main__':
    app.run(port=5555)