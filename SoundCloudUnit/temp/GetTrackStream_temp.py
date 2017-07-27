import soundcloud
import SoundCloudUnit.Account
#Track (곡 하나)을 가져오는 예제입니다.

# create a client object with your app credentials
client = soundcloud.Client(client_id=SoundCloudUnit.Account.SoundCloudAPIAccount.api_id)

# fetch track to stream
track = client.get('/tracks/323204279')

# get the tracks streaming URL
stream_url = client.get(track.stream_url, allow_redirects=False)

# print the tracks stream URL
print (stream_url.location)
#stream_url.location은 playlist로 얻어온 json 파일에는 들어있지 않다. 어디서 가져오는진 모르곘지만 바로 재생 가능.