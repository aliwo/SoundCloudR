import soundcloud, requests

class SoundCloudAPIAccount:
    client_id = None
    client_name = None
    client = None
    api_id = 'jDtJOucgyacN8CELJ8vR3vJ4KuDwcTGQ'
    api_secret = 'PTlD6rjotNUi3En6Eo4Ctrxyho4PqSWk'

    def __init__(self):
        self.client = soundcloud.Client(
            client_id='jDtJOucgyacN8CELJ8vR3vJ4KuDwcTGQ',
            client_secret='PTlD6rjotNUi3En6Eo4Ctrxyho4PqSWk',
            username='reborn@inu.ac.kr',
            password='young4ever')

        self.client_id = str(self.client.get('/me').id)
        self.client_name = self.client.get('/me').username

    def get_playlists(self):
        uri = 'https://api.soundcloud.com/users/' + self.client_id + '/playlists'
        payload = {'client_id': self.api_id}
        playlists = requests.get(uri, params=payload)
        return playlists
