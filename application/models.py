from application import db
import datetime

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    image = db.Column(db.String, nullable=True)
    track_num = db.Column(db.String, nullable=False)

    def __init__(self, title, image, track_num=0):
        self.title = title
        self.image = image
        self.created_at = datetime.datetime.now()
        self.track_num = track_num

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    location = db.Column(db.String)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    playlist = db.relationship('Playlist', backref=db.backref('tracks', lazy='dynamic'))

    def __init__(self, title, location, playlist):
        self.title = title
        self.location = location
        self.playlist = playlist