from application import db
import datetime

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    image = db.Column(db.String, nullable=True)
    track_num = db.Column(db.Integer, nullable=False)

    def __init__(self, title, image = None, track_num=0):
        self.title = title
        if image:
            self.image = self.set_image(image_name=image)
        else:
            self.image = 'No Image'
        self.created_at = datetime.datetime.now()
        self.track_num = track_num

    def set_image(self, image_name):
        return '/original/image?image_title=' + image_name


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    location = db.Column(db.String)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    playlist = db.relationship('Playlist', backref=db.backref('tracks', lazy='dynamic'))

    def __init__(self, title, playlist):
        self.title = title
        self.location = self.set_location(title= title)
        self.playlist = playlist
        playlist.track_num +=1
        db.session.commit()

    def set_location(self, title):
        return '/original/track?track_title=' + title