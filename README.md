## README



### Quickstart :rocket::rocket:

```
pip install -r requirements.txt
```



```python
"""
    Example of batch processings
"""

videos = [{
    "video_id": "iYmm3dDkaIs",
    "artist": "Laika",
    "year":  2016
}]

from tubify import get_video_as_mp3, tag_mp3_file, splice_audio

for video in videos:
    video_id = video["video_id"]
    artist = video["artist"]
    year = video["year"]
    print("Downloading video as mp3 {}".format(video_id))
    video_title = get_video_as_mp3(video_id)
    print("Tagging MP3 {}".format(video_id))
    tag_mp3_file(
        "{}.mp3".format(video_title),
        video_id, video_title,
        artist,
        year
    )

"""
    Examples of slicing
"""
videos = [{
    "video_id": "iYmm3dDkaIs",
    "artist": "Laika",
    "year":  2016,
    "start": "00:00:00",
    "end": "00:00:10"
}]
for video in videos:
    video_id = video["video_id"]
    artist = video["artist"]
    year = video["year"]
    print("Downloading video as mp3 {}".format(video_id))
    video_title = get_video_as_mp3(video_id)
    print("Tagging MP3 {}".format(video_id))
    tag_mp3_file(
        "{}.mp3".format(video_title),
        video_id, video_title,
        artist,
        year
    )
    splice_audio(
        "{}.mp3".format(video_title),
        start=video["start"],
        end=video["end"]
    )
```



### Design Ideas

Wrapping the API underneath a CLI for faster access or even Alfred hotkey workflows

