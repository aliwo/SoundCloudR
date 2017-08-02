from application import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    jacket = db.Column(db.String) # 앨범 쟈켓
    def __init__(self):
        pass

class PlayList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    def __init__(self):
        pass