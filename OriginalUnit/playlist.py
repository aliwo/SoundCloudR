from flask import request
from application import models
from OriginalUnit import uploader
import config


def make_playlist():
    title =  request.form.get('title')
    image_name = uploader.upload_file(config.IMAGES_UPLOAD_FOLDER, 'image')
    tracks = uploader.upload_file_arrays(config.TRACKS_UPLOAD_FOLDER, 'tracks[]')
    if title:
        track_names = []
        for track in tracks:
            track_names.append(uploader.secure_filename(track.filename))
        #track_names가 만들어진 후에야 playlist가 만들어지고, playlist가 만들어지고 나서야 track 객체가 만들어질 수 있다.
        #TODO: 나중에 더 효율적으로 리펙토링 해보기
        if image_name:
            playlist = models.Playlist(title=title, image=image_name)
        else:
            playlist = models.Playlist(title=title, track_num=len(track_names))
        models.db.session.add(playlist)

        for name in track_names:
            track = models.Track(title = name, playlist= playlist)
            models.db.session.add(track)

        models.db.session.commit()
        return 'playlist: '+ title +' created'
    else:
        return 'invalid title'


def get_playlists():
    playlists = models.Playlist.query.limit(10).all()

    playlists_array = []
    for playlist in playlists:
        tracks_array = []
        for track in playlist.tracks:
            track_json = {
                'title': track.title
                , 'location': track.location
            }
            tracks_array.append(track_json)

        playlist_json = {
            'title': playlist.title
            , 'image' : playlist.image
            , 'tracks' : tracks_array
        }
        playlists_array.append(playlist_json)

    return playlists_array

def get_playlist(playlist_title):
    playlist = models.Playlist.query.filter_by(title=playlist_title).first()
    if playlist:
        tracks = models.Track.query.filter_by(playlist_id = playlist.id).all()

        tracks_array = []

        for track in tracks:
            track_json = {
                'title': track.title
                ,'location' : track.location
            }
            tracks_array.append(track_json)

        json = {
            'title': playlist.title
            , 'image' : playlist.image
            , 'created_at' : playlist.created_at
            , 'tracks' : tracks_array
        }
        return json
    else:
        return None

def delete_playlist(playlist_title):
    playlist = models.Playlist.query.filter_by(title=playlist_title).first()
    if playlist:
        #play list에 연관된 음악, 이미지를 서버에서 싸그리 지워야 함.
        #이후 db에서도 지워야 함.

        #TODO: 만약 음악 파일은 그냥 지워버리면, 다른 플레이리스트와 공유하는 경우에 문제가 생김.

        config.os.remove(config.application_dir)

        models.db.session.remove(playlist)

        return playlist
    else:
        return None


def add_image():
    playlist_title = request.form.get('title')
    image_name = uploader.upload_file(config.IMAGES_UPLOAD_FOLDER, 'image')
    if image_name:
        playlist = models.Playlist.query.filter_by(title = playlist_title).first()
        if playlist:
            playlist.set_image(image_name=image_name)
            models.db.session.commit()
            return 'image '+ image_name +' set'
        else:
            return'invalid playlist name'
    else:
        return 'invalid image name'

def add_tracks():
    playlist_title = request.form.get('title')
    tracks = uploader.upload_file_arrays(config.TRACKS_UPLOAD_FOLDER, 'tracks[]')
    playlist = models.Playlist.query.filter_by(title=playlist_title).first()

    if playlist:
        for track in tracks:
            track = models.Track(title= uploader.secure_filename(track.filename), playlist= playlist)
            models.db.session.add(track)

        models.db.session.commit()
        return 'new tracks added'
    else:
        return 'invalid playlist title'









