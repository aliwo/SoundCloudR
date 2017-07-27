from SoundCloudR import application, soundcloud
from flask import request, jsonify, redirect
from SoundCloudUnit import Account, Playlist,Track


@application.route('/')
def hello_world():
    return 'Hello World!'

@application.route('/playlist', methods=['POST', 'GET'])
def get_playlist():
    command = request.args.get('command', '')
    account = Account.SoundCloudAPIAccount()
    playlists = account.get_playlists()
    playlist = Playlist.Playlist(playlist_json = soundcloud.get_playlist_json(playlists=playlists, option=command))
    #TODO: playlist가 비어서 돌아올 경우 예외처리와 함께 client error 코드를 보내야 함.

    tracks = playlist.tracks
    track_stream_urls = ''
    track_list = [] # 이걸 리턴할 수 잇는지도 시험해보기
    for track_json in tracks:
        track = Track.Track(track_json=track_json)
        track_list.append(track)
        track_stream_urls += str(track.get_stream_url(account.client))+' '

    return track_stream_urls

@application.route('/stream', methods=['GET'])
def get_stream_url():
    pass #TODO: 로직 짜기
    #soundcloud.get_stream_url()
