class Playlist:
    playlist_json = None
    tracks = None

    def __init__(self, playlist_json):
        self.playlist_json = playlist_json
        self.tracks = playlist_json.get('tracks')

    def get_permalink_url(self):
        permalink_url = self.playlist_json.get('permalink_url', '')
        return permalink_url