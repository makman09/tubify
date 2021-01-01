## README



### Thoughts

```python
from tubify import get_video_as_mp3, tag_mp3_file

video_id = "racmy7Y9P4M"

title = get_video_as_mp3(video_id)

tag_mp3_file(
    "{}.mp3".format(title),
    video_id, "Parasite Eve",
    "Bring Me The Horizon",
    2020
)
```