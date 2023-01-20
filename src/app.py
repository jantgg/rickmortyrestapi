"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Favorite, Location, Charuser, Episode, Epiuser, Locuser
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_all_Users():
    users = User.query.all()
    users_serialized = [x.serialize() for x in users]
    return jsonify({"body": users_serialized}), 200


@app.route('/characters', methods=['GET'])
def get_all_characters():
    characters = Character.query.all()
    characters_serialized = [x.serialize() for x in characters]
    return jsonify({"body": characters_serialized}), 200

@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    favorites = Favorite.query.all()
    favorites_serialized = [x.serialize() for x in favorites]
    return jsonify({"body": favorites_serialized}), 200

@app.route('/episodes', methods=['GET'])
def get_all_episodes():
    episodes = Episode.query.all()
    episodes_serialized = [x.serialize() for x in episodes]
    return jsonify({"body": episodes_serialized}), 200

@app.route('/locations', methods=['GET'])
def get_all_locations():
    locations = Location.query.all()
    locations_serialized = [x.serialize() for x in locations]
    return jsonify({"body": locations_serialized}), 200

@app.route('/charusers', methods=['GET'])
def get_all_charusers():
    charusers = Charuser.query.all()
    charusers_serialized = [x.serialize() for x in charusers]
    return jsonify({"body": charusers_serialized}), 200

@app.route('/epiusers', methods=['GET'])
def get_all_epiusers():
    epiusers = Epiuser.query.all()
    epiusers_serialized = [x.serialize() for x in epiusers]
    return jsonify({"body": epiusers_serialized}), 200

@app.route('/locusers', methods=['GET'])
def get_all_locusers():
    locusers = Loc_user.query.all()
    locusers_serialized = [x.serialize() for x in locusers]
    return jsonify({"body": locusers_serialized}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
