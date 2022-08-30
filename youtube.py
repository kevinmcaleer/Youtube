from webbrowser import get
import scrapetube
from pprint import pprint
import yaml

videos = scrapetube.get_channel("UCuoS-cgppnO46VCcQi81jvQ", sort_by="newest")
x=-1

yaml_file = open("youtube.yaml", "w")

yaml_content = []


def get_video_info(videos):
    print("Getting video info...")
    for video in videos:
        video_id = str(video['videoId'])
        title = str(video['title']['runs'][x+1]['text'].replace("/","//").replace('-',',').replace(' ,',',')).replace('!',".")
        views = str(video['viewCountText']['simpleText'].replace(" views",""))
        published = str(video['publishedTimeText']['simpleText'])
        yaml_content.append({'title':title, 'view':views, 'published':published,'video_id':video_id})

    yaml.dump(yaml_content, yaml_file, default_flow_style=False)
    yaml_file.close()

get_video_info(videos)
print("youtube.yaml file created")