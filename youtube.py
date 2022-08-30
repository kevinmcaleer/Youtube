from secret import api_key

from googleapiclient.discovery import build

# youtube = build('youtube', 'v3', developerKey=api_key)

# stats = youtube.channels().list(part='id, snippet', forUsername='kevinmcaleer28').execute()

# print(stats)

import urllib
import json

def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request(url)
       
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links

vid_list = get_all_video_in_channel('UCuoS-cgppnO46VCcQi81jvQ')
print(vid_list)
