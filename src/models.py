from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False, unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "active": self.active,
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    char_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    epi_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    loc_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    def serialize(self):
        return {
            "id": self.id,
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    char_named = db.Column(db.String(250), nullable=False, unique=True)
    char_img = db.Column(db.String(250), nullable=False, unique=True)
    char_content = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "char_named": self.char_named,
            "char_img": self.char_img,
            "char_content": self.char_content,
        }

class Charuser(db.Model):
    __tablename__ = 'charuser'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    char_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    char = db.relationship(Character)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "char_id": self.char_id,
        }

class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, primary_key=True)
    epi_name = db.Column(db.String(250), nullable=False, unique=True)
    epi_img = db.Column(db.String(250), nullable=False, unique=True)
    epi_content = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "char_name": self.char_name,
            "char_img": self.char_img,
            "char_content": self.char_content,
        }


class Epiuser(db.Model):
    __tablename__ = 'epiuser'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    epi_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    epi = db.relationship(Episode)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "epi_id": self.epi_id,
        }


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    loc_name = db.Column(db.String(250), nullable=False, unique=True)
    loc_img = db.Column(db.String(250), nullable=False, unique=True)
    loc_content = db.Column(db.String(250), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "loc_name": self.loc_name,
            "loc_img": self.loc_img,
            "loc_content": self.loc_content,
        }



class Locuser(db.Model):
    __tablename__ = 'locuser'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    loc_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    loc = db.relationship(Location)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "loc_id": self.loc_id,
        }


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@