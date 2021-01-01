import eyed3
import re
import subprocess
import urllib3

VIDEO_ID = "WeUf6hYGvqM"


def get_video_as_mp3(video_id, path_prefix=""):
    """

    """
    cmd_arr = [
        "youtube-dl",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "-o",
        "%(title)s.%(ext)s",
        "https://youtu.be/{}".format(VIDEO_ID)
    ]

    youtube_dl_cmd = subprocess.run(cmd_arr, stdout=subprocess.PIPE, text=True)

    if youtube_dl_cmd.returncode == 0:
        regex = r"(\[ffmpeg\]\sDestination:\s)([\s\S]*)(.mp3)"
        matches = re.search(regex, youtube_dl_cmd.stdout).groups()
        prefix, title, extension = matches

        return title
    else:
        raise Exception(youtube_dl_cmd.stderr)




def get_video_thumbnail(video_id):
    """

    """
    url = "https://img.youtube.com/vi/{}/hqdefault.jpg".format(VIDEO_ID)

    http = urllib3.PoolManager()
    response = http.request('GET', url)

    return response.data


def tag_mp3_file(filepath, video_id, title, artist, year):
    """

    """
    audiofile = eyed3.load(filepath)

    if audiofile.tag == None:
        audiofile.initTag()

    audiofile.tag.title = title
    audiofile.tag.artist = artist
    audiofile.tag.album = title

    thumbnail = get_video_thumbnail(video_id)
    audiofile.tag.images.set(3, thumbnail, 'image/jpeg')

    _year = eyed3.core.Date(year)
    audio.tag.recording_date = _year

    audiofile.tag.save()