from SoundCloudUnit import Playlist, Track
import requests, json

host = 'https://api.soundcloud.com'

#admin 계정에서 playlists 목록을 반환

def get_playlist_json(playlists, option):
    #playlists는 request 객체임.
    json_arr = json.loads(playlists.text) # JSON ARRAY로 파싱.
    playlist = None
    if option =='most_recent':
        playlist = json_arr[0] # 가장 최근 플레이리스트를 가져옵니다.
    elif option == 'last_time':
        playlist = json_arr[1] #저번에 틀었던 걸 가져옵니다.

    return playlist

#플레이리스트의 SoundCloud 페이지 주소를 반환.
