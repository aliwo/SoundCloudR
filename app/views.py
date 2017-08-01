from app import application, soundcloud
from flask import request, jsonify, redirect
from SoundCloudUnit import Account, Playlist,Track
import json
import datetime


@application.route('/')
def hello_world():
    return 'Hello World!'

@application.route('/playlist', methods=['POST', 'GET'])
def get_playlist():
    if request.method == 'GET': #플레이리스트를 반환합니다.
        account = Account.SoundCloudAPIAccount()
        playlists = account.get_playlists()
        playlist_json = soundcloud.get_playlist_json(playlists=playlists, option=request.args.get('command', ''))
        if playlist_json:
            playlist = Playlist.Playlist(playlist_json=playlist_json)
            tracks = soundcloud.get_tracks(playlist, account)
            return jsonify(tracks)
        else:
            return 'invalid command' #TODO: 에러 코드를 담아서 response를 보내야함... 혹은 다른 방식으로 처리할지 손코딩 해보기

    if request.method == 'POST': #플레이리스트를 서버에 만듭니다.
        pass



@application.route('/stream', methods=['GET'])
def get_stream_url():
    pass #TODO: 로직 짜기
    #soundcloud.get_stream_url()
