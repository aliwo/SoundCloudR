from flask import request, jsonify, redirect, send_from_directory, url_for

from OriginalUnit import uploader
import OriginalUnit.playlist
from SoundCloudUnit import Account, Playlist, soundcloud
from application import application
import config


@application.route('/')
def hello_world():
    return 'Hello! <br> if you have any question, please send email to <br> aliwo@naver.com'

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
            return 'invalid command'
            #TODO: invalid 관련 에러 페이지 만들기

@application.route('/stream', methods=['GET'])
def get_stream_url():
    pass #TODO: 로직 짜기
    #soundcloud.get_stream_url()


@application.route('/original/playlist', methods=['GET', 'POST', 'DELETE'])
def original_playlist():
    if request.method== 'POST':
        if request.form.get('secret') == config.ADMIN_SECRET:
            return OriginalUnit.playlist.make_playlist()
        else:
            return 'you shall not pass'

    if request.method == 'GET':
        playlist = OriginalUnit.playlist.get_playlist(request.args.get('playlist_title'))
        if playlist:
            return jsonify(playlist)
        else:
            return 'invalid title'

    if request.method == 'DELETE':
        title = request.args.get('playlist_title')
        playlist = OriginalUnit.playlist.delete_playlist(title)
        if playlist:
            playlist.title+' deleted'
        else:
            return 'no playlist found name:'+title


@application.route('/original/playlists', methods=['GET'])
def original_playlists():
    if request.method == 'GET':
        playlists = OriginalUnit.playlist.get_playlists()
        return jsonify(playlists)


@application.route('/original/track', methods=['GET', 'POST'])
def upload_file():
    if request.method== 'GET':
        track_title = str(request.args.get('track_title'))
        track_title = uploader.secure_filename(track_title)
        return send_from_directory(config.TRACKS_SHIPMENT_FOLDER,
                            track_title)
        #return uploader.upload_UI(application.config['UPLOAD_FOLDER'], application.config['SHIPMENT_FOLDER'])
    if request.method== 'POST':
        return OriginalUnit.playlist.add_tracks()

@application.route('/original/image', methods=['GET', 'POST'])
def uploaded_image():
    if request.method == 'GET':
        image_name = str(request.args.get('image_title'))
        return send_from_directory(config.IMAGES_SHIPMENT_FOLDER,
                                   image_name)
    if request.method == 'POST':
        return  OriginalUnit.playlist.add_image()
        #TODO: 이미 있는 플레이리스트에 이미지 추가하기 기능.

'''send_from)directory는 자신이 호출된 views.py를 무조건 기본 디렉터리로 사용하는
 지랄 맞은 알고리즘을 가지고 있기 때문에, config[] 에서 send_from_directory 전용의 SHIPMENT 경로를
 만들었습니다. 실제적으로 UPLOAD_FOLDER와 SHIPMENT_FOLDER는 같은 디렉터리를 가리킵니다.
'''