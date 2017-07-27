
class Track(dict): # 곡 하나를 Track 객체로 표현.
    kind =  None
    id = None
    created_at = None
    user_id = None
    last_modified = None
    genre = None
    title = None
    description = None
    uri = None
    artwork_url = None
    stream_url = None
    track_json = None

    def __init__(self, track_json):
        super().__init__()
        #Track Json 객체를 파싱해서 갖는다.
        self.kind = track_json.get('kind', 'null')
        self.id = str(track_json.get('id', 'null'))
        self.created_at = track_json.get('created_at', 'null')
        self.user_id = track_json.get('user_id', 'null')
        self.last_modified = track_json.get('last_modified', 'null')
        self.genre = track_json.get('genre', 'null')
        self.title = track_json.get('title', 'null')
        self.description = track_json.get('description', 'null')
        self.uri = track_json.get('uri', 'null')
        self.artwork_url = track_json.get('artwork_url', 'null')
        self.stream_url = track_json.get('stream_url', 'null')
        self.track_json = track_json

    def get_stream_url(self, client):
        track = client.get('/tracks/' + self.id)
        stream_url = client.get(track.stream_url, allow_redirects=False)
        return stream_url.location
        # stream_url.location은 playlist로 얻어온 json 파일에는 들어있지 않다. 어디서 가져오는진 모르곘지만 바로 재생 가능.