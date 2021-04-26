## README



### Quickstart :rocket::rocket:

```
pip install -r requirements.txt
```



```python
from tubify import get_video_as_mp3, tag_mp3_file

video_id = "iYmm3dDkaIs"

video_title = get_video_as_mp3(video_id)
tag_mp3_file(
    "{}.mp3".format(video_title),
    video_id, "Laika",
    "Boston Manor",
    2016
)
```



### Design Ideas

Wrapping the API underneath a CLI for faster access or even Alfred hotkey workflows

