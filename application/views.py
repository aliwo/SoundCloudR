from flask import request, jsonify, redirect, send_from_directory, url_for

from OriginalUnit import uploader
from SoundCloudUnit import Account, Playlist, soundcloud
from application import application


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

@application.route('/stream', methods=['GET'])
def get_stream_url():
    pass #TODO: 로직 짜기
    #soundcloud.get_stream_url()


@application.route('/original/track', methods=['GET', 'POST'])
def upload_file():
    if request.method== 'GET':
        return uploader.upload_UI(application.config['UPLOAD_FOLDER'])
    if request.method== 'POST':
        filename = uploader.upload_file(application.config['UPLOAD_FOLDER'])
        return redirect(url_for('uploaded_file', filename=filename))

@application.route('/original/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(application.config['SHIPMENT_FOLDER'],
                               filename)
'''send_from)directory는 자신이 호출된 views.py를 무조건 기본 디렉터리로 사용하는
 지랄 맞은 알고리즘을 가지고 있기 때문에, config[] 에서 send_from_directory 전용의 SHIPMENT 경로를
 만들었습니다. 실제적으로 UPLOAD_FOLDER와 SHIPMENT_FOLDER는 같은 디렉터리를 가리킵니다.
'''