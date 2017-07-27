from SoundCloudR import db

# class TrackResponse(dict):
#     artwork_url =None
#     title =None
#     artist =None
#     genre =None
#     stream_url = None
#
#     def __init__(self, data):
#         super().__init__()



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